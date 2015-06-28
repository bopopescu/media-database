# Copyright 2014 Google Inc. All Rights Reserved.

"""Help document markdown helpers."""

import argparse
import collections
import re
import StringIO
import textwrap

from googlecloudsdk.calliope import usage_text


SPLIT = 78  # Split lines longer than this.
SECTION_INDENT = 10  # Section or list within section indent.
FIRST_INDENT = 2  # First line indent.
SUBSEQUENT_INDENT = 6  # Subsequent line indent.


class Error(Exception):
  """Exceptions for the markdown module."""


def Markdown(command):
  """Generates a markdown help document for command.

  Args:
    command: calliope._CommandCommon, Help extracted from this calliope command
        or group.

  Returns:
    The generated markdown string.
  """
  command.LoadAllSubElements()

  buf = StringIO.StringIO()
  out = buf.write
  detailed_help = getattr(command, 'detailed_help', {})
  command_name = ' '.join(command.GetPath())
  file_name = '_'.join(command.GetPath())
  top_element = command._TopCLIElement()  # pylint: disable=protected-access
  is_top_element = command == top_element

  def IsGlobalFlag(arg):
    """Checks if arg is a global (top level) flag.

    Args:
      arg: The argparse arg to check.

    Returns:
      True if arg is a global flag.
    """
    return arg.unique_flag or (arg in top_element.ai.flag_args)

  def IsGroupFlag(arg):
    """Checks if arg is a group only flag.

    Args:
      arg: The argparse arg to check.

    Returns:
      True if arg is a group only flag.
    """
    return arg.group_flag

  def IsSuppressed(arg):
    """Checks if arg help is suppressed.

    Args:
      arg: The argparse arg to check.

    Returns:
      True if arg help is suppressed.
    """
    return arg.help == argparse.SUPPRESS

  def UserInput(msg):
    """Returns msg with user input markdown.

    Args:
      msg: str, The user input string.

    Returns:
      The msg string with embedded user input markdown.
    """
    return (usage_text.MARKDOWN_CODE + usage_text.MARKDOWN_ITALIC +
            msg +
            usage_text.MARKDOWN_ITALIC + usage_text.MARKDOWN_CODE)

  def Section(name, sep=True):
    """Prints the section header markdown for name.

    Args:
      name: str, The manpage section name.
      sep: boolean, Add trailing newline.
    """
    out('\n\n== {name} ==\n'.format(name=name))
    if sep:
      out('\n')

  def PrintSectionIfExists(name, default=None):
    """Print a section of the .help file, from a part of the detailed_help.

    Args:
      name: str, The manpage section name.
      default: str, Default help_stuff if section name is not defined.
    """
    help_stuff = detailed_help.get(name, default)
    if not help_stuff:
      return
    if callable(help_stuff):
      help_message = help_stuff()
    else:
      help_message = help_stuff
    Section(name)
    out('{message}\n'.format(message=textwrap.dedent(help_message).strip()))

  def PrintFlagSection(flags, section):
    if not flags:
      return
    Section(section, sep=False)
    for flag in sorted(flags, key=lambda f: f.option_strings):
      out('\n{0}::\n'.format(usage_text.FlagDisplayString(flag, markdown=True)))
      out('\n{arghelp}\n'.format(arghelp=Details(flag)))

  def PrintCommandSection(name, subcommands):
    """Prints a group or command section.

    Args:
      name: str, The section name singular form.
      subcommands: dict, The subcommand dict.
    """
    # Determine if the section has any content.
    content = ''
    for subcommand, help_info in sorted(subcommands.iteritems()):
      if command.IsHidden() or not help_info.is_hidden:
        # If this group is already hidden, we can safely include hidden
        # sub-items.  Else, only include them if they are not hidden.
        content += '\n*link:{cmd}[{cmd}]*::\n\n{txt}\n'.format(
            cmd=subcommand,
            txt=help_info.help_text)
    if content:
      Section(name + 'S')
      out('{cmd} is one of the following:\n'.format(cmd=UserInput(name)))
      out(content)

  def Details(arg):
    """Returns the detailed help message for the given arg."""
    help_stuff = getattr(arg, 'detailed_help', (arg.help or '') + '\n')
    if callable(help_stuff):
      help_message = help_stuff()
    else:
      help_message = help_stuff
    return textwrap.dedent(help_message).replace('\n\n', '\n+\n').strip()

  def Split(line):
    """Splits long example command lines.

    Args:
      line: str, The line to split.

    Returns:
      str, The split line.
    """
    ret = ''
    m = SPLIT - FIRST_INDENT - SECTION_INDENT
    n = len(line)
    while n > m:
      indent = SUBSEQUENT_INDENT
      j = m
      noflag = 0
      while True:
        if line[j] == ' ':
          # Break at a flag if possible.
          j += 1
          if line[j] == '-':
            break
          # Look back one more operand to see if it's a flag.
          if noflag:
            j = noflag
            break
          noflag = j
          j -= 2
        else:
          # Line is too long -- force an operand split with no indentation.
          j -= 1
          if not j:
            j = m
            indent = 0
            break
      ret += line[:j] + '\\\n' + ' ' * indent
      line = line[j:]
      n = len(line)
      m = SPLIT - SUBSEQUENT_INDENT - SECTION_INDENT
    return ret + line

  subcommands = command.GetSubCommandHelps()
  subgroups = command.GetSubGroupHelps()

  out('= {0}(1) =\n'.format(file_name.upper()))

  Section('NAME')
  out('{{command}} - {index}\n'.format(index=command.index_help))

  # Post-processing will make the synopsis a hanging indent.
  # MARKDOWN_CODE is the default SYNOPSIS font style.
  code = usage_text.MARKDOWN_CODE
  em = usage_text.MARKDOWN_ITALIC
  Section('SYNOPSIS')
  out('{code}{command}{code}'.format(code=code, command=command_name))

  # Output the positional args up to the first REMAINDER or '-- *' args. The
  # rest will be picked up after the flag args are output. argparse does not
  # have an explicit '--' arg intercept, so we use the metavar value as a '--'
  # sentinel.
  positional_args = command.ai.positional_args[:]
  while positional_args:
    arg = positional_args[0]
    if arg.nargs == argparse.REMAINDER or arg.metavar.startswith('-- '):
      break
    positional_args.pop(0)
    out(usage_text.PositionalDisplayString(arg, markdown=True))

  # rel is the relative path offset used to generate ../* to the reference root.
  rel = 1
  if subcommands and subgroups:
    out(' ' + em + 'GROUP' + em + ' | ' + em + 'COMMAND' + em)
  elif subcommands:
    out(' ' + em + 'COMMAND' + em)
  elif subgroups:
    out(' ' + em + 'GROUP' + em)
  else:
    rel = 2

  # Places all flags into a dict. Flags that are in a mutually
  # exlusive group are mapped group_id -> [flags]. All other flags
  # are mapped dest -> [flag].
  global_flags = False
  groups = collections.defaultdict(list)
  for flag in command.ai.flag_args + command.ai.ancestor_flag_args:
    if IsGlobalFlag(flag) and not is_top_element:
      global_flags = True
    else:
      group_id = command.ai.mutex_groups.get(flag.dest, flag.dest)
      groups[group_id].append(flag)

  for group in sorted(groups.values(), key=lambda g: g[0].option_strings):
    if len(group) == 1:
      arg = group[0]
      if IsSuppressed(arg):
        continue
      msg = usage_text.FlagDisplayString(arg, markdown=True)
      if arg.required:
        out(' {msg}'.format(msg=msg))
      else:
        out(' [{msg}]'.format(msg=msg))
    else:
      group.sort(key=lambda f: f.option_strings)
      group = [flag for flag in group if not IsSuppressed(flag)]
      msg = ' | '.join(usage_text.FlagDisplayString(arg, markdown=True)
                       for arg in group)
      # TODO(user): Figure out how to plumb through the required
      # attribute of a required flag.
      out(' [{msg}]'.format(msg=msg))
  if global_flags:
    out(' [' + em + 'GLOBAL-FLAG ...' + em + ']')

  # positional_args will only be non-empty if we had -- ... or REMAINDER left.
  for arg in positional_args:
    out(usage_text.PositionalDisplayString(arg, markdown=True))

  PrintSectionIfExists('DESCRIPTION',
                       default=usage_text.ExpandHelpText(command,
                                                         command.long_help))
  PrintSectionIfExists('SEE ALSO')

  if command.ai.positional_args:
    Section('POSITIONAL ARGUMENTS', sep=False)
    for arg in command.ai.positional_args:
      out('\n{0}::\n'.format(
          usage_text.PositionalDisplayString(arg, markdown=True).lstrip()))
      out('\n{arghelp}\n'.format(arghelp=Details(arg)))

  # Partition the flags into FLAGS, GROUP FLAGS and GLOBAL FLAGS subsections.
  command_flags = []
  group_flags = []
  global_flags = False
  for arg in command.ai.flag_args:
    if not IsSuppressed(arg):
      if IsGlobalFlag(arg) and not is_top_element:
        global_flags = True
      elif IsGroupFlag(arg):
        group_flags.append(arg)
      else:
        command_flags.append(arg)
  for arg in command.ai.ancestor_flag_args:
    if not IsSuppressed(arg):
      if IsGlobalFlag(arg) and not is_top_element:
        global_flags = True
      else:
        group_flags.append(arg)

  for flags, section in ((command_flags, 'FLAGS'),
                         (group_flags, 'GROUP FLAGS')):
    PrintFlagSection(flags, section)

  if global_flags:
    Section('GLOBAL FLAGS', sep=False)
    out('\nRun *$ gcloud help* or *$ gcloud --help* for a description of the\n'
        'global flags available to all commands.\n')

  if subgroups:
    PrintCommandSection('GROUP', subgroups)
  if subcommands:
    PrintCommandSection('COMMAND', subcommands)

  PrintSectionIfExists('EXAMPLES')

  if command.IsHidden() or command.ReleaseTrack(for_help=True).help_note:
    Section('NOTES')
    if command.IsHidden():
      # This string must match gen-help-docs.sh to prevent the generated html
      # from being bundled.
      out('This command is an internal implementation detail and may change or '
          'disappear without notice.\n\n')
    if command.ReleaseTrack(for_help=True).help_note:
      out(command.ReleaseTrack(for_help=True).help_note + '\n\n')

  # This allows formatting to succeed if the help has any {somekey} in the text.
  doc = usage_text.ExpandHelpText(command, buf.getvalue())

  # Split long $ ... example lines.
  pat = re.compile(r'(\$ .{%d,})$' % (SPLIT - FIRST_INDENT - SECTION_INDENT),
                   re.M)
  pos = 0
  rep = ''
  while True:
    match = pat.search(doc, pos)
    if not match:
      break
    rep += doc[pos:match.start(1)] + Split(doc[match.start(1):match.end(1)])
    pos = match.end(1)
  if rep:
    doc = rep + doc[pos:]

  # $ command ... example refs.
  top = command.GetPath()[0]
  # This pattern matches "$ {top} {arg}*" where each arg is lower case and does
  # not start with example-, my-, or sample-. This follows the style guide rule
  # that user-supplied args to example commands contain upper case chars or
  # start with example-, my-, or sample-.
  pat = re.compile(r'\$ (' + top +
                   '((?: (?!(example|my|sample)-)[a-z][-a-z]*)*))[ `\n]')
  pos = 0
  rep = ''
  while True:
    match = pat.search(doc, pos)
    if not match:
      break
    cmd = match.group(1)
    i = cmd.find('set ')
    if i >= 0:
      # This terminates the command at the first positional ending with set.
      # This handles gcloud set and unset subcommands where 'set' and 'unset'
      # are the last command args, the remainder user-specified.
      i += 3
      rem = cmd[i:]
      cmd = cmd[0:i]
    else:
      rem = ''
    ref = match.group(2)
    if ref:
      ref = ref[1:]
    ref = '/'.join(['..'] * (len(command.GetPath()) - rel) + ref.split(' '))
    lnk = 'link:' + ref + '[' + cmd + ']' + rem
    rep += doc[pos:match.start(1)] + lnk
    pos = match.end(1)
  if rep:
    doc = rep + doc[pos:]

  # gcloud ...(1) man page refs.
  pat = re.compile(r'(\*?(' + top + r'((?:[-_ a-z])*))\*?)\(1\)')
  pos = 0
  rep = ''
  while True:
    match = pat.search(doc, pos)
    if not match:
      break
    cmd = match.group(2).replace('_', ' ')
    ref = match.group(3).replace('_', ' ')
    if ref:
      ref = ref[1:]
    ref = '/'.join(['..'] * (len(command.GetPath()) - rel) + ref.split(' '))
    lnk = '*link:' + ref + '[' + cmd + ']*'
    rep += doc[pos:match.start(2)] + lnk
    pos = match.end(1)
  if rep:
    doc = rep + doc[pos:]

  # ``*'' emphasis quotes => UserInput(*)
  pat = re.compile(r'(``([^`]*)\'\')')
  pos = 0
  rep = ''
  while True:
    match = pat.search(doc, pos)
    if not match:
      break
    rep += doc[pos:match.start(1)] + UserInput(match.group(2))
    pos = match.end(1)
  if rep:
    doc = rep + doc[pos:]

  return doc

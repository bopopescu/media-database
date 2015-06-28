@echo off
rem Copyright 2013 Google Inc. All Rights Reserved.

echo WARNING: 'gcutil' has been deprecated and is no longer part of default Cloud SDK distribution. >&2
echo WARNING: Please use 'gcloud compute' instead. >&2
echo WARNING: For more information see https://cloud.google.com/compute/docs/gcutil >&2
echo. >&2

SET GCUTIL_SCRIPT=%~dp0bootstrapping\gcutil.py

IF EXIST %GCUTIL_SCRIPT% GOTO GCUTIL_INSTALLED

echo WARNING: If you still must use 'gcutil', you can install it via >&2
echo WARNING: 'gcloud components update gcutil', >&2
echo WARNING: but note this option will also soon will be removed. >&2

exit /b 1

:GCUTIL_INSTALLED

SETLOCAL EnableDelayedExpansion


rem <cloud-sdk-cmd-preamble>
rem
rem  CLOUDSDK_ROOT_DIR            (a)  installation root dir
rem  CLOUDSDK_PYTHON              (u)  python interpreter path
rem  CLOUDSDK_PYTHON_ARGS         (u)  python interpreter arguments
rem  CLOUDSDK_PYTHON_SITEPACKAGES (u)  use python site packages
rem
rem (a) always defined by the preamble
rem (u) user definition overrides preamble

SET CLOUDSDK_ROOT_DIR=%~dp0..
SET PATH=%CLOUDSDK_ROOT_DIR%\bin\sdk;%PATH%

IF "%CLOUDSDK_PYTHON%"=="" (
  SET CLOUDSDK_PYTHON=python.exe
)

IF "%CLOUDSDK_PYTHON_SITEPACKAGES%" == "" (
  IF "!VIRTUAL_ENV!" == "" (
    SET CLOUDSDK_PYTHON_SITEPACKAGES=
  ) ELSE (
    SET CLOUDSDK_PYTHON_SITEPACKAGES=1
  )
)
SET CLOUDSDK_PYTHON_ARGS_NO_S=%CLOUDSDK_PYTHON_ARGS:-S=%
IF "%CLOUDSDK_PYTHON_SITEPACKAGES%" == "" (
  IF "!CLOUDSDK_PYTHON_ARGS!" == "" (
    SET CLOUDSDK_PYTHON_ARGS=-S
  ) ELSE (
    SET CLOUDSDK_PYTHON_ARGS=!CLOUDSDK_PYTHON_ARGS_NO_S! -S
  )
) ELSE IF "%CLOUDSDK_PYTHON_ARGS%" == "" (
  SET CLOUDSDK_PYTHON_ARGS=
) ELSE (
  SET CLOUDSDK_PYTHON_ARGS=!CLOUDSDK_PYTHON_ARGS_NO_S!
)

rem </cloud-sdk-cmd-preamble>


"%COMSPEC%" /C ""%CLOUDSDK_PYTHON%" %CLOUDSDK_PYTHON_ARGS% "%GCUTIL_SCRIPT%" %*"

"%COMSPEC%" /C exit %ERRORLEVEL%

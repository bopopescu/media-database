import Ember from 'ember';

export
default Ember.Component.extend({
  actions: {
    search: function() {
      var q = this.get('query');
      $('input').val('');
      this.sendAction('action', this.get('query'));
    }
  }
});
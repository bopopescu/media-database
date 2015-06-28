import Ember from 'ember';

export
default Ember.Component.extend({
  actions: {
    search: function() {
      this.sendAction('action', this.get('query'));
    }
  }
});
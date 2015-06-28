import Ember from 'ember';

export
default Ember.Route.extend({
  beforeModel: function(transition) {
    this.set('params', transition.queryParams);
  },
  model: function() {
    this.get('params.q');
    return this.store.find('media-item');
  }
});
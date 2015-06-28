import Ember from 'ember';

export
default Ember.Route.extend({
  model: function() {
    var item = this.store.createRecord('media-item');
    this.set('item', item);
    return item;
  },
  actions: {
    save: function() {
      this.get('item').save();
    }
  }
});
import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.resource('media', {
    path: '/'
  }, function() {
    this.route('add');
    this.route('edit', {
      path: '/:id'
    });
    this.route('view', {
      path: '/:id'
    });
  });
  this.route('search');
});

export
default Router;
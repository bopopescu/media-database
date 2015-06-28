import DS from 'ember-data';

export
default DS.Model.extend({
  title: DS.attr('string'),
  year: DS.attr('number'),
  review: DS.attr('string'),
  rating: DS.attr('number')
}).reopenClass({
  FIXTURES: [{
    id: 1,
    title: 'Avatar',
    year: 2012,
    review: 'terrible!',
    rating: 80
  }, {
    id: 2,
    title: 'Inception',
    year: 2010,
    review: 'amazing!',
    rating: 100
  }, {
    id: 3,
    title: 'Forrest Gump',
    year: 1994,
    review: 'great!',
    rating: 100
  }]
});
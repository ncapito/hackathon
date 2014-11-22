

angular.module('App').config(function($stateProvider, $urlRouterProvider, $httpProvider) {
  $urlRouterProvider.otherwise(function(){
    return  '/';

  });
  $stateProvider
    .state('home', {
      url: "/",
      controller : 'MainCtrl',
      templateUrl: '/partials/main.html',
      resolve    : { 'guestService': 'guestService' },
    })
    .state('invite', {
      url: "/invite",
      controller : 'InsertCtrl',
      templateUrl: '/partials/insert.html'
    })
    .state('update', {
      controller : 'UpdateCtrl',
      templateUrl: '/partials/update.html',
      resolve    : { 'guestService': 'guestService' },
    });
  });
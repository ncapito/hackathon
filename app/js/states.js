

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
    .state('devices', {
      url: "/devices",
      controller : 'DeviceCtrl',
      templateUrl: '/partials/device.html'
    })
    .state('add', {
      url: "/add",
      controller : 'DeviceAddCtrl',
      templateUrl: '/partials/device.add.html'
    });

  });

(function(angular){

'use strict';

var App = angular.module('App', ['ngResource','ui.router','ngAnimate']);

App.factory('myHttpInterceptor', function($rootScope, $q) {
  return {
    'requestError': function(config) {
      $rootScope.status = 'HTTP REQUEST ERROR ' + config;
      return config || $q.when(config);
    },
    'responseError': function(rejection) {
      $rootScope.status = 'HTTP RESPONSE ERROR ' + rejection.status + '\n' +
                          rejection.data;
      return $q.reject(rejection);
    },
  };
});

App.factory('guestService', function($rootScope, $http, $q, $log) {
  $rootScope.status = 'Retrieving data...';
  var deferred = $q.defer();
  $http.get('/api/devices/')
  .success(function(data, status, headers, config) {
    $rootScope.devices = data;
    deferred.resolve();
    $rootScope.status = '';
  });
  return deferred.promise;
});



App.config(function($httpProvider) {
  $httpProvider.defaults.headers.common.Authorization = 'Bearer e2110423b7a483d778daf6525141e2bbb694b8eb71cd04da1c27414f7e328711';
  $httpProvider.defaults.headers.common.Accept = 'application/vnd.littlebits.v2+json';
  $httpProvider.defaults.headers.delete = { "Content-Type": "application/json;charset=utf-8" };
  $httpProvider.interceptors.push('myHttpInterceptor');
});

})(angular);

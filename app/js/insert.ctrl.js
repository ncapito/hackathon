 angular.module('App').controller('InsertCtrl', function($scope, $rootScope, $log, $http, $stateParams, $location, $state) {
  $scope.device = {};
  $scope.submitInsert = function() {
    $rootScope.status = 'Creating...';
    $http.post('/api/devices/', $scope.device)
    .success(function(data, status, headers, config) {
      $rootScope.devices.push(data);
      $rootScope.status = '';
    });
    $location.path('/');
  };
});

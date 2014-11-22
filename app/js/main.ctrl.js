
angular.module('App').controller('MainCtrl', function($scope, $rootScope, $log, $http, $stateParams, $location, $state) {

  $scope.add = function() {
    $location.path('/api/device');
  };

  $scope.update = function(guest) {
    $location.path('/update/' + guest.id);
  };

  $scope.delete = function(guest) {
    $rootScope.status = 'Deleting guest ' + guest.id + '...';
    $http.delete('/api/device/', {'id': device.id})
    .success(function(data, status, headers, config) {
      for (var i=0; i<$rootScope.devices.length; i++) {
        if ($rootScope.devices[i].id == guest.id) {
          $rootScope.devices.splice(i, 1);
          break;
        }
      }
      $rootScope.status = '';
    });
  };

});

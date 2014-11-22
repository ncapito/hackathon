
angular.module('App').controller('UpdateCtrl', function($stateParams, $rootScope, $scope, $log, $http, $location) {

  for (var i=0; i<$rootScope.guests.length; i++) {
    if ($rootScope.guests[i].id == $stateParams.id) {
      $scope.guest = angular.copy($rootScope.guests[i]);
    }
  }

  $scope.submitUpdate = function() {
    $rootScope.status = 'Updating...';
    $http.post('/rest/update', $scope.guest)
    .success(function(data, status, headers, config) {
      for (var i=0; i<$rootScope.guests.length; i++) {
        if ($rootScope.guests[i].id == $scope.guest.id) {
          $rootScope.guests.splice(i,1);
          break;
        }
      }
      $rootScope.guests.push(data);
      $rootScope.status = '';
    });
    $location.path('/');
  };

});


angular.module('App').controller('MainCtrl', function($scope, $rootScope, $log, $http, $stateParams, $location, $state) {

  $scope.invite = function() {
    $location.path('/invite');
  };

  $scope.update = function(guest) {
    $location.path('/update/' + guest.id);
  };

  $scope.delete = function(guest) {
    $rootScope.status = 'Deleting guest ' + guest.id + '...';
    $http.post('/rest/delete', {'id': guest.id})
    .success(function(data, status, headers, config) {
      for (var i=0; i<$rootScope.guests.length; i++) {
        if ($rootScope.guests[i].id == guest.id) {
          $rootScope.guests.splice(i, 1);
          break;
        }
      }
      $rootScope.status = '';
    });
  };

});

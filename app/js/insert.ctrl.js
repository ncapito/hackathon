 angular.module('App').controller('InsertCtrl', function($scope, $rootScope, $log, $http, $stateParams, $location, $state) {

  $scope.submitInsert = function() {
    var guest = {
      first : $scope.first,
      last : $scope.last,
    };
    $rootScope.status = 'Creating...';
    $http.post('/rest/insert', guest)
    .success(function(data, status, headers, config) {
      $rootScope.guests.push(data);
      $rootScope.status = '';
    });
    $location.path('/');
  };
});

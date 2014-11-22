angular.module('App').controller('SubscriptionCtrl',
  function($scope, $resource, $rootScope, $log, $http, $stateParams, $location, $state) {
    var token = 'e2110423b7a483d778daf6525141e2bbb694b8eb71cd04da1c27414f7e328711';
    var save = $resource('http://localhost:8080/idevices/');

    var device = $resource('https://api-http.littlebitscloud.cc/devices/:device_id/',
      {"device_id": "@device_id"},{query: {
              method: 'GET',
              headers: {
                  'Authorization': 'Bearer ' + token
              },
              isArray: true
          }});

    $scope.device = new device();

    device.query(function(data){
      $scope.devices = data;
    });

    $scope.test = new save();

    var clazz = $resource('https://api-http.littlebitscloud.cc/subscriptions',
        {"subscriber_id": "@subscriber_id"},
    {


        query: {
                method: 'GET',
                headers: {
                    'Authorization': 'Bearer ' + token
                },
                isArray: true
            },
            save: {
              method: 'POST',
              headers: {
                  'Authorization': 'Bearer ' + token
              }
          },
          delete: {
            method: 'DELETE',
            headers: {
                'Authorization': 'Bearer ' + token
            }
        }
    });

    $scope.add  =function(){
      $scope.addMe = true;
      $scope.subscription = new clazz();
    };
    $scope.close = function(){
      $scope.addMe = false;
      $scope.subscription = null;

    };
    $scope.delete = function(d){
      d.$delete({subscriber_id: d.subscriber_id, publisher_id: d.publisher_id});
    };
    $scope.create = function(){
      console.log($scope.subscription);
      $scope.subscription.subscriber_id = 'http://rmc-room-finder.appspot.com/api/devices/' +
        $scope.subscription.publisher_id + '/';

      $scope.subscription.$save();
    };
    $scope.subscriptions = clazz.query({publisher_id: '00e04c0201cd'});
});

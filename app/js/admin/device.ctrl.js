angular.module('App').controller('DeviceCtrl',
  function($scope, $http, $resource,$log) {
    var Subscriber = $resource('https://api-http.littlebitscloud.cc/v2/subscriptions?publisher_id=:publisher_id&subscriber_id=:subscriber_id',
        {"subscriber_id": "@sid",
        "publisher_id": "@pid"}
      );


    var Device = $resource('https://api-http.littlebitscloud.cc/v2/devices/:device_id/:action',
        {"device_id": "@id"},
        {
          'update': { method:'PUT' },
          output:{
            params:{
              action: 'output'
            }
          },
          input:{
            params:{
              action: 'input'
            }
          },
        });


    Device.query(function(data){
      $scope.devices = data;
    });

    $scope.msg = '';


    $scope.getInput = function(device){
        if(device.processing){
          return;
        }
        device.processing = true;

        device.$input(function(data){
            device.processing = false;
            device.lastInput = data;
        },function(error){

        });
    };

    $scope.close = function(){
      $scope.addMe = false;
      $scope.subscription = null;

    };
    $scope.delete = function(d){
      d.$delete(function(){
        $scope.msg = 'Deleted';
      });
    };

    $scope.save = function(device){
      delete device._edit;
      device.$update();
    };

    $scope.addRMCSubscriber = function(device){
      var sub = new Subscriber({
        subscriber_id : 'http://rmc-room-finder.appspot.com/api/devices/' + device.id + '/',
        publisher_id:  device.id,
        publisher_events:  ['amplitude:delta:release', 'amplitude:delta:ignite' ]
      });

      sub.$save(function(){
        $scope.msg = 'success';
        device.$get();
      });

    };

    $scope.hasRMCSubscriber = function(device){
        var found = _.find(device.subscribers, function(item){
          //look for one that starts/contains rmc-room-finder
          return !!~item.sid.indexOf('rmc-room-finder.appspot.com/api/devices/' + device.id);
        });
        return found !== undefined;
    };


    $scope.deleteSubscriber = function(subscriber, d){
      var body = {publisher_id: subscriber.pid, subscriber_id: subscriber.sid };
        $http({url: 'https://api-http.littlebitscloud.cc/v2/subscriptions', method: 'DELETE', data: body}).then(function(res) {
            $scope.msg = 'deleted';
            d.$get();
        }, function(error) {
            $scope.msg = 'failed';
            console.log(error);
        });

    };

});

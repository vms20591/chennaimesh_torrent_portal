(function(){
    var torrentService=angular.module('torrentService',[]);

        function service($http,$q){
            var defer=$q.defer();

            var successCallback=function(response){
                defer.resolve(response.data);
            };
                            
            var failureCallback=function(response){
                defer.reject(response.data);
            };
                                    
            //Get Torrents from DB
            this.retrieveTorrents=function(bookmark){
                $http({
                    method:'get',
                    url:'torrents/',
                    config:{
                        headers:{
                            'Content-Type':'application/json'
                        }
                    },
                    responseType:'json'
                }).then(successCallback,failureCallback);

                return defer.promise;
            };
        }

        //Torrent Service holds all the methods required to talk with the api and retrieve results
        torrentService.service('torrentService',service);
})();

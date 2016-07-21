(function(){
	var app=angular.module('torrentController',['torrentService']);
	
        var errorTexts={
            loadingTorrent:'searching stash...',
            emptyTorrent:'No Torrents found !!!',
            errorTorrent:'Error occured while retrieving Torrents !!!'
        };

	app.controller('torrentHomeController',function($scope,torrentService,$timeout){
            
        $scope.searchState=0;
        $scope.applicationState=0;;
        $scope.errorText=''
        $scope.searchQuery='';

        //method to call torrent service and retrieve the list of torrents
        $scope.retrieveTorrents=function(){
            var promise=torrentService.retrieveTorrents();
                                                
            promise.then(function(data){
                if(data && data.torrents){
                    var result=data.torrents;

                    if(result && result.length>0){
                        $scope.torrents=result;

                        $scope.applicationState=1;
                    }
                }
                else{
                    $scope.applicationState=2;
                    $scope.errorText=errorTexts.emptyTorrent
                    console.log(errorTexts.emptyTorrent);
                }

            },function(data){
                $scope.applicationState=3;
                $scope.errorText=errorTexts.errorTorrent;
                console.log(errorTexts.errorTorrent);
            });
        };

        //method to call torrent service and retrieve the list of torrents based on search query
        $scope.searchTorrents=function(){
            var promise=torrentService.retrieveTorrents($scope.searchQuery);
            
            $scope.searchState=1;
            $scope.errorText=errorTexts.loadingTorrent;

            promise.then(function(data){
                if(data && data.torrents){
                    var result=data.torrents;

                    if(result && result.length>0){
                        $scope.torrents=result;
                        $scope.searchState=0;
                    }
                }
                else{
                    $scope.searchState=2;
                    $scope.errorText=errorTexts.emptyTorrent
                    console.log(errorTexts.emptyTorrent);
                }

            },function(data){
                $scope.searchState=3;
                $scope.errorText=errorTexts.errorTorrent;
                console.log(errorTexts.errorTorrent);
            });
        };

        $scope.copiedToClipboard=function(index){
           $scope.copied=index;

           $timeout(function(){
                $scope.copied=null;
           },1000);
        }

        $scope.retrieveTorrents();

    });
})();

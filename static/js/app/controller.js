(function(){
	var app=angular.module('torrentController',['torrentService']);
	
        var errorTexts={
            emptyTorrent:'No Torrents found !!!',
            errorTorrent:'Error occured while retrieving Torrents !!!'
        };

	app.controller('torrentHomeController',function($scope,torrentService){
            
        $scope.showTorrents=true;
        $scope.errorText=''

        //method to call torrent service and retrieve the list of folders and populate $scope.folders.folderList
        $scope.retrieveTorrents=function(){
            var promise=torrentService.retrieveTorrents();
                                                
            promise.then(function(data){
                if(data && data.torrents){
                    var result=data.torrents;

                    if(result && result.length>0){
                        $scope.torrents=result;
                    }
                }
                else{
                    $scope.showTorrents=false;
                    $scope.errorText=errorTexts.emptyTorrent
                    console.log(errorTexts.emptyTorrent);
                }
            },function(data){
                $scope.showTorrents=false;
                $scope.errorText=errorTexts.errorTorrent;
                console.log(errorTexts.errorTorrent);
            });
        };

        $scope.retrieveTorrents();

    });
})();

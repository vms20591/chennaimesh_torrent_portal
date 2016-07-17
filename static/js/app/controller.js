(function(){
	var app=angular.module('torrentController',[]);
	
	app.controller('torrentHomeController',function($scope){
	    $scope.searchInput="";	
            $scope.torrentResults=[
                {
                    name:"Arch",
                    category:"Linux",
                    type:"url",
                    url:"http://archlinux.org"
                },
                {
                    name:"Fedora",
                    category:"Linux",
                    type:"magnet",
                    url:"magnet:?xt.1=urn:sha1:YNCKHTQCWBTRNJIV4WNAE52SJUQCZO5C&xt.2=urn:sha1:TXGCZQTH26NL6OUQAJJPFALHG2LTGBC7"
                }

            ];
	});
})();

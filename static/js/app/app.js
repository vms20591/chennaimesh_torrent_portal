(function(){
	var app=angular.module('torrentApp',['torrentController']);

        app.config(['$compileProvider', function($compileProvider) {
            $compileProvider.aHrefSanitizationWhitelist(/^\s*(https?|ftp|mailto|magnet|file|tel):/);
        }]);
})();

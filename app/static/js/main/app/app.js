(function(){
	var app=angular.module('torrentApp',['torrentController','ngclipboard']);

        //Added this to avoid clash with django's template loader
        app.config(function($interpolateProvider) {
            $interpolateProvider.startSymbol('{[{');
            $interpolateProvider.endSymbol('}]}');
        });

        app.config(['$compileProvider', function($compileProvider) {
            $compileProvider.aHrefSanitizationWhitelist(/^\s*(https?|ftp|mailto|magnet|file|tel):/);
        }]);
})();

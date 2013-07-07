define([
    'jquery' 
   ,'underscore'
   ,'backbone'
   ,'handlebars'
], function($, _, Backbone, Handlebars, MainPageTemplate) {
    
    var AppRouter = Backbone.Router.extend({});

    var initialize = function() {
        var appRouter = new AppRouter(); 
        /*
        appRouter.on('route:showLogin', function() {
            var loginView = new LoginView();
            loginView.render();
        });*/

        //Magic that starts Backbone
        Backbone.history.start();
    };

    return {
        'initialize': initialize
    };
});

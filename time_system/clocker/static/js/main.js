requirejs.config({
    shim: {
       'handlebars': {
           exports: 'Handlebars'
       }

       ,'underscore': {
           exports: '_'
       }

       ,'backbone': {
            deps: ['underscore', 'jquery']
           ,exports: 'Backbone'
        }
    },

    baseUrl: '/static/js',

    paths: {
         jquery: "//cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min"
        ,underscore: "libs/underscore"
        ,backbone: "libs/backbone"
        ,handlebars: "libs/handlebars"
        ,templates: "../templates"
    }
    
});

require([
    'app',
    ], function(App) {
        App.initialize(); 
});

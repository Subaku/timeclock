define([
    'jquery'
   ,'underscore'
   ,'backbone'
   ,'router'
], function($, _, Backbone, Router) {

    var initialize = function() {

        //Sets up csrf token for Django when we make post requests
        var _sync = Backbone.sync;
        Backbone.sync = function(method, model, options) {
            options.beforeSend = function(xhr) {
                var token = $('meta[name="csrf-token"]').attr('content');
                xhr.setRequestHeader('X-XSRFToken', token);
            };
            return _sync(method, model, options);
        };

        Router.initialize();
    }
    
    //Handy snippet that bundles up form fields into js object
    $.fn.serializeObject = function() {
        var o = {};
        var a = this.serializeArray();
        $.each(a, function() {
          if (o[this.name] !== undefined) {
              if (!o[this.name].push) {
                  o[this.name] = [o[this.name]];
              }
              o[this.name].push(this.value || '');
          } else {
              o[this.name] = this.value || '';
          }
        });
        return o;
    }; 
        
    return {
        initialize: initialize
    };
});


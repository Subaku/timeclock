from django.http import HttpResponseRedirect, HttpResponse
from settings import SESSION_TIMEOUT

class CheckAccess():
    '''
    ' Middleware that validates that a user is logged into the app and is active.
    '''

    def process_view(self, request, view_func, args, kwargs):
       
        #If there are decorators then make sure none of them are 
        #'login_exempt' before continueing
        if hasattr(view_func, '_decorators'):
            for dec in view_func._decorators:
                if dec.__name__ == "login_exempt":
                    return None
       
        #Boot back to login page
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/')

        #Give custom page telling them they are no longer active
        if not request.user.isActive:
            return HttpResponse("user no longer active!")
        
        request.session.set_expiry(SESSION_TIMEOUT)
        return None


from django.http import HttpResponse
from django.template import loader, RequestContext
from django.contrib.auth import authenticate, login
#from django.core.context_processors import csrf
#from django.contrib.auth import logout as auth_logout
#from check_access import check_access
#from clocker.models import Employee

def renderLogin(request, context=None):

    if context is None or not isinstance(context, dict):
        context = {}

    t = loader.get_template('login.html')
    c = RequestContext(request, context)
    return HttpResponse(t.render(c), mimetype="text/html")


def loginUser(request):
    
    #TODO: check_access or middleware
   
    #TODO: proper 404 handling
    if request.method != 'POST':
        return HttpResponse('404');
    
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')
    user = authenticate(username=username, password=password)
    if user is None:
        return renderLogin(request, {'error': "Incorrect username or password"})

    if not user.isActive:
        return renderLogin(request, {'error': "User is deactivated"})
    
    login(request, user)

    t = loader.get_template('app.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c), mimetype="text/html")



'''
def view(request):

    error = ''

    response = check_access(request)
    if(isinstance(response, Employee)):
        return HttpResponseRedirect('/timeclock/')

    if request.method == 'POST':
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/timeclock/')
            else:
                error = "Account disabled"
        else:
            error = "Invalid login";


    request.user = None
    t = loader.get_template('login.html');
    c = RequestContext(request, {'error':error})
    c.update(csrf(request));
    return HttpResponse(t.render(c))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/timeclock/login/")
'''

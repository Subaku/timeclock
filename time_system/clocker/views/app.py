
from django.http import HttpResponse
from django.template import loader, RequestContext

def renderApp(request):
    
    t = loader.get_template('app.html')
    c = RequestContext(request, {})
    return HttpResponse(t.render(c), mimetype="text/html")



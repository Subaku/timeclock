from django.conf.urls import patterns, include, url
#from django.views.generic import RedirectView
#from django.contrib import admin
#from dajaxice.core import dajaxice_config, dajaxice_autodiscover
#from settings import APP_PATH, DEBUG
#admin.autodiscover()
#dajaxice_autodiscover()


#login views
urlpatterns = patterns('clocker.views.login',
    url(r'^$', 'renderLogin', name="render-login"),
    url(r'^login/$', 'loginUser', name="login"),
)


'''
#normal views
urlpatterns += patterns('clocker.views',
    
    url(r'^$', RedirectView.as_view(url='/timeclock/')),
    url(r'^timeclock/$', 'main_page'),

    url(r'^timeclock/hours/$', 'total_hours'),

    url(r'(?i)^utilities/', include('chucho.urls')),                                                                                                                                                
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

if DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^images\/(?P<path>.+)$', 'django.views.static.serve', {
            'document_root': APP_PATH + 'chucho/static/plugins/slickGrid/images'})
    )

#shift_summary stuff
urlpatterns += patterns('clocker.shift_summary',
    url(r'^timeclock/shift_summary/$', 'summary'),
)
'''

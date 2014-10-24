from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^items/?$', 'main.views.get_or_create_items'),
    url(r'^articles/?$', 'main.views.get_article'),
)

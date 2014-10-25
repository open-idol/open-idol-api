from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^items/?$', 'main.views.get_or_create_items'),
    url(r'^(?P<item>\w+)/articles/?$', 'main.views.get_article'),
)

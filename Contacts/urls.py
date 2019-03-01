from django.conf.urls import url
from . import views

app_name = 'Contacts'
urlpatterns = [
    # view all contacts
    # contacts/

    url(r'^$', views.index, name='index'),

    # view specific contact
    # contacts/3/
    url(r'^(?P<contact_id>[0-9]+)/$', views.detail, name='detail')
]

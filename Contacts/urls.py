from django.conf.urls import url
from . import views

app_name = 'Contacts'
urlpatterns = [
    # view all contacts
    # contacts/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # view specific contact
    # contacts/3/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /contacts/add
    url(r'add/$', views.ContactCreate.as_view(), name='contact-add'),

    # /contacts/2
    url(r'contact/(?P<pk>[0-9]+)/$', views.ContactUpdate.as_view(), name='contact-update'),

    # /contacts/2/delete
    url(r'contact/(?P<pk>[0-9]+)/delete$', views.ContactDelete.as_view(), name='contact-delete')
]

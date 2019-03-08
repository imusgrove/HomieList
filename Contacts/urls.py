from django.conf.urls import url
from django.conf import settings
from . import views
from .views import (searchcontacts)
from django.contrib.auth.views import logout


app_name = 'Contacts'
urlpatterns = [
    # view all contacts
    # contacts/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # view specific contact
    # contacts/3/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /contacts/add
    url(r'^add/$', views.ContactCreate.as_view(), name='contact-add'),

    # contacts/contacts/2---for updating
    url(r'^contacts/(?P<pk>[0-9]+)/$', views.ContactUpdate.as_view(), name='contact-update'),

    # /contacts/2/delete---for deleting
    url(r'^contact/(?P<pk>[0-9]+)/delete/$', views.ContactDelete.as_view(), name='contact-delete'),

    # logout
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    #search
    url(r'^$', searchcontacts, name='searchcontacts')
]

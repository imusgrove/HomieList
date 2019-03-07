from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Contact

class IndexView(generic.ListView):
    template_name = 'Contacts/index.html'
    context_object_name = 'all_contacts'
    def get_queryset(self):
        return Contact.objects.all()

class DetailView(generic.DetailView):
    model = Contact
    template_name = 'Contacts/detail.html'

class ContactCreate(CreateView):
    model = Contact
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'street_address', 'headshot']

class ContactUpdate(UpdateView):
    model = Contact
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'street_address', 'headshot']

class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('Contacts:index')






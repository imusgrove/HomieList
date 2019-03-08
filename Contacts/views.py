from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .models import Contact
from .forms import UserForm


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

# registration form
class UserFormView(View):
    form_class = UserForm
    template_name = 'Contacts/registration_form.html'
    # blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Contacts:index')

        return render(request, self.template_name,{'form': form})

# class SearchView(generic.DetailView):
#     def search(self, request):
#         if request.method == 'GET':
#             first_name = request.GET.get('search')
#             try:
#                 status=Contact.objects.filter(first_name__icontains=first_name)
#             except Contact.DoesNotExist:
#                 status = None
#             return render(request, 'Contacts/search.html', {"contacts": status})
#         else:
#             return render(request, 'Contacts/search.html', {})











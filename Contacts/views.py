from django.shortcuts import render, get_object_or_404
from .models import Contact

def index(request):
    all_contacts = Contact.objects.all()
    return render(request, 'Contacts/index.html', {'all_contacts': all_contacts})

def detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'Contacts/detail.html', {'contact': contact})



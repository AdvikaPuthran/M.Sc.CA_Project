from django.shortcuts import render, redirect
from .forms import CustomerEnquiryForm

def contact_view(request):
    success = False
    if request.method == "POST":
        form = CustomerEnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = CustomerEnquiryForm()

    return render(request, "contact/contact.html", {"form": form, "success": success})

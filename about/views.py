from django.shortcuts import render, redirect
from .models import About
from .forms import CollaborateForm
from django.contrib import messages


# Create your views here.

def about_me(request):
    """
    Render the most recent About Me page and handle collaboration form. :model:`about.About`.
    **context**
    'about'
        Latest instance of :model:`about.About`.
    'collaborate_form'
        An instance of :model:`about.CollaborateForm`.
    **Template:**
    :template:`about/about.html`
    """

    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(request, "Collaboration request received! I endeavour to respond within 2 working days.")
            # PRG pattern to avoid resubmission and ensure message shows after redirect
            return redirect('about')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )

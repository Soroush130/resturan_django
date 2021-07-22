from django.shortcuts import render, HttpResponse, redirect
from .forms import ResevationForm
from .models import Reseve


# Create your views here.

def reseveation(request):

    if request.method == "POST":
        reseve_form = ResevationForm(request.POST)
        if reseve_form.is_valid():
            reseve_form.save()
            return redirect('/')
    else:
        reseve_form = ResevationForm()

    context = {
        'form': reseve_form,
    }
    return render(request, 'reserve/reserve.html', context)

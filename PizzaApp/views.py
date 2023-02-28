from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *

def index(request):
    if request.method == "POST":
				# create a new copy of the form with the data the user 
				# entered , it is stored in request.POST
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza1 = form.save() # create the Employee object and save it
						# send the user to a confirmation page saying
						# confirming that they filled in the form and the data was saved 
            #return render(request, 'details.html', {'pizza1':pizza1})
            print(pizza1.toppings.all())
            return redirect('details', pizza1.id)
        else:
						# form has errors
						# send the form back to the user
            return render(request, 'index.html', {'form': form})
    else:
        # normal get reuqest, user wants to see the form 
        form = PizzaForm()

        return render(request, 'index.html', {'form': form})

def details(request, pizzaid):
    pizza = get_object_or_404(Pizza, id=pizzaid)
    if request.method == "POST":
				# create a new copy of the form with the data the user 
				# entered , it is stored in request.POST
        form1 = DetailsForm(request.POST)
        if form1.is_valid():
            customer=form1.save() # create the Employee object and save it
						# send the user to a confirmation page saying
						# confirming that they filled in the form and the data was saved 
            return render(request, 'confirmation.html', {'customer':customer,'pizza':pizza})
        else:
						# form has errors
						# send the form back to the user
            return render(request, 'details.html', {'form1': form1, 'pizza':pizza})
    else:
        # normal get reuqest, user wants to see the form 
        form1 = DetailsForm()
    return render(request, 'details.html', {'form1': form1, 'pizza':pizza})


def confirmation(request):
    return render(request, 'confirmation.html')

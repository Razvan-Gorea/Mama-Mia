from django import forms
from .models import * 
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime



class PizzaForm(forms.ModelForm):
    toppings = forms.ModelMultipleChoiceField(
        queryset=Toppings.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    
    class Meta:
        model = Pizza
        fields = ['size', 'toppings', 'crust', 'sauces', 'cheese']




class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['first_name', 'last_name', 'card_number', 'date', 'card_cvv', 'address', 'pizza_details']

        widgets = {
        'date': forms.TextInput(attrs={'placeholder': 'MM/YY'}),
        'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
        'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        'card_number': forms.TextInput(attrs={'placeholder': 'Card Number'}),
        'card_cvv': forms.TextInput(attrs={'placeholder': 'CVV'}),
        'address': forms.TextInput(attrs={'placeholder': 'Address'}),
      }
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise ValidationError(_('Please enter a first name'))
        
        if not first_name.isalpha():
            raise ValidationError(_('First name can only contain letters'))
        
        return first_name.capitalize()
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise ValidationError(_('Please enter a last name'))
        
        if not last_name.isalpha():
            raise ValidationError(_('Last name can only contain letters'))
        
        return last_name.capitalize()

          
    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number')
        if not card_number:
            raise ValidationError(('Please enter a card number'))
        # Remove all non-digit characters from the card number
        card_number = ''.join(filter(str.isdigit, card_number))
        if len(card_number) < 12:
            raise ValidationError(('Card number must be at least 12 digits long'))
        return card_number

    def clean_card_cvv(self):
        card_cvv = self.cleaned_data.get('card_cvv')
        if not card_cvv:
            raise ValidationError(('Please enter a CVV'))
        # Remove all non-digit characters from the CVV
        card_cvv = ''.join(filter(str.isdigit, card_cvv))
        if len(card_cvv) < 3:
            raise ValidationError(('CVV must be at least 3 digits long'))
        return card_cvv
    
    def clean_date(self):
        date = self.cleaned_data.get('date')
        if not date:
            raise ValidationError(_('Please enter a date'))

        try:
            # Attempt to parse the date string into a datetime object
            parsed_date = datetime.datetime.strptime(date, '%m/%y').date()
        except ValueError:
            # If the date cannot be parsed, raise a validation error
            raise ValidationError(_('Invalid date format'))

        # Check if the date is in the past
        if parsed_date < datetime.date.today():
            raise ValidationError(_('Expiration date must be in the future'))

        # Return the parsed date
        return parsed_date.strftime('%m/%y')
    

    def __init__(self, *args, **kwargs):
        super(DetailsForm, self).__init__(*args, **kwargs)
        self.fields['pizza_details'].required = False    
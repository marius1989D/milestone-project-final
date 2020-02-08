from django import forms
from .models import Order

class MakePaymentForm(forms.Form):
	"""cardNumber = forms.CharField(label='Credit card number', required=False)
	cardExpiry = forms.IntegerField(default=0)
	cardCvc = forms.IntegerField(default=0)"""



"""
	MONTH_CHOICES = [(i, i) for i in range(1, 12)]
	YEAR_CHOICES = [(i, i) for i in range(2019, 2040)]

	credit_card_number = forms.CharField(label='Credit card number', required=False)
	cvv = forms.CharField(label='Security code (CVV)', required=False)
	expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
	expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
	stripe_id = forms.CharField(widget=forms.HiddenInput)
"""
class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('full_name','email', 'phone_number', 'country', 'post_code', 'town_or_city', 'street_address')
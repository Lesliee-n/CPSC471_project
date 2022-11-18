from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ticket
from django import forms
from tkinter import Widget

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = "__all__"

        # price_option = (
        #     ('Adult Ticket','Adult Ticket $10.00'),
        #     ('Kid Ticket','Kid Ticket $5.00')
        # )
        # labels ={
		# 	'show_time_movie_id':'what movie showtime do you want to see?',
    	# 	'seat_number':'Seat numbers available are from 1 to 10. Input your selection:',
    	# 	'row_letter':'Row letters avauable are from A to G. Input your selection',
    	# 	'classification':'Are you a loyalty member?',
    	# 	'price':'Select your ticket price.',
    	# 	'date':'Input the movie date',
    	# 	'customer_account_number':'What is your account number?'
        # }
        # widgets = {
		# 	'seat_number':forms.TextInput(attrs={'class':'form-control'}),
		# 	'row_letter':forms.TextInput(attrs={'class':'form-control'}),
		# 	'classification':forms.TextInput(attrs={'class':'form-control'}),
		# 	'price' :forms.Select(choices=price_option, attrs={'class':'form-control'})
        # }


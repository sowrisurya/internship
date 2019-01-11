from django import forms

class loginform(forms.Form):
    username = forms.CharField(label='Your User Name', max_length=100)
    password = forms.CharField(label='Your Password', max_length=100, widget=forms.PasswordInput)

class registerform(forms.Form):
	types = (
		('seller','seller'),
		('user','user'),
		('clinic','clinic'),
		('hospital','hospital'),
		('bloodbank','bloodbank'),
		('diagnostic','diagnostic'),
	)

	username = forms.CharField(label='Your User Name', max_length=100)
	password = forms.CharField(label='Your Password', max_length=100, widget=forms.PasswordInput)
	password2 = forms.CharField(label='Your Password again', max_length=100, widget=forms.PasswordInput)
	fname = forms.CharField(label='Your First Name', max_length=100)
	lname = forms.CharField(label='Your Last Name', max_length=100)
	email = forms.EmailField(label='Your email')
	user_type = forms.ChoiceField(label = "Which Category?",choices=types)


from django import forms
from .models import User

class UserForm(forms.ModelForm):
     class Meta:
        model = User
        fields = '__all__'

        labels = {
            'uid': 'User ID',
            'firstName' : 'First Name',
            'lastName' : 'Last Name.' ,
            'profession' : 'Profession' ,
            'age' : 'Age',
            'Address' : 'Address' ,
        }

        widgets  ={
            'uid' : forms.NumberInput(attrs={'placeholder': 'ID number'}),
            'firstName' : forms.TextInput(attrs={'placeholder': 'First Name'}),
            'lastName' : forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'profession' : forms.TextInput(attrs={'placeholder': 'profession'}),
            'age' : forms.NumberInput(attrs={'placeholder': 'age'}),
            'Address' : forms.Textarea(attrs={'placeholder': 'Address'}),
        }
class UserIdForm(forms.Form):
    user_ids = forms.CharField(label='User IDs', widget=forms.TextInput(attrs={'placeholder': 'Enter user IDs separated by spaces'}))

# from django import forms

# class TodoForm(forms.Form):
#     title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
#         'class': 'w-full p-2 border border-gray-300 rounded mt-1',
#         'placeholder': 'Enter task title'
#     }))
#     description = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'w-full p-2 border border-gray-300 rounded mt-1',
#         'placeholder': 'Enter task description',
#         'rows': 4
#     }), required=False) 
#     due_date = forms.DateField(widget=forms.DateInput(attrs={
#         'class': 'w-full p-2 border border-gray-300 rounded mt-1',
#         'type': 'date'  
#     }))
#     category=forms.CharField(max_length=50, widget=forms.TextInput(attrs={
#         'class': 'w-full p-2 border border-gray-300 rounded mt-1',
#         'placeholder': 'Enter task category'
#     })) 
    
from django import forms
class CustomSignupForm(forms.Form):
    first_name=forms.CharField(max_length=30, label='First Name', required=False)
    last_name=forms.CharField(max_length=30, label='Last Name', required=False)
    
    def signup(self, request, user):
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.save()     
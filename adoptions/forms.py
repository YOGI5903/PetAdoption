# from django import forms
# from .models import Pet
# from django.forms import ModelForm

# class PetFilterForm(forms.Form):
#     BREED_CHOICES = [
#         ('', 'All'),
#         ('breed1', 'Breed 1'),
#         ('breed2', 'Breed 2'),
#         # Add more breed choices
#     ]

#     pet_type = forms.ChoiceField(choices=Pet.PET_TYPE_CHOICES, required=False)
#     breed = forms.ChoiceField(choices=BREED_CHOICES, required=False)
#     min_age = forms.IntegerField(label='Min Age', required=False)
#     max_age = forms.IntegerField(label='Max Age', required=False)


# class RehomeForm(forms.Form):
#     name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'floatingInput','placeholder':'Name'}))
#     breed = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':''}))
#     age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'name'}))
#     pet_type = forms.ChoiceField(choices=[('dog', 'Dog'), ('cat', 'Cat')],widget=forms.Select(attrs={'class':'name'}))
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class':'name'}))
 
        

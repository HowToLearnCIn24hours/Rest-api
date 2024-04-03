from django import forms


#Form to enter name of the city user wants to buy tour to
class Cityform(forms.Form):
    choose_city = forms.CharField(label="Найти город", max_length=200)


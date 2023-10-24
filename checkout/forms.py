from django import forms


class ShippingAddressForm(forms.Form):
    shipping_address = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Please enter your shipping address'}))

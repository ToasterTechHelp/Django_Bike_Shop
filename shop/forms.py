from django import forms


class BikePurchaseForm(forms.Form):
    name = forms.CharField(
        label='your name:',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'John'})
    )
    surname = forms.CharField(
        label='your surname:',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Smith'})
    )
    phone_number = forms.CharField(
        label='your phone number:',
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': '000-000-0000'})
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")

        if len(phone_number) < 10 or len(phone_number) > 15:
            raise forms.ValidationError("Phone number must be between 10 and 15 digits.")

        return phone_number
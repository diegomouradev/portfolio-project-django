from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=20, help_text="eg. Marilyn")
    last_name = forms.CharField(max_length=80, help_text="Monroe")
    email = forms.EmailField(
        required=true, error_messages="oops! try again.", help_text="ash.catcher@pokemon.com")

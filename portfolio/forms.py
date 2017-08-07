from django import forms

class ContactForm(forms.Form):
    contact_name= forms.CharField(required=True)
    contact_email= forms.EmailField(required=True)
    content= forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"

class NumberInput(forms.Form):
    number_val = forms.NumberInput()

    def __init__(self, *args, **kwargs):
        super(NumberInput, self).__init__(*args, **kwargs)
        self.fields['number_val'].label = "Enter a post number:"
from django import forms
from .models import Student

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        label="Email",
        max_length=40,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter your email'})
    )
    message = forms.CharField(
        label="Message",
        max_length=50,
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control my-2', 'placeholder': 'Enter your message'})
    )

    def clean(self):
        cleaned_data = super().clean()
        
        name = cleaned_data.get('name')
        if name and len(name) < 3:
            raise forms.ValidationError("Minimum 3 characters are required for name.")
        
        return cleaned_data


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

    # Optionally customize widgets here
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control my-2',
            'placeholder': 'Enter your name'
        })
        self.fields['age'].widget.attrs.update({
            'class': 'form-control my-2',
            'placeholder': 'Enter your age'
        })

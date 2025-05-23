from django import forms
from .models import Email,EmailVerificationEvent
from . import css
from .services import verify_email, start_verification_event


class EmailForm(forms.Form):  
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "id": "email-login-input",
            'class' : css.EMAIL_FIELD_CSS,
            'placeholder': 'Enter your email',
        }))
    # class Meta: 
    #     model = EmailVerificationEvent
    #     fields = ['email']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        verified = verify_email(email)
        if verified:
            raise forms.ValidationError("Invalid email, Please try again")
        return email
        
    
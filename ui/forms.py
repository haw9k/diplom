from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=150,
        label="Имя",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Имя",
        }),
    )
    last_name = forms.CharField(
        max_length=150,
        label="Фамилия",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Фамилия",
        }),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Адрес электронной почты",
        })
        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Пароль",
        })
        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Пароль ещё раз",
        })

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]


        if not user.username:
            user.username = self.cleaned_data["email"]

        user.save()
        return user

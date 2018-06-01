from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
	password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)

	class Meta:
		model = User

		fields = ('username', 'email',)

	def clean_password(self):
		pass1 = self.cleaned_data.get("password1")
		pass2 = self.cleaned_data.get("password2")

		if pass1 and pass2 and pass1 != pass2:
			raise forms.ValidationError("Passwords do not match")

		return pass2


	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email__iexact = email)

		if qs.exists():
			raise forms.ValidationError(f"{email} is already registered")

		return email
		

	def save(self, commit = True):
		user = super(RegisterForm, self).save(commit = False)
		user.set_password(self.cleaned_data["password1"])
		user.is_active = False

		if commit:
			user.save()
			user.profile.send_activation_mail()

		return user
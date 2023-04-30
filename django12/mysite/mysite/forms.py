# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from myapp.models import CustomUser

# class CustomUserAdminCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields + ('is_approved',)

#     def clean_is_approved(self):
#         is_approved = self.cleaned_data.get('is_approved')
#         if not self.instance.is_admin and is_approved:
#             raise forms.ValidationError('Only admin users can approve user registrations.')
#         return is_approved

# class CustomUserAdminForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'

#     def clean_is_approved(self):
#         is_approved = self.cleaned_data.get('is_approved')
#         if not self.instance.is_admin and is_approved:
#             raise forms.ValidationError('Only admin users can approve user registrations.')
#         return is_approved

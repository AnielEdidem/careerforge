from django import forms
from .models import CVProfile

class CVProfileForm(forms.ModelForm):
    class Meta:
        model = CVProfile
        fields = [
            "full_name", "email", "phone", "location", "target_role",
            "bio", "education", "experience", "skills", "projects",
            "certifications", "linkedin", "github"
        ]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 3}),
            "education": forms.Textarea(attrs={"rows": 4}),
            "experience": forms.Textarea(attrs={"rows": 6}),
            "skills": forms.Textarea(attrs={"rows": 3}),
            "projects": forms.Textarea(attrs={"rows": 4}),
            "certifications": forms.Textarea(attrs={"rows": 3}),
        }

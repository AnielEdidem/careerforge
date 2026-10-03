from django import forms
from .models import CVProfile


class CVProfileForm(forms.ModelForm):

    class Meta:
        model = CVProfile

        fields = [
            "full_name",
            "email",
            "phone",
            "location",
            "target_role",
            "bio",
            "education",
            "experience",
            "skills",
            "projects",
            "certifications",
            "linkedin",
            "github",
        ]

        labels = {
            "full_name": "Full name",
            "email": "Email address",
            "phone": "Phone number",
            "location": "Location",
            "target_role": "Target job / role",
            "bio": "Professional summary",
            "education": "Education",
            "experience": "Work experience",
            "skills": "Skills",
            "projects": "Projects",
            "certifications": "Certifications",
            "linkedin": "LinkedIn profile",
            "github": "GitHub profile",
        }

        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Aniel Edidem",
                    "autocomplete": "name",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "e.g. aniel@example.com",
                    "autocomplete": "email",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "e.g. +234 801 234 5678",
                }
            ),

            "location": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Port Harcourt, Nigeria",
                }
            ),

            "target_role": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Python Developer",
                }
            ),

            "bio": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Briefly describe yourself, your strengths, and career goals...",
                }
            ),

            "education": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "School, degree, field of study, graduation year...",
                }
            ),

            "experience": forms.Textarea(
                attrs={
                    "rows": 7,
                    "placeholder": "Company, job title, responsibilities, achievements...",
                }
            ),

            "skills": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Python, Django, JavaScript, Git, SQL...",
                }
            ),

            "projects": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Project name, what you built, technologies used, results...",
                }
            ),

            "certifications": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Certification name, organization, year...",
                }
            ),

            "linkedin": forms.URLInput(
                attrs={
                    "placeholder": "https://linkedin.com/in/yourname",
                }
            ),

            "github": forms.URLInput(
                attrs={
                    "placeholder": "https://github.com/yourusername",
                }
            ),
        }
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CVProfileForm
from .models import CVProfile
from .services import generate_cv_content
from .pdf import make_cv_pdf

def home(request):
    if request.method == "POST":
        form = CVProfileForm(request.POST)
        if form.is_valid():
            profile = form.save()
            try:
                result = generate_cv_content(profile)
                profile.generated_summary = result.get("summary", "")
                profile.generated_experience = result.get("experience", "")
                profile.save(update_fields=["generated_summary", "generated_experience"])
            except Exception:
                # Keep the user's data even if AI generation fails.
                pass
            return redirect("cv:preview", pk=profile.pk)
    else:
        form = CVProfileForm()
    return render(request, "cv/home.html", {"form": form})

def preview(request, pk):
    profile = get_object_or_404(CVProfile, pk=pk)
    return render(request, "cv/preview.html", {"profile": profile})

def download_pdf(request, pk):
    profile = get_object_or_404(CVProfile, pk=pk)
    return make_cv_pdf(profile)

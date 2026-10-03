
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .forms import CVProfileForm
from .models import CVProfile
from .services import generate_cv_content
from .pdf import make_cv_pdf




def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("cv:home")

        return render(
            request,
            "registration/login.html",
            {"error": "Invalid username or password."}
        )

    return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    return redirect("cv:login")



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("cv:home")

    else:
        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {"form": form}
    )


@login_required
def home(request):
    if request.method == "POST":
        form = CVProfileForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            try:
                result = generate_cv_content(profile)

                profile.generated_summary = result.get("summary", "")
                profile.generated_experience = result.get("experience", "")

                profile.save(
                    update_fields=[
                        "generated_summary",
                        "generated_experience"
                    ]
                )

            except Exception:
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

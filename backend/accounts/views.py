from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .decorators import admin_required
from .forms import SignupForm


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect("brawl")
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Cycle the session and sign the new member in.
            login(request, user)
            return redirect("/brawl/")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


class MemberLoginView(LoginView):
    # LoginView validates ?next= with url_has_allowed_host_and_scheme,
    # so unsafe external redirects are rejected.
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class MemberLogoutView(LogoutView):
    # Django 5+ accepts POST only; auth.logout() flushes the session.
    next_page = "/"


@admin_required
def admin_control(request):
    return render(request, "accounts/admin_control.html")

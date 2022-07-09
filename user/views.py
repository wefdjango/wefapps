from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.views import generic
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # group = Group.objects.get(name="Customers")
            # user.groups.add(group)
            messages.success(
                request,
                (
                    "You have successfully register, you can now login and update your profile"
                ),
            )
            return redirect("user-login")
    else:
        form = CreateUserForm()
    context = {"form": form}
    return render(request, "user/register.html", context)


def profile(request):
    context = {}
    return render(request, "user/profile.html", context)


@login_required
def profile_update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, ("Your profile was successfully updated!"))
            return redirect("user-profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "user/profile_update.html", context)


# class AllProfilesView(generic.ListView):
#     model = Profile
#     context_object_name = "profiles"

#     queryset = Profile.objects.filter(title__icontains="war")[:5]
#     template_name = "books/my_arbitrary_template_name_list.html"  # Specify your own template name/location

# if request.method != "POST":
#     u_form = UserUpdateForm(instance=request.user)
#     p_form = ProfileUpdateForm(instance=request.user.profile)

# context = {
#     "u_form": u_form,
#     "p_form": p_form,
# }
# return render(request, "user/profile_update.html", context)

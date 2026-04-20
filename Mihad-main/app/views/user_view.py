from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from app.forms import UserForm, ProfileForm
from app.models import Profile


@login_required
def profile(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    return render(request, 'app/profile.html', {'user_form': user_form, 'profile_form': profile_form})


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('password_change_done')
    form_class = PasswordChangeForm


class CustomPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('password_reset_done')


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name_suffix = '_update_form'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy('profile')

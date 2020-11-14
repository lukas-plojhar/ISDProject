from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from . import forms
from .models import Profile

def update_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=User.objects.get(pk=request.user.id))
        profile.birthdate = request.POST.get('birthdate')
        profile.telephone = request.POST.get('telephone')
        profile.privacy_settings = request.POST.get('privacy_settings')
        profile.save()

    return redirect(to='/profiles/edit')

class EditProfileView(FormView):
    template_name = 'profile/edit.html'
    form_class = forms.UpdateProfileForm
    success_url = '/home'
    context = {}

    def get(self, request):
        """
        Finds Profile using User one-to-one relation, that is found by user.id stored in request
        """
        profile = Profile.objects.get(user=User.objects.get(pk=request.user.id))
        self.context.update(form = forms.UpdateProfileForm(instance=profile))
        return render(request, 'profile/edit.html', self.context)

    # def form_valid(self, form):
    #     form.user = self.request.user
    #     form.instance.save()
    #     return super().form_valid(form)


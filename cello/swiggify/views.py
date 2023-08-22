from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.views.generic.list import ListView

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts

# Create your views here.
class GenerateRandomUserView(FormView):
    template_name = 'swiggify/random_generate.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('users_list')
    
class UsersListView(ListView):
    template_name = 'swiggify/users_list.html'
    model = User

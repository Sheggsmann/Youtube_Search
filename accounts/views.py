from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('login')
        else:
            messages.error(request, 'An Error Occurred')
    user_form = UserRegistrationForm()
    context = {'form': user_form}
    return render(request, 'accounts/register.html', context)
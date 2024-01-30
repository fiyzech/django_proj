# users/views.py
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
import requests
from .models import User
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    form = UserForm(request.POST or None, instance=user)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'users/edit.html', {'form': form, 'user': user})

def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'users/delete.html', {'user': user})


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'password', 'first_name', 'last_name', 'email']


def add_users(request):
    if request.method == 'POST':
        num_users = int(request.POST.get('num_users', 0))

        api_url = 'https://random-data-api.com/api/v2/users'
        response = requests.get(api_url, params={'size': num_users})

        try:
            users_data_list = response.json()
        except ValueError:
            users_data_list = []

        for user_data in users_data_list:

            if isinstance(user_data, dict):
                user_form = UserForm(user_data)
                if user_form.is_valid():
                    user_form.save()

        return redirect('user_list')

    return render(request, 'users/add_users.html')
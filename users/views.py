from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def UserRegisterView(request):
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        #username = form.cleaned_data.get('username')
        return redirect('login')

    context = {'form':form}
    template_name = 'users/register.html'
    return render(request, template_name, context)

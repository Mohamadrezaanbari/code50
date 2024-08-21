from django.shortcuts import render, redirect
from .models import User
from .form import UserForm , UserIdForm



def UserFormView(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'CRUD/order.html'
    return render(request, template_name, {
        'form': form
        })

def showView(request):
    obj = User.objects.all()
    template_name = 'CRUD/list.html'
    return render(request, template_name, {
        'obj': obj
        })

def updateView(request, id):
    obj = User.objects.get(uid=id)
    form = UserForm(instance=obj)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'CRUD/order.html'
    return render(request, template_name, {
        'form': form
        })

def deleteView(request, id):
    obj = User.objects.get(uid=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('show')
    template_name = 'CRUD/confirmation.html'
    return render(request, template_name, {
        'obj': obj
        })

def userdetailview(request):
     if request.method == 'POST':
        form = UserIdForm(request.POST)
        if form.is_valid():
            user_ids = form.cleaned_data['user_ids'].split(' ')
            users = User.objects.filter(uid__in=user_ids)
            return render(request, 'CRUD/details.html', {
                'users': users
            })
        else:
            form = UserIdForm(request.POST)
            return render(request, 'CRUD/input.html', {
                'form': form
            })
     else:
        form = UserIdForm()
        return render(request, 'CRUD/input.html', {
            'form': form
        })

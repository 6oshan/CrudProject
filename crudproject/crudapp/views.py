from django.shortcuts import render, redirect
from .models import Crud
from django.contrib import messages
# from django.views.generic import ListView,DetailView

# Create your views here.
def demo(request):
    task1 = Crud.objects.all()
    if request.method == 'POST':
        slno = request.POST.get('slno', '')
        name = request.POST.get('name', '')
        desc = request.POST.get('desc', '')
        crud = Crud(slno=slno, name=name, desc=desc)
        crud.save()
        messages.success(request, 'Data created successfully.')
    return render(request, "index.html", {'task1': task1})

def delete(request, crudid):
    crud = Crud.objects.get(id=crudid)
    if request.method == 'POST':
        crud.delete()
        return redirect('/')
    return render(request, 'delete.html')

def update(request, id):
    crud = Crud.objects.get(id=id)
    if request.method == 'POST':
        crud.slno = request.POST.get('slno', '')
        crud.name = request.POST.get('name', '')
        crud.desc = request.POST.get('desc', '')
        crud.save()
        return redirect('/')
    return render(request, 'edit.html', {'crud': crud})


# class  MyModelList(ListView):
#     model=Crud
#     template_name='classList.html'
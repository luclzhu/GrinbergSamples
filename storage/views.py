from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sample, CustomColumn
from .forms import SampleForm, CustomColumnForm

# Create your views here

def home(request):
    samples = Sample.objects.all()
    new_vars = CustomColumn.objects.all()
    return render(request, 'storage/spreadview.html', {'samples':samples, 'columns':new_vars})

def new_var(request):
    form = CustomColumnForm()
    if CustomColumn.objects.count() >= 3:
        return HttpResponse('You can only add a maximum of three new variables. Press the back arrow to return to the home page.')
    if request.method == 'POST':
        form = CustomColumnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'storage/column_form.html', context)

def update_var(request, pk):

    column = CustomColumn.objects.get(id=pk)
    form = CustomColumnForm(instance=column)

    if request.method == 'POST':
        form = CustomColumnForm(request.POST, instance=column)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'storage/column_form.html', context)

def delete_var(request,pk):
    column = CustomColumn.objects.get(id=pk)
    if request.method=='POST':
        column.delete()
        return redirect('home')

    context = {'item':column}
    return render(request, 'storage/delete_var.html', context)

def new_sample(request):
    form = SampleForm()
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'storage/sample_form.html', context)

def update_sample(request, pk):

    sample = Sample.objects.get(id=pk)
    form = SampleForm(instance=sample)

    if request.method == 'POST':
        form = SampleForm(request.POST, instance=sample)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'storage/sample_form.html', context)

def delete_sample(request,pk):
    sample = Sample.objects.get(id=pk)
    if request.method=='POST':
        sample.delete()
        return redirect('home')

    context = {'item':sample}
    return render(request, 'storage/delete_sample.html', context)
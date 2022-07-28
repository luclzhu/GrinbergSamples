from django.shortcuts import render, redirect
from django.http import HttpResponse
import django

from storage.models import Sample, UserCustomColumn
from storage.forms import SampleForm, UserCustomColumnForm

# Create your views here

def enhance_sample(samples, columns):
    for sample in samples:
        for column in columns:
            if column.internal_title  not in sample.custom_values:
                sample.custom_values[column.internal_title] = '---'
                sample.unpacked_list.append('---')
            else:
                sample.unpacked_list.append(sample.custom_values[column.internal_title])

def home(request):
    columns = UserCustomColumn.objects.all().filter(in_use = True).order_by('UI_position') #filter by in_use = True
    samples = Sample.objects.all()
    enhance_sample(samples,columns)
    return render(request, 'storage/spreadview.html', {'samples':samples, 'columns':columns})

def new_sample(request):
    form = SampleForm()
    new_vars = UserCustomColumn.objects.all()

    if request.method == 'POST':
        form = SampleForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form, 'columns':new_vars}
    return render(request, 'storage/sample_form.html', context)

def update_sample(request, pk):

    sample = Sample.objects.get(id=pk)
    form = SampleForm(instance=sample)
    new_vars = UserCustomColumn.objects.all()
    print(new_vars)

    if request.method == 'POST':
        form = SampleForm(request.POST, instance=sample)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form,'columns':new_vars}
    return render(request, 'storage/sample_form.html', context)

def delete_sample(request,pk):
    sample = Sample.objects.get(id=pk)
    if request.method=='POST':
        sample.delete()
        return redirect('home')

    context = {'item':sample}
    return render(request, 'storage/delete_sample.html', context)

def new_var(request):
    form = UserCustomColumnForm()
    if request.method == 'POST':
        form = UserCustomColumnForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'storage/column_form.html', context)

def update_var(request, pk):

    column = UserCustomColumn.objects.get(id=pk)
    form = UserCustomColumnForm(instance=column)
    print(column)

    if request.method == 'POST':
        form = UserCustomColumnForm(request.POST, instance=column)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'storage/column_form.html', context)

def delete_var(request,pk):
    column = UserCustomColumn.objects.get(id=pk)
    samples = Sample.objects.all()
    if request.method=='POST':
        column.delete()
        for sample in samples:
            if column.internal_title in sample.custom_values:
                print(sample.custom_values[column.internal_title])
                del sample.custom_values[column.internal_title]
                print(sample.custom_values)
                #print(sample.custom_values[column.internal_title])
                Sample.save(sample)
        return redirect('home')

    context = {'item':column}
    return render(request, 'storage/delete_var.html', context)
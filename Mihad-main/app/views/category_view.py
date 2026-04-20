from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from products.models import Category
from products.forms import CategoryForm

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

@login_required
@staff_member_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_create.html', {'form': form})

@login_required
@staff_member_required
def category_edit(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_edit.html', {'form': form, 'category': category})

@login_required
@staff_member_required
def category_delete(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully')
        return redirect('category_list')
    return render(request, 'category_delete.html', {'category': category})


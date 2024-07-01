from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import CategoryForm, ProductForm

def products_view(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})

def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'store/categories.html', {'categories': categories})

def category_add_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_view')
    else:
        form = CategoryForm()
    return render(request, 'store/category_add.html', {'form': form})

def category_edit_view(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories_view')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'store/category_edit.html', {'form': form, 'category': category})

def category_delete_view(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('categories_view')

def product_add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_view', id=product.id)
    else:
        form = ProductForm()
    return render(request, 'store/product_add.html', {'form': form})

def product_edit_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_view', id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_edit.html', {'form': form, 'product': product})

def product_delete_view(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('products_view')

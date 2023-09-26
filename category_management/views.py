from django.shortcuts import render,redirect
from .models import Category
# Create your views here.


# ^ Category list
def categories(request):
    
    if not request.user.is_superuser:
        return redirect('admin_panel:login')
    categories=Category.objects.all()
    content={
        'categories':categories
    }
    return render(request,'admin_partition/category.html',content)

# ^ Category add

def add_category(request):
    category_name   = request.POST['category_name']
    parent          = None if request.POST['parent'] =='None' else request.POST['parent']
    description     = request.POST['description']
    soft_delete     = request.POST.get('soft_delete', False) != False
    image           = request.FILES['image']

    Category.objects.create(
        category_name   = category_name,
        parent          = Category.objects.get(category_name=parent),
        description     = description,
        # soft_delete     = soft_delete,
        category_img    = image,
    )
    return redirect('category:category_list')

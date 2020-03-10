from django.shortcuts import render,redirect
from .models import Product
from .forms import productForm


# Create your views here.
def product_list(request):
    context = {'product_list': Product.objects.all()}
    return render(request, "product/product_list.html", context)

def product_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = productForm()
        else:
            product = Product.objects.get(pk = id)
            form = productForm(instance=product)
        return render(request, "product/productform.html", {'form': form})
    else:
        if id == 0:
            form = productForm(request.POST)
        else:
            product = Product.objects.get(pk=id)
            form = productForm(request.POST,instance=product)
        if form.is_valid():
            form.save()

        return redirect('/product')



def product_delete(request,id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect('/product')

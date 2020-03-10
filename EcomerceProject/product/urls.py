from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static

from .views import product_list
from .views import product_form
from .views import product_delete

urlpatterns = [

                  path('', product_form, name='product_form'),
                  path('product/', product_list, name='product_list'),
                  path('<int:id>/', product_form, name='product_update'),
                  path('delete/<int:id>', product_delete, name='product_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

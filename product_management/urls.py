from django.urls import path
from . import views

app_name='product'

urlpatterns = [
    path('add_brand/',views.add_brand,name='add_brand'),
    path('add_attribute/',views.add_attribute,name='add_attribute'),
    path('add_attribute_value/',views.add_attribute_value,name='add_attribute_value'),
    # path('product_list/',views.product_list,name='product_list'),
    # path('add_product/',views.add_product,name='add_product'),
]
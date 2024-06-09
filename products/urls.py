from django.urls import path
from .views import getProducts,addProduct,updateProduct,deleteProduct


urlpatterns = [
    path('getproducts/', getProducts, name='getproducts'),
    path('addProduct/', addProduct, name='addProduct'),
    path('updateProduct/', updateProduct, name='updateProduct'),
    path('deleteProduct/', deleteProduct, name='deleteProduct')
]

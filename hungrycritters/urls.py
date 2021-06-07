from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.indexHome),
    path('product/<int:product_id>', views.viewProduct),
    path('cart/', views.viewCart),
    path('checkout/', views.viewCheckout),
    path('addtocart/<int:product_id>', views.addToCart),
    path('additem/<int:id>', views.addItem),
    path('removeitem/<int:id>', views.removeItem),
    path('processorder/<int:id>', views.processOrder)
]
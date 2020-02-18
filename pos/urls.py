from django.urls import path

from pos import views

urlpatterns = [
    path('accounts/login/', views.userlogin, name='userlogin'),
    path('ajaxgetproduct/', views.getProduct, name='ajaxgetproduct'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.billing, name='billing'),
    path('bs/', views.billing_success, name='billing_success'),
    path('order/', views.order, name='order'),

]

from django.urls import path
from . import views  # Just remove the space for cleanliness

urlpatterns = [
    path('', views.landingPageView, name="landingPage"),
    path('first/', views.firstPageView, name='firstpage'),
    path('pricing/', views.pricingPageView, name='pricepage'),
    path('contact/', views.contactPageView, name='contactpage'),
    path('pricing2/', views.pricingPageView2, name='pricingpage2'),
    path('index/', views.indexPageView, name='indexpage'),
    path('student/', views.studentPageView, name='studentpage'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login')
]

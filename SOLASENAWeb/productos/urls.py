from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    path('', views.productos_asfalticos, name='productosasfalticos' ),

    path('emulsionesasfalticas/', views.emulsiones_asfalticas, name='EmulsionesAsfalticas'),

]


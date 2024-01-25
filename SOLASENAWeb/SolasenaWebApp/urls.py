from django.urls import path
from SolasenaWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    path('sobrenosotros/', views.sobre_nosotros, name='sobrenosotros'),
    path('tienda/', views.tienda, name='tienda' ),
    path('combustible/', views.combustibles_alternos, name='combustible' ),
    
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
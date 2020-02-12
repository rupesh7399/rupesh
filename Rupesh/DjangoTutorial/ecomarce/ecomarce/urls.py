from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('eco.urls')),
    path('product/',include('products.urls')),
    path('search/',include('search.urls',namespace='search')),
    path('carts/',include('carts.urls')),
    path('addresses/',include('addresses.urls')),  
    path('accounts/',include('accounts.urls')),
    
]

if settings.DEBUG:
     urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
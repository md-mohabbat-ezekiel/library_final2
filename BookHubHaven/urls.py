from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Core.urls')),
    path('member/',include('Members.urls')),
    path('add/',include('bookCollection.urls')),
    path('transitions/',include('transitions.urls')),
    path('user/',include('profiles.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('site_admin/', admin.site.urls),
    path('', include('portfolios.urls')),
    path('comment/', include('blog.urls')),
    path('admin/', include('site_admin.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
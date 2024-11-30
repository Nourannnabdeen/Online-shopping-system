from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # Root path for the home page
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

    # Admin panel
    path('admin/', admin.site.urls),

    # API and app routes
    path('api/', include('shop.urls')),
]

# Add static and media URL handling during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
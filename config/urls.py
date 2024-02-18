import os

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get admin URL from environment variable, with a default fallback
admin_url = os.getenv('DJANGO_ADMIN_URL', 'admin/')

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('projects/', TemplateView.as_view(template_name="pages/projects.html"), name='projects'),
    path('snippets/', TemplateView.as_view(template_name="pages/snippets.html"), name='snippets'),
    path('contact/', TemplateView.as_view(template_name="pages/contact.html"), name='contact'),
    path('resume/', TemplateView.as_view(template_name="pages/resume.html"), name='resume'),
    # path('blog/', include('blog.urls', namespace='blog')),
    # path('projects/', include('projects.urls', namespace='projects')),
    # path('snippets/', include('snippets.urls', namespace='snippets')),
    path(admin_url, admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "My Admin"
admin.site.site_header = "My Admin"
admin.site.index_title = "My Admin"

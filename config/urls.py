import os

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get admin URL from environment variable, with a default fallback
admin_url = os.getenv('DJANGO_ADMIN_URL', 'admin/')

urlpatterns = [
    # path('', include('core.urls', namespace='core')),
    # path('blog/', include('blog.urls', namespace='blog')),
    # path('projects/', include('projects.urls', namespace='projects')),
    # path('snippets/', include('snippets.urls', namespace='snippets')),
    path(admin_url, admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "My Admin"
admin.site.site_header = "My Admin"
admin.site.index_title = "My Admin"

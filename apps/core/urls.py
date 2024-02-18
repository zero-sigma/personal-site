from django.urls import path, include
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView

app_name = "core"

urlpatterns = [
    path('', TemplateView.as_view(template_name="pages/home.html"), name='home'),
    
]
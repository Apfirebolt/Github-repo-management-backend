"""django_github URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('test', TemplateView.as_view(template_name='test.html'), name='test'),
    path('admin/', admin.site.urls),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('hub/', include(('github.urls', 'github'), namespace='github')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('forum/', include(('forum.urls', 'forum'), namespace='forum')),

    path('1', TemplateView.as_view(template_name='test/test1.html'), name='t1'),
    path('2', TemplateView.as_view(template_name='test/test2.html'), name='t2'),
    path('3', TemplateView.as_view(template_name='test/test3.html'), name='t3'),
    path('4', TemplateView.as_view(template_name='test/test4.html'), name='t4'),
    path('5', TemplateView.as_view(template_name='test/test5.html'), name='t5'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
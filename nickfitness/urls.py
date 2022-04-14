"""nickfitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from plans import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('plans/<int:pk>', views.plan, name='plan'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/signup', views.SignUp.as_view(), name='signup'),
    path('join', views.join, name='join'),
    path('checkout', views.checkout, name='checkout'),
    path('auth/settings', views.settings, name='settings'),
    path('updateaccounts', views.updateaccounts, name='updateaccounts'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('fitness', views.fitnessBlogs, name='fitnessBlogs'),
    path('fitness/<int:pk>', views.fitness, name='fitness'),
    path('food', views.foodsPage, name='foodsPage'),
    path('foods/<int:pk>',views.food,name='food'),
    path('health', views.healthBlogs, name='healthBlogs'),
    path('health/<int:pk>', views.health, name='health'),
    path('love', views.loveBlogs, name='loveBlogs'),
    path('love/<int:pk>', views.love, name='love'),
    path('beauty', views.beautyBlogs, name='beautyBlogs'),
    path('beauty/<int:pk>', views.beauty, name='beauty'),
    path('culture', views.cultureBlogs, name='cultureBlogs'),
    path('culture/<int:pk>', views.culture, name='culture'),
    path('blogs/<int:blog_id>',views.blogdetail,name='blogdetail')
]


if settings.DEBUG:
      urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
      urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





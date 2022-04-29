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
    path('password-reset/',views.ResetPassword.as_view(), name='password_reset'),
    path('join', views.join, name='join'),
    path('checkout', views.checkout, name='checkout'),
    path('auth/settings', views.settings, name='settings'),
    path('updateaccounts', views.updateaccounts, name='updateaccounts'),
    path('about', views.about, name='about'),
    path('fitness', views.fitnessBlogs, name='fitnessBlogs'),
    path('story=/fitness/<int:pk>', views.fitness, name='fitness'),
    path('food', views.foodsPage, name='foodsPage'),
    path('story=/food/<int:pk>',views.food,name='food'),
    path('health', views.healthBlogs, name='healthBlogs'),
    path('story=/health/<int:pk>', views.health, name='health'),
    path('love', views.loveBlogs, name='loveBlogs'),
    path('story=/love/<int:pk>', views.love, name='love'),
    path('beauty', views.beautyBlogs, name='beautyBlogs'),
    path('story=/beauty/<int:pk>', views.beauty, name='beauty'),
    path('culture', views.cultureBlogs, name='cultureBlogs'),
    path('story=/culture/<int:pk>', views.culture, name='culture'),
]



if settings.DEBUG:
      urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
      urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





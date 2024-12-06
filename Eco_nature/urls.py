"""Eco_nature URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about',views.about,name="about"),
    path('contactus',views.contactus,name="contactus"),
    path('footer',views.footer,name=""),
    path('gallery',views.gallery,name="gallery"),
    path('header',views.header,name=""),
    path('',views.index,name="index"),
    path('base',views.base,name=""),
    path('all current issue',views.all_current_issue,name="all_current_issue"),
    path('details current issue/<int:id>',views.details_current_issue,name="details_current_issue"),
    path('all news',views.all_news,name="all_news"),
    path('details news/<int:id>',views.details_news,name="details_news"),
    path('all faq',views.all_faq,name="all_faq"),
    path('all laws',views.all_laws,name="all_laws"),
    path('all university',views.all_university,name="all_university"),
    path('details_university/<int:id>',views.details_university,name="details_university"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('allenergy',views.allenergy,name="allenergy"),
    path('allhealth',views.allhealth,name="allhealth"),
    path('detailhealth/<int:id>',views.detailhealth,name="detailhealth"),
    path('alltechnology',views.alltechnology,name="alltechnology"),
    path('detailtechnology/<int:id>',views.detailtechnology,name="detailtechnology"),
    path('myprofile',views.myprofile,name="myprofile"),
    path('Edit profile',views.Edit_profile,name="Edit_profile"),
    path('change Password',views.change_password,name="change_password"),
    path('help&support',views.help_support,name="help_support"),
    path('review',views.review,name="review"),
    path('logout',views.logout,name="logout"),
    path('forgotpassword',views.forgotpassword,name="forgotpassword"),
    path('side',views.side,name=""),

    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
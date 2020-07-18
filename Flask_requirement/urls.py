"""Flask_requirement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name="main"),
    path('admin_page/',views.admin_page,name="admin_page"),
    path('save_adminlogin/',views.save_adminlogin,name="save_adminlogin"),
    path('home_page/',views.home_page,name="home_page"),
    path('schedule_class/',views.schedule_class,name="schedule_class"),
    path('save_schedule/',views.save_schedule,name="save_schedule"),
    path('view_all/',views.view_all,name="view_all"),
    path('show_update/',views.show_update,name="show_update"),
    path('update_record/',views.update_record,name="update_record"),
    path('student_login/',views.student_login,name="student_login"),
    path('delete/',views.delete,name="delete"),
    path('save_studentdata/',views.save_studentdata,name="save_studentdata"),
    path('student_home/',views.student_home,name="student_home"),
    path("login/",views.login,name="login"),
    path('login_s/',views.login_s,name="login_s"),
    path('welcome_student/',views.welcome_student,name="welcome_student"),
    path('entrol/',views.entrol,name="entrol")
]

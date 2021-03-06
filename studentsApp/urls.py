"""studentsApp URL Configuration

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
from home.views import home,login_fun,register,delete,search,student_id,Insert_Intake,Intakes_List,logout_fun
import re

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('login/', login_fun),
    path('register/', register),
    path('search/', search),
    path('logout/', logout_fun),
    path('delete/<int:student_id>/', delete, name="delete"),
    path('student/<int:student_id>/', student_id, name="student_id"),
    path('insertIntake/', Insert_Intake.as_view(), name="insertIntake"),
    path('intakes/', Intakes_List.as_view(), name="IntakeSList"),
]


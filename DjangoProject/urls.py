"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from authentication.views import user_login, user_register, user_profile, user_logout
from home.views import home
from vege.views import recipes, recipe_delete, recipe_edit, get_students, get_student_details

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('login',user_login, name='login' ),

    path('profile', user_profile, name='profile' ),
    path('register',user_register, name='register' ),

    path('logout',user_logout, name='logout' ),

    path('recipes',recipes, name='recipes' ),
    path('recipe_delete/<recipe_id>/',recipe_delete, name='recipe_delete' ),
    path('recipe_edit/<recipe_id>/', recipe_edit, name='recipe_edit' ),

    path('students', get_students, name='students' ),
    path('student-details/<str:student_id>/', get_student_details, name='student_details'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


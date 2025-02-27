"""
URL configuration for personal_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task_manager import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.CreatingTask, name = 'CreatingTask'),
    path('tasks/', views.TaskList, name='TaskList'),
    path('trash/', views.TrashList, name='TrashList'),
    path('tasks/delete/<int:task_id>/', views.DeleteTask, name='DeleteTask'),
    path('trash/restore/<int:task_id>/', views.RestoreTask, name='RestoreTask'),
    path('trash/delete_permanently/<int:task_id>/', views.DeletePermanently, name='DeletePermanently'),
    path('task/<int:id>/', views.ViewTask, name='ViewTask'),
    path('task/<int:id>/edit/', views.EditTask, name='EditTask'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


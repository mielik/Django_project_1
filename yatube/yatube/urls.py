from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Главная страница:
    # если получен запрос без относительного адреса
    # (то есть это запрос к имени домена, например yatube.com),
    # будет вызвана функция index() из файла views.py
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]

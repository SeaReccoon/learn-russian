from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Подключаем файлы маршрутов других приложений
# Также подключаем административную панель из django
# И пути для редактора ckeditor
urlpatterns = [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('admin/', admin.site.urls),
    path('lessons/', include("lessons.urls")),
    path('testing/', include("testing.urls")),
    path('user/', include('user.urls')),
    path('', include("main.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Подключаем обработку пути для медиа файлов

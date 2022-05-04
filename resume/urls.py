
from django.contrib import admin
from django.urls import path
from poll import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path('detail/<int:pk>',views.detail,name='detail'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

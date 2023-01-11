
from django.contrib import admin
from django.urls import path, include
# 업로드 된 파일을 접근하기 위한
from django.conf.urls.static import static
# seeting config 파일을 접근하기 위한
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/rooms/", include("rooms.urls")),
    path("api/v1/categories/", include("categories.urls")),
    path("api/v1/experiences/", include("experiences.urls")),
    path("api/v1/medias/", include("medias.urls")),
    path("api/v1/wishlists/", include("wishlists.urls")),
    path("api/v1/users/", include("users.urls")),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

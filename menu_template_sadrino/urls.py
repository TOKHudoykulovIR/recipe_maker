from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('menu/', include('menu.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "Administration Panel"
admin.site.site_url = "https://damp-taiga-59981.herokuapp.com/admin/"
# admin.site.site_title = ''
# admin.site.index_title = ""

from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    url('admin/', admin.site.urls),
    # path("api/", include('modules.api.urls'))
]

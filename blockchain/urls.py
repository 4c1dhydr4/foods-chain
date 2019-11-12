from django.contrib import admin
from django.urls import path
from views.dashboard import (index,tacks,)

urlpatterns = [
	path('', index, name="index"),
	path('tacks/', tacks, name="tacks"),
    path('admin/', admin.site.urls),
]

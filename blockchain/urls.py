from django.contrib import admin
from django.urls import path
from views.dashboard import (index,tacks,blockchain_card)

urlpatterns = [
	path('', index, name="index"),
	path('tacks/', tacks, name="tacks"),
	path('blockchain_card/', blockchain_card, name="blockchain_card"),
    path('admin/', admin.site.urls),
]

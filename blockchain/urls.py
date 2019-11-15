from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from views.dashboard import (index,tacks,blockchain_card, traceability)
from views.phone import (phone, cell_traceability,)

urlpatterns = [
	path('', login_required(index), name="index"),
	path('phone/', login_required(phone), name="phone"),
	path('cell_traceability/', login_required(cell_traceability), name="cell_traceability"),
	path('tacks/', login_required(tacks), name="tacks"),
	path('blockchain_card/', login_required(blockchain_card), name="blockchain_card"),
	path('traceability/', login_required(traceability), name="traceability"),
    path('admin/', admin.site.urls),
	path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]

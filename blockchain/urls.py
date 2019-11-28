from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from views.dashboard import (index,tacks,blockchain_card, traceability, case)
from views.phone import (phone, qr_track, client_select, company_login)

urlpatterns = [
	path('', login_required(index), name="index"),
	path('phone/', login_required(phone), name="phone"),
	path('client_select/', login_required(client_select), name="client_select"),
	path('company_login/', login_required(company_login), name="company_login"),
	path('qr_track/<int:opt>', login_required(qr_track), name="qr_track"),
	path('tacks/', login_required(tacks), name="tacks"),
	path('blockchain_card/', login_required(blockchain_card), name="blockchain_card"),
	path('traceability/', login_required(traceability), name="traceability"),
	path('case/', login_required(case), name="case"),
    path('admin/', admin.site.urls),
	path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('accounts/logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]


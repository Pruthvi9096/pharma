from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name="index"),
    path('signup/',views.signup,name='signup'),
	path('login/',views.loginView,name='login'),
	path('logout/',views.logout_view,name="logout"),
    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
    path('request/',views.requestForm,name="request"),
    path('search/',views.search,name="search"),
    path('request-detail/<int:pk>',views.requestDetails,name="request-detail"),
    path('request-done/<int:pk>',views.doneRequest,name="request-done"),
]
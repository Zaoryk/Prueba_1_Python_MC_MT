from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("devices/", views.device_list_view, name="device_list"),
    path("devices/<int:device_id>/", views.device_detail_view, name="device_detail"),
    path("devices/add/", views.add_device_view, name="add_device"),
    path("devices/add/category/", views.add_category_view, name="add_category"),
    path("devices/add/zone/", views.add_zone_view, name="add_zone"),
    path("devices/generate-sample/", views.generate_sample_data_view, name="generate_sample_data"),
    path("measurements/", views.measurement_list_view, name="measurement_list"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("password-reset/", views.password_reset_view, name="password_reset"),
]
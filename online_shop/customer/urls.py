from django.urls import path
from customer.views import contact, CustomerLoginView, Register, home
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordResetView

urlpatterns = [
    path('comment/', contact, name='contact'),
    path('login/', CustomerLoginView.as_view(), name='login'),
    path('register/', Register.as_view(), name="register"),
    path('home/', home, name="home"),
    path('password_reset/', PasswordResetView.as_view(), name="password_reset"),
    path('change_password/', PasswordChangeView.as_view(), name="change_password"),
    path('logout/', LogoutView.as_view(), name="logout"),

]

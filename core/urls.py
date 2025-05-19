from django.urls import path
from .views import HomeView
from .views import HomeView, ContactView
from .views import test_email_view

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('test-email/', test_email_view, name='test_email'),

]
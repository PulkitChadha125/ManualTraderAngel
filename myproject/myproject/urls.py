"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard_view, name='dashboard'),
    path('login/', views.api_login, name='api_login'),
    path('futidx-buy/', views.futidx_buy, name='futidx_buy'),
    path('futidx-sell/', views.futidx_sell, name='futidx_sell'),
    path('b-action/', views.b_action, name='b_action'),
    path('s-action/', views.s_action, name='s_action'),
    path('fetch-symbol-data/', views.fetch_symbol_data, name='fetch_symbol_data'),
]

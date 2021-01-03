"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns 
from django.utils.translation import gettext_lazy as _
import home
from home.views import about
from home import views
from user import views as UserViews


urlpatterns = [
    path(_('admin/'), admin.site.urls),
    path('', include('home.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('faq/', views.faq, name='faq'),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('user/', include('user.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('login/', UserViews.login_view, name='login_view'),
    path('logout/', UserViews.logout_view, name='logout_view'),
    path('signup/', UserViews.signup_view, name='signup_view'),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('currencies/', include('currencies.urls')),
    path('selectcurrency', views.selectcurrency, name='selectcurrency'),

    

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

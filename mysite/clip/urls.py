from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import HomePageView
from . import views


app_name = 'clip'
urlpatterns = [

    path('', views.category_crab, name='category_crab'),
    path('clip/<int:pk>/', views.detail, name='detail'),
    path('all/', HomePageView.as_view(), name='all'),
    path('spring/', views.category_spring, name='category_spring'),
    path('cart', views.cart, name='cart'),
    path('in_cart', views.in_cart, name='in_cart'),
    path('manage_cart', views.manage_cart, name='manage_cart'),
    path('order', views.order, name='order'),
    path('emty_order', views.emty_order, name='emty_order'),
    #re_path(r'^emty_order/(?:user-(?P<user_id>\d+)/)?$', emty_order),
    #path('emty_order/<int:user_id>/', views.emty_order,),
    # path('clip/<int:user_id>/', views.detail, name='example'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

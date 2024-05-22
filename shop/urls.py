from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('collections',views.collections, name="collections"),
    path('collections/<str:name>',views.homeview, name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_details, name="product_details"),
    path('register',views.register, name="register"),
    path('login',views.login_page, name="login"),
    path('logout',views.logout_page, name="logout"),
    path('addtocart',views.add_to_cart, name="addtocart"),
    path('remove_cart/<str:cid>',views.remove_cart, name="remove_cart"),
    path('remove_fav/<str:fid>',views.remove_fav, name="remove_fav"),
    path('cart',views.cart_page, name="cart"),
    path('fav',views.fav_page, name="fav"),
    path('favviewpage',views.favviewpage, name="favviewpage"),
    path('checkout',views.checkout, name="checkout"),
    path('payment',views.payment_page, name="payment"),
    path('about',views.about_page, name="about"),
    path('shipping',views.shipping_page, name="shipping"),
    path('privacy',views.privacy_page, name="privacy"),
    path('terms',views.terms_page, name="terms"),
    path('cardpayment',views.cardpayment, name="cardpayment"),
    path('confirm',views.confirm, name="confirm"),
]
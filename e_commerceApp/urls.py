from rest_framework import routers
from django.urls import include, path
from e_commerceApp.views import ProductViewSet, ClientViewSet

# get instance of the router defined in rest_framework
router = routers.DefaultRouter()
# add Product and client urls( get, post, put, delete) 
router.register(r'product', ProductViewSet, basename='product') 
router.register(r'client', ClientViewSet, basename='clent')
urlpatterns = [
    path('', include(router.urls))
]
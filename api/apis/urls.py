#URL conf
from django.urls import include, path

#routers
from rest_framework import routers

#* views
from .views import *


#router defining
router = routers.DefaultRouter()

#router path and viewset being used
router.register(r'suppliers', SuppliersViewSet)

#URL path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
from django.urls import path 

from rest_framework_simplejwt.views import TokenRefreshView

from auth_user.api.views import MyTokenObtainPairView


urlpatterns = [

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
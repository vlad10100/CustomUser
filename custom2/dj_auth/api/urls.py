from django.urls import path 
from dj_auth.api.views import Routes, MyTokenObtainPairView, NoteView

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView



urlpatterns = [
    path('', Routes.as_view(), name='get-routes'),
    path('notes/', NoteView.as_view()),

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   
    path('api/token/verify/', TokenVerifyView.as_view()), 
    
]

from django.urls import path, include

from contestant import views
from .views import (random_contestant_email, LastesContestantsList, ContestantRegisterView, ContestantLoginView, SetPasswordView, VerifyEmailView) 

urlpatterns = [
    path('lastest-contestans/', views.LastesContestantsList.as_view()),
    path('api/random-contestant-email/', random_contestant_email, name='random_contestant_email'),
    path('contestants/register/', ContestantRegisterView.as_view(), name='contestant-register'),
    path('login/', ContestantLoginView.as_view(), name='contestant-login'),
    path('set-password/', SetPasswordView.as_view(), name='set-password'),
    path('verify-email/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    ]
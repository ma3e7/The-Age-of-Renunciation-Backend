from django.urls import path
from . import views
from . import auth_views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('users/signup/', auth_views.signup),
    path('users/signin/', auth_views.signin),
    path('users/signout/', auth_views.signout),
    path('users/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/profile/', views.update_profile),

    path('codex/heroes/', views.all_heroes),
    path('codex/heroes/<int:id>/', views.single_hero),
    path('codex/abilities/<int:hero_id>/', views.hero_abilities),
]

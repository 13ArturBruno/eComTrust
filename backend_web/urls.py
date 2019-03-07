from rest_framework.routers import DefaultRouter
from backend_web.user import views as users_views

mobile_router = DefaultRouter()
mobile_router.register('users', users_views.UserViewSetRegister)






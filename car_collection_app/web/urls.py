from django.urls import path, include

from car_collection_app.web.views import index, catalogue, \
    create_car, edit_car, delete_car, details_car, \
    create_profile, edit_profile, delete_profile, details_profile

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
        path('details/', details_profile, name='details profile'),
    ])),
    path('car/', include([
        path('create/', create_car, name='create car'),
        path('<int:pk>/edit/', edit_car, name='edit car'),
        path('<int:pk>/delete/', delete_car, name='delete car'),
        path('<int:pk>/details/', details_car, name='details car'),
    ])),

)

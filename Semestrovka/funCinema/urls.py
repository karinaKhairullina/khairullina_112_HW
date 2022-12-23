from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('reg/', views.Reg.as_view(), name='reg'),
    path("serials_list/", views.SerialsView.as_view(), name='serials_list'),
    path("add/", views.AddView.as_view(), name='add'),
    path("single_serial/", views.SerialDetailView.as_view(), name='single_serial'),
    path("<slug:slug>/", views.SingleSerial.as_view(), name='detail_serial'),
    path("actor/<int:id>/", views.ActorView.as_view(), name='actor_detail'),
]


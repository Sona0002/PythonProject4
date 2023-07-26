
from django.urls import path, include
from . import views

app_name='mobileapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('mobile/<int:mobile_id>/',views.detail,name='detail'),
    path('add/',views.add_mobile,name='add_mobile'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]

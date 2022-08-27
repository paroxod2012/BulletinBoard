from django.urls import path
from .views import BoardList, AdCreate, AdUpdate, AdDelete, AdDetail, MyResponse
# add_response


urlpatterns = [
   path('', BoardList.as_view(),  name='board'),
   path('create/', AdCreate.as_view(), name='ad_create'),
   path('<int:pk>/update/', AdUpdate.as_view(), name='ad_edit'),
   path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
   path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
   path('<int:pk>', AdDetail.as_view(), name='ad_detail'),
   path('responses/', MyResponse.as_view(), name='responses'),
   # path('my_response/<int:pk>', add_response, name='my_response'),

]
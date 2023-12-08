from django.urls import include, path
from rest_framework.routers import SimpleRouter

from cats.views import cat_list, APICat, CatList, CatDetail, CatViewSet


router = SimpleRouter()
router.register('cats', CatViewSet)

urlpatterns = [
   # path('cats/', cat_list),
   # path('cats/', APICat.as_view()),
   # path('cats/', CatList.as_view()),
   # path('cats/<int:pk>/', CatDetail.as_view()),
   path('', include(router.urls))
]



from django.urls import path

from cats.views import cat_list, APICat, CatList, CatDetail


urlpatterns = [
   # path('cats/', cat_list),
   # path('cats/', APICat.as_view()),
   path('cats/', CatList.as_view()),
   path('cats/<int:pk>/', CatDetail.as_view()),
]



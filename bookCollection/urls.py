from django.urls import path,include
from .views import BookView,DetailsPost,BookBorrowView


urlpatterns = [
 path('book/',BookView.as_view(),name='book'),
 path('category/<slug:category_slug>/',BookView.as_view(), name='category_wise_post'),
 path('details/<int:id>/',DetailsPost.as_view(),name="details_view"),
 path('buy_car/<int:id>/',DetailsPost.as_view(),name='buyCar'),
 path('borrow_book/<int:id>/', BookBorrowView.as_view(), name='borrow_book'),
]
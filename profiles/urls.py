from django.urls import path 
from .views import BookListView,ReturnBookView
urlpatterns = [
    path('profile',BookListView.as_view(),name='profile'),
    path('return/<int:id>',ReturnBookView.as_view(),name='return')
]

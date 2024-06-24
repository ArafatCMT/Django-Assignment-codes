from django.urls import path
from library.views import BookDetailView, BookBorrowView

urlpatterns = [
   path('detail/<int:id>', BookDetailView.as_view(), name='book_details'),
   path('borrow/<int:id>', BookBorrowView, name='borrow_book'),
]
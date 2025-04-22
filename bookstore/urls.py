from django.urls import path
from django.conf import settings  # Import settings
from django.conf.urls.static import static
from .views import (
    RegisterView, LoginView, LogoutView, BookCreateView, BookUpdateView,
    BookDeleteView, BookInventoryView, BookListView, BookDetailView,
    CartView, AddToCartView, book_list, PaymentView, RemoveFromCartView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/books/', BookInventoryView.as_view(), name='book-inventory'),
    path('admin/books/add/', BookCreateView.as_view(), name='book-add'),
    path('admin/books/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    path('admin/books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:pk>/', AddToCartView.as_view(), name='add-to-cart'),
    path('books/', book_list, name='book-list-function'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('cart/remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
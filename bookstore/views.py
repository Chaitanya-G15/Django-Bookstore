from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('book-list')
        return render(request, 'login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

class BookCreateView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        return render(request, 'admin/book_form.html')

    def post(self, request):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            description=request.POST['description'],
            price=request.POST['price'],
            stock=request.POST['stock']
        )
        return redirect('book-inventory')

class BookUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        book = Book.objects.get(pk=pk)
        return render(request, 'admin/book_form.html', {'book': book})

    def post(self, request, pk):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        book = Book.objects.get(pk=pk)
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.description = request.POST['description']
        book.price = request.POST['price']
        book.stock = request.POST['stock']
        book.save()
        return redirect('book-inventory')

class BookDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        Book.objects.get(pk=pk).delete()
        return redirect('book-inventory')

class BookInventoryView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        books = Book.objects.all()
        return render(request, 'admin/inventory.html', {'books': books})

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'book_list.html', {'books': books})

class BookDetailView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, 'book_detail.html', {'book': book})


class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        total = sum(item['price'] * item['quantity'] for item in cart.values())
        return render(request, 'cart.html', {'cart': cart, 'total': total})

from decimal import Decimal
from django.shortcuts import get_object_or_404
from .models import Book

class AddToCartView(View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        cart = request.session.get('cart', {})

        book_id = str(book.id)
        if book_id in cart:
            cart[book_id]['quantity'] += 1
        else:
            cart[book_id] = {
                'title': book.title,
                'price': float(book.price),
                'quantity': 1
            }

        request.session['cart'] = cart
        return redirect('cart')


from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

from django.shortcuts import render, redirect

class PaymentView(View):
    def post(self, request):
        # Handle payment logic here (e.g., integrate with a payment gateway)
        # For now, clear the cart and redirect to a success page
        request.session['cart'] = {}
        return render(request, 'payment.html')

class RemoveFromCartView(View):
    def post(self, request, pk):
        cart = request.session.get('cart', {})
        book_id = str(pk)

        # Remove the book from the cart if it exists
        if book_id in cart:
            del cart[book_id]

        # Update the session
        request.session['cart'] = cart
        return redirect('cart')
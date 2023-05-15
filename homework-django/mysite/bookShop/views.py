from django.http import JsonResponse
from django.views import View

from bookShop.models import Book, Author, City, Customer, Sale

import json


class SearchView(View):
    def get(self, request):
        title = request.GET.get('title')
        author_name = request.GET.get('author_name')

        if not title and not author_name:
            return JsonResponse({'error': 'No search parameters provided'}, status=400)

        books = Book.objects.all()

        if title:
            books = books.filter(title__icontains=title)

        if author_name:
            books = books.filter(author__name__icontains=author_name)

        results = [{'title': book.title, 'author': book.author.name} for book in books]

        return JsonResponse({'results': results}, status=200)

class BooksView(View):
    def get(self, request):
        books = Book.objects.all()
        data = [{'title': book.title, 'author': book.author.name} for book in books]
        return JsonResponse(data, status=200, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        title = data.get('title')
        author_id = data.get('author_id')
        published_date = data.get('published_date')
        price = data.get('price')

        try:
            author = Author.objects.get(id=author_id)
            book = Book.objects.create(title=title, author=author, published_date=published_date, price=price)
            return JsonResponse({'ok': 'Book created', 'book_id': book.id}, status=200)
        except Author.DoesNotExist:
            return JsonResponse({'error': 'Author not found'}, status=404)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class BookInfoView(View):
    def get(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            data = {'title': book.title, 'author': book.author.name, 'published_date': book.published_date}
            return JsonResponse(data, status=200)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

    def put(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            data = json.loads(request.body)
            book.title = data.get('title', book.title)
            author_id = data.get('author_id')
            if author_id:
                try:
                    author = Author.objects.get(id=author_id)
                    book.author = author
                except Author.DoesNotExist:
                    return JsonResponse({'error': 'Author not found'}, status=404)

            book.save()
            return JsonResponse({'ok': 'Book updated'}, status=200)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

    def delete(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            book.delete()
            return JsonResponse({'ok': 'Book deleted'}, status=200)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class CustomersView(View):
    def get(self, request):
        customers = Customer.objects.all()
        data = [{'first_name': customer.first_name, 'last_name': customer.last_name} for customer in customers]
        return JsonResponse(data, status=200, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        address = data.get('address')
        city_id = data.get('city_id')

        try:
            city = City.objects.get(id=city_id)
            customer = Customer.objects.create(first_name=first_name, last_name=last_name, email=email,
                                               phone_number=phone_number, address=address, city=city)
            return JsonResponse({'ok': 'Customer created', 'customer_id': customer.id}, status=200)
        except City.DoesNotExist:
            return JsonResponse({'error': 'City not found'}, status=404)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class CustomerInfoView(View):
    def get(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            data = {
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'email': customer.email,
                'phone_number': customer.phone_number,
                'address': customer.address,
                'city': customer.city.name
            }
            return JsonResponse(data, status=200, safe=False)
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)

    def put(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            data = json.loads(request.body)
            customer.first_name = data.get('first_name', customer.first_name)
            customer.last_name = data.get('last_name', customer.last_name)
            customer.email = data.get('email', customer.email)
            customer.phone_number = data.get('phone_number', customer.phone_number)
            customer.address = data.get('address', customer.address)
            city_id = data.get('city_id')
            if city_id:
                try:
                    city = City.objects.get(id=city_id)
                    customer.city = city
                except City.DoesNotExist:
                    return JsonResponse({'error': 'City not found'}, status=404)

            customer.save()
            return JsonResponse({'ok': 'Customer updated'}, status=200)
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)

    def delete(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            customer.delete()
            return JsonResponse({'ok': 'Customer deleted'}, status=200)
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=404)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class SalesView(View):
    def get(self, request):
        sales = Sale.objects.all()
        data = [{'customer': sale.customer.first_name, 'book': sale.book.title, 'sale_date': sale.sale_date} for sale in
                sales]
        return JsonResponse(data, status=200, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        customer_id = data.get('customer_id')
        book_id = data.get('book_id')

        try:
            customer = Customer.objects.get(id=customer_id)
            book = Book.objects.get(id=book_id)
            sale = Sale.objects.create(customer=customer, book=book)
            return JsonResponse({'ok': 'Sale created', 'sale_id': sale.id}, status=200)
        except (Customer.DoesNotExist, Book.DoesNotExist):
            return JsonResponse({'error': 'Customer or Book not found'}, status=404)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class SaleInfoView(View):
    def get(self, request, sale_id):
        try:
            sale = Sale.objects.get(id=sale_id)
            data = {
                'book': sale.book.title,
                'customer': f"{sale.customer.first_name} {sale.customer.last_name}",
                'sale_date': sale.sale_date
            }
            return JsonResponse(data, status=200, safe=False)
        except Sale.DoesNotExist:
            return JsonResponse({'error': 'Sale not found'}, status=404)

    def put(self, request, sale_id):
        try:
            sale = Sale.objects.get(id=sale_id)
            data = json.loads(request.body)
            book_id = data.get('book_id')
            customer_id = data.get('customer_id')

            if book_id:
                try:
                    book = Book.objects.get(id=book_id)
                    sale.book = book
                except Book.DoesNotExist:
                    return JsonResponse({'error': 'Book not found'}, status=404)

            if customer_id:
                try:
                    customer = Customer.objects.get(id=customer_id)
                    sale.customer = customer
                except Customer.DoesNotExist:
                    return JsonResponse({'error': 'Customer not found'}, status=404)

            sale.save()
            return JsonResponse({'ok': 'Sale updated'}, status=200)
        except Sale.DoesNotExist:
            return JsonResponse({'error': 'Sale not found'}, status=404)

    def delete(self, request, sale_id):
        try:
            sale = Sale.objects.get(id=sale_id)
            sale.delete()
            return JsonResponse({'ok': 'Sale deleted'}, status=200)
        except Sale.DoesNotExist:
            return JsonResponse({'error': 'Sale not found'}, status=404)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)

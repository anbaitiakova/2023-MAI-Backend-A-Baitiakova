from django.http import JsonResponse
from django.views import View


class BooksView(View):
    def get(self, request):
        return JsonResponse({'ok': 'get books stub'}, status=200)

    def post(self, request):
        return JsonResponse({'ok': 'put books stub'}, status=200)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class BookInfoView(View):
    def get(self, request, book_id):
        return JsonResponse({'ok': 'get book with id {} stub'.format(book_id)}, status=200)

    def put(self, request, book_id):
        return JsonResponse({'ok': 'put book with id {} stub'.format(book_id)}, status=200)

    def delete(self, request, book_id):
        return JsonResponse({'ok': 'delete book with id {} stub'.format(book_id)}, status=200)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class CustomersView(View):
    def get(self, request):
        return JsonResponse({'ok': 'get customer stub'}, status=200)

    def post(self, request):
        return JsonResponse({'ok': 'put customer stub'}, status=200)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class CustomerInfoView(View):
    def get(self, request, customer_id):
        return JsonResponse({'ok': 'get customer with id {} stub'.format(customer_id)}, status=200)

    def put(self, request, customer_id):
        return JsonResponse({'ok': 'put customer with id {} stub'.format(customer_id)}, status=200)

    def delete(self, request, customer_id):
        return JsonResponse({'ok': 'delete customer with id {} stub'.format(customer_id)}, status=200)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)

class SalesView(View):
    def get(self, request, customer_id):
        return JsonResponse({'ok': 'get sale with id {} stub'.format(customer_id)}, status=200)

    def put(self, request, customer_id):
        return JsonResponse({'ok': 'put sale with id {} stub'.format(customer_id)}, status=200)

    def delete(self, request, customer_id):
        return JsonResponse({'ok': 'delete sale with id {} stub'.format(customer_id)}, status=200)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)


class SaleInfoView(View):
    def get(self, request, customer_id):
        return JsonResponse({'ok': 'get sale with id {} stub'.format(customer_id)}, status=200)

    def put(self, request, customer_id):
        return JsonResponse({'ok': 'put sale with id {} stub'.format(customer_id)}, status=200)

    def delete(self, request, customer_id):
        return JsonResponse({'ok': 'delete sale with id {} stub'.format(customer_id)}, status=200)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Invalid request method'}, status=405)
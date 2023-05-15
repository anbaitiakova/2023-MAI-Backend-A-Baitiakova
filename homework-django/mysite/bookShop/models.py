from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = 'city'

    def __str__(self):
        return f"{self.name}, {self.country}"


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.title


class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sale_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'sale'

    def __str__(self):
        return f"{self.customer} bought {self.book} on {self.sale_date}"

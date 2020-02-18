from django.db import models
import decimal


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(db_column='ctyID', primary_key=True)
    productname = models.CharField('Product Name', max_length=200)
    #barcode = models.CharField('Barcode', max_length=1000, )
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    sale_price = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=100, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    picture = models.ImageField('Product Picture', upload_to='products/%Y/%m/%d', default='')

    def __str__(self):
        return self.productname

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'


# def customer_photo_directory(instance, filename):
#     return 'customers/{0}_{1}'.format(instance.identity, instance.name)
#
#
# class Customer(models.Model):
#     identity = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     balance = models.DecimalField(max_digits=6, decimal_places=2)
#     photo = models.ImageField(upload_to=customer_photo_directory, null=True)
#
#     def __str__(self):
#         return '{0} ({1})'.format(self.identity, self.name)


class Order(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Sale {0}'.format(self.id)

    class Meta:
        verbose_name_plural = 'Sales'
        verbose_name = 'Sales'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product.productname) + " - " + str(self.product.price)

    class Meta:
        verbose_name_plural = 'Sold Products'
        verbose_name = 'Sold Product'


class StoreDetails(models.Model):
    store_name = models.CharField('Store Name', max_length=200)
    store_logo = models.ImageField('Store Logo', upload_to='logo/%Y/%m/%d', default='')

    class Meta:
        verbose_name = 'Store Details'
        verbose_name_plural = 'Store Details'

    def __str__(self):
        return self.store_name


PAYMENT_STATUS = (
    ('Fully paid', 'Fully paid'),
    ('Got balnce', 'Got balance'),
    ('Not paid', 'Not paid'),
)


class Creditor(models.Model):
    customer_name = models.CharField('Customer name', max_length=200, )
    item_description = models.TextField('Item Description', max_length=500)
    amount = models.DecimalField('Total Price', max_digits=20, decimal_places=2, )
    addamount = models.DecimalField('Add New Item Price', default=0, max_digits=20, decimal_places=2, )
    quantity = models.DecimalField('Quantity', max_digits=20, decimal_places=2, )
    payment_status = models.CharField('Payment Status', max_length=200, default='Not paid', choices=PAYMENT_STATUS)
    amount_paid = models.DecimalField('Amount Paid', max_digits=20, decimal_places=2, default=0)
    balance = models.DecimalField('Balance', max_digits=20, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True)

    # def save(self, **kwargs):
    #
    #     if not self.id:
    #         amountEntered = decimal.Decimal(self.amount_paid)
    #         self.balance = self.amount - amountEntered
    #         self.amount_paid = amountEntered
    #
    #         if self.balance < 1:
    #             self.payment_status = 'Fully paid'
    #
    #         super(Creditor, self).save()

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name_plural = 'Ba Nkongole'
        verbose_name = 'Ba Nkongole'

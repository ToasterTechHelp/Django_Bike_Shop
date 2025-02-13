from django.db import models

STATUS_CHOICES = [
    ('P', 'Pending'),
    ('R', 'Ready')
]


class Frame(models.Model):
    color = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color


class Seat(models.Model):
    color = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color


class Tire(models.Model):
    type = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.type


class Basket(models.Model):
    quantity = models.IntegerField()


class Bike(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    has_basket = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    status = models.CharField(max_length=1, default="", choices=STATUS_CHOICES)
    def bike_name(self):
        return self.bike.name
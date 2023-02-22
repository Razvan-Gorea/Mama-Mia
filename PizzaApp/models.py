from django.db import models

class Details(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=16)
    date = models.CharField(max_length=5)
    card_cvv = models.CharField(max_length=3)
    address = models.CharField(max_length=200)
    pizza_details = models.ForeignKey('Pizza', models.DO_NOTHING, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Size(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.size

class Toppings(models.Model):
    id = models.AutoField(primary_key=True)
    toppings = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.toppings

class Crust(models.Model):
    id = models.AutoField(primary_key=True)
    crust = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.crust

class Sauces(models.Model):
    id = models.AutoField(primary_key=True)
    sauces = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.sauces

class Cheese(models.Model):
    id = models.AutoField(primary_key=True)
    cheese = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.cheese

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.ForeignKey(Size, blank=True, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Toppings, blank=True)
    crust = models.ForeignKey(Crust, blank=True, on_delete=models.CASCADE)
    sauces = models.ForeignKey(Sauces, blank=True, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.size) + " " +  str(self.toppings) + " " + str(self.crust) + " " + str(self.sauces) + " " + str(self.cheese)
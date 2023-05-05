from django.db import models
import uuid

class Section(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    section_name = models.CharField(max_length=15)

    def __str__(self):
        return self.section_name

class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    category_name = models.CharField(max_length=50, unique=True)
    category_image = models.ImageField(upload_to='category/')
    bar_food = models.BooleanField(default=False)
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

class Meal(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    meal_name = models.CharField(max_length=70)
    meal_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    meal_image1 = models.ImageField(upload_to='meal_images/')
    meal_image2 = models.ImageField(upload_to='meal_images/',blank=True, null=True)
    meal_image3 = models.ImageField(upload_to='meal_images/',blank=True, null=True)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    is_hot = models.BooleanField(default=False)

    def __str__(self):
        return self.meal_name


class Cart(models.Model):
    cart_id = models.CharField(max_length=50, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.meal

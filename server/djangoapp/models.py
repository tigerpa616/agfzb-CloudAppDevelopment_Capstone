from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model

class CarMake(models.Model):

    # Fields
    carmake_id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True, blank=False)
    Description = models.TextField(max_length=100)

    def __str__(self):
        return str(self.name)

 



# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    YEAR_CHOICES = []
    for r in range((now().year), 1979, -1):
        YEAR_CHOICES.append((r, r))

    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    TYPE_CHOICES = [
        (SEDAN, 'sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]
    carmodel_id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(null=False)
    year = models.IntegerField(choices=YEAR_CHOICES, default=now().year)
    type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default=SEDAN
    )

    def __str__(self):
        return self.carmake.name + " " + self.name
# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data

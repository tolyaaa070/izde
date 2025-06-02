from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    def __str__(self):
        return f'{self.email}'
class Agent(UserProfile):
    position = models.CharField(max_length=60, default='agent')
    image = models.ImageField(upload_to='agent_image/')
    LANGUAGE_CHOICES =(
        ('english','english'),
        ('russian','russian'),
        ('kyrgyz','kyrgyz'),
        ('china','china'),
        ('french','french')
    )
    language =MultiSelectField(choices=LANGUAGE_CHOICES,max_choices=5)
    company = models.ImageField(upload_to='company_image/')
    areas = models.CharField(max_length=70,verbose_name='где в основном')
    active_listing = models.IntegerField()
    experience = models.DateField()
    phone_number = PhoneNumberField(null=True,blank=True)



    def __str__(self):
        return f'{self.position},{self.image},{self.language}'


class Houses(models.Model):
    TYPE_CHOICES=(
        ('buy','buy'),
        ('rent','rent')
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    name_houses = models.CharField(max_length=70)
    SERIES_CHOICES=(
        ('individual','individual'),
        ('elite','elite'),
        ('104','104'),
        ('105','105'),
        ('106','106')
    )
    series = models.CharField(choices=SERIES_CHOICES, max_length=10)
    ROOM_CHOICES = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6+','6+')
    )
    rooms = models.CharField(choices=ROOM_CHOICES,max_length=7)
    BATHROOMS_CHOICES =(
        ('combined','combined'),
        ('separate','separate')
    )

    bathroom = models.CharField(choices=BATHROOMS_CHOICES,max_length=15)
    bathroom_icon = models.FileField(upload_to='bathroom_icon/')
    PARKING_CHOICES = (
        ('ground','ground'),
        ('underground','underground'),
        ('no parking','no parking')
    )
    parking= models.CharField(choices=PARKING_CHOICES,max_length=20)
    parking_icon = models.FileField(upload_to='parking_icon/')
    locations = models.CharField(max_length=35)
    square = models.IntegerField()
    price = models.PositiveIntegerField()
    about_property = models.TextField(max_length=100)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE,related_name='agent')
    min_stay = models.PositiveSmallIntegerField(verbose_name="Минимальный срок аренды (в месяцах)",null=True,blank=True)
    deposit = models.PositiveIntegerField(null=True,blank=True)
    floor = models.PositiveIntegerField()
    total_floors = models.PositiveIntegerField()
    floor_icon = models.FileField(upload_to='floor_icon/')


    def __str__(self):
        return f'{self.name_houses}'


    def get_avg_rating(self):
        ratting=self.houses_rating.all()
        if ratting.exists():
            return round(sum([i.rating for i in ratting]) / ratting.count(),1)
        return 0
    def get_count_reviews(self):
        return self.houses_rating.count()

class Amenity(models.Model):
    AMENITIES_CHOICES = (
        ('Balkony', 'Balkony'),
        ('Microwave', 'Microwave'),
        ('WiFi', 'WiFi'),
        ('Coverad parking', 'Coverad parking'),
        ('TV', 'TV'),
        ('Central heating', 'Central heating'),
        ('Washing machine', 'Washing machine'),
        ('Air-conditioner', 'Air-conditioner'),
        ('Tableware', 'Tableware'),
        ('Swimming pool', 'Swimming pool'),
        ('Gym', 'Gym')
    )
    amenities = MultiSelectField(choices=AMENITIES_CHOICES,max_choices=12,null=True,blank=True)
    amenity_houses = models.ForeignKey(Houses,on_delete=models.CASCADE,related_name='amenity')
    amenities_icon = models.FileField(upload_to='amenities_icon/')

    def __str__(self):
        return f'{self.amenities}'


class HousePhotos(models.Model):
    image = models.ImageField(upload_to='houses_image/')
    house = models.ForeignKey(Houses,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.house}'

class Rating(models.Model):
    houses = models.ForeignKey(Houses, on_delete=models.CASCADE,related_name='houses_rating')
    rating = models.IntegerField(choices=[(i, str(i))for i in range(1, 6)])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.houses},{self.rating}'

class Main(models.Model):
    houses = models.ManyToManyField(Houses)
    agents = models.ManyToManyField(Agent)

    def __str__(self):
        return f'{self.houses},{self.agents}'

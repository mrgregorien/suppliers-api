from django.db import models
# Create your models here.
EST = 'EST'
PST = 'PST'
MST = 'MST'
CST = 'CST'

TIMEZONE_CHOICES = [
    (EST, 'Eastern Standard Time'),
    (PST,'Pacific Standard Time'),
    (MST, 'Mountain Standard Time'),
    (CST, 'Central Standard Time')
]

MAN = 'Manufacturer'
DIS = 'Distributor'
WHO = 'Wholesaler'

SUPPLIER_TYPE = [
    (DIS,'Distributor'),
    (MAN, 'Manufacturer'),
    (WHO, 'Wholesaler')


]



DEPARTMENT_CATEGORIES = [
    ('Appliances','Appliances'),
    ('Apps & Games','Apps & Games'),
    ('Arts Crafts & Sewing','Arts Crafts & Sewing'),
    ('Automotive Parts & Accessories','Automotive Parts & Accessories'),
    ('Baby','Baby'),
    ('Beauty & Personal Care','Beauty & Personal Care'),
    ('Books','Books'),
    ('CDs & Vinyl','CDs & Vinyl'),
    ('Cell Phones & Accessories','Cell Phones & Accessories'),
    ('Clothing Shoes & Jewelry','Clothing Shoes & Jewelry'),
    ('Collectibles & Fine Art',	'Collectibles & Fine Art'),
    ('Computers','Computers'),
    ('Credit and Payment Cards','Credit and Payment Cards'),
    ('Digital Educational Resources','Digital Educational Resources'),
    ('Digital Music','Digital Music'),
    ('Electronics','Electronics'),
    ('Garden & Outdoor','Garden & Outdoor'),
    ('Gift Cards','Gift Cards'),
    ('Grocery & Gourmet Food','Grocery & Gourmet Food'),
    ('Handmade','Handmade'),
    ('Health Household & Baby Care','Health Household & Baby Care'),
    ('Home & Business Services','Home & Business Services'),
    ('Home & Kitchen','Home & Kitchen'),
    ('Industrial & Scientific','Industrial & Scientific'),
    ('Luggage & Travel Gear','Luggage & Travel Gear'),
    ('Luxury Stores','Luxury Stores'),
    ('Magazine Subscriptions','Magazine Subscriptions'),
    ('Movies & TV','Movies & TV'),
    ('Musical Instruments','Musical Instruments'),
    ('Office Products','Office Products'),
    ('Online Learning','Online Learning'),
    ('Pet Supplies','Pet Supplies'),
    ('Premium Beauty','Premium Beauty'),
    ('Smart Home','Smart Home'),
    ('Software','Software'),
    ('Sports & Outdoors','Sports & Outdoors'),
    ('Subscription Boxes','Subscription Boxes'),
    ('Tools & Home Improvement','Tools & Home Improvement'),
    ('Toys & Games','Toys & Games'),
]
class SuppliersModels(models.Model):
    CompanyName = models.CharField(max_length=50,default='')
    ContactName = models.CharField(max_length=24,default='')
    ContactTitle = models.CharField(max_length=15, default='')
    Category = models.CharField(max_length=80, default='Category', choices=DEPARTMENT_CATEGORIES)
    Address = models.CharField(max_length=42, default='')
    City = models.CharField(max_length=18,default='')
    PostalCode = models.IntegerField(max_length=6, default='12041')
    Type = models.CharField(max_length=12, choices=SUPPLIER_TYPE, default=DIS)
    Website = models.URLField(max_length=250, default='')
    Phone = models.IntegerField(max_length= 8 , default='123')
    Email = models.EmailField(max_length=30, default='')
    TimeZone = models.CharField(max_length=50, choices=TIMEZONE_CHOICES, default=EST)


    


    #category view spreadsheet scraped data
    
    def __str__(self):
        return self.CompanyName


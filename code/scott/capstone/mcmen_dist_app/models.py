from django.db import models

class Driver(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    nick_name = models.CharField(max_length=20)
    phone_num = models.IntegerField()
    schedule = models.CharField(max_length=40)

    def __str__(self):
        return self.nick_name
    
    class Meta:
        ordering = ('nick_name',)

class Property(models.Model):
    code = models.CharField(max_length=10)
    latX = models.FloatField(max_length=20)
    lngX = models.FloatField(max_length=20)
    name = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=20,null=True, blank=True)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=15)
    manager = models.CharField(max_length=30)
    brewer = models.CharField(max_length=30)
    delivery = models.CharField(max_length=30)
    notes = models.TextField(max_length=300)
    images = models.ImageField

    def __str__(self):
        return self.code
    
    class Meta:
        ordering = ('name',)

class Route(models.Model):
    truck_num = models.CharField(max_length=10)
    driver = models.ManyToManyField(Driver)
    day = models.CharField(max_length=10)
    properties = models.ManyToManyField(Property)
    mech_record = models.TextField(max_length=300)

    def __str__(self):
        return self.truck_num

    class Meta:
        ordering = ('truck_num',)

class Article(models.Model):
    author = models.ForeignKey(Driver, on_delete=models.CASCADE) ##if we delete an Author, all articles associated with that author will get deleted. 
    title = models.CharField(max_length = 20)
    text = models.TextField(max_length = 500)
    pub_date = models.DateField()

    def __str__(self):
        return self.title
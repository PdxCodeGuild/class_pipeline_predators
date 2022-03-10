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
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)
    name = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=20,null=True, blank=True)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=15)
    manager = models.CharField(max_length=30)
    brewer = models.CharField(max_length=30)
    delivery = models.CharField(max_length=30)
    notes = models.TextField(max_length=500)
    images = models.ImageField(upload_to='images/', default='default.jpg')

    def __str__(self):
        return self.code
    
    class Meta:
        ordering = ('name',)

class Route(models.Model):
    truck_num = models.CharField(max_length=10)
    day = models.CharField(max_length=10)
    drivers = models.ManyToManyField(Driver)
    properties = models.ManyToManyField(Property)

    def __str__(self):
        return self.truck_num + ', ' + self.day

    class Meta:
        ordering = ('truck_num',)

class Article(models.Model):
    author = models.ForeignKey(Driver, on_delete=models.CASCADE)
    title = models.CharField(max_length = 20)
    text = models.TextField(max_length = 300)
    pub_date = models.DateField()

    def __str__(self):
        return self.title

class PostComment(models.Model):
    post_connected = models.ForeignKey(
        Article, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(Driver, on_delete=models.CASCADE)
    content = models.TextField(max_length = 300)
    date_posted = models.DateField()
    com_counter = models.CharField(max_length = 100, default = 0)

    def __str__(self):
        return str(self.author) + ', ' + self.post_connected.title[:40]

class Images(models.Model):
    picture = models.ImageField(upload_to='images/', default='default.jpg')

    class Meta:
        ordering = ('picture',)
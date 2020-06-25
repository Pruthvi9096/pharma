from django.db import models
from django.contrib.auth.models import User

class Pharmacy(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    contact = models.CharField(max_length=20, null=False)
    delivery = models.CharField(max_length=50,choices=[('available','Available'),
        ('not_available','Not Available')],null=True,default='available')
    deliver_charges = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True,default=0.00)

    def __str__(self):
        return self.name

    @property
    def show_address(self):
        return "{}\n{} {}\n{}".format(self.address,self.city,self.state,self.zipcode)


class DrugRequest(models.Model):

    name = models.CharField(max_length=250,null=True,blank=True)
    first_name = models.CharField(max_length=250,null=True)
    last_name = models.CharField(max_length=250,null=True)
    dob = models.DateField(verbose_name='Date Of Birth',null=True)
    phone = models.CharField(max_length=250,null=True)
    email = models.EmailField(null=True)
    note = models.TextField(max_length=1000,null=True,blank=True)
    address = models.TextField(max_length=1000)
    zip = models.CharField(max_length=250,null=True)
    city = models.CharField(max_length=250,null=True)
    state = models.CharField(max_length=250,null=True)
    pharmacy = models.ForeignKey(Pharmacy,on_delete=models.SET_NULL,null=True,related_name="pharmacy",blank=True)
    ip_address = models.CharField(max_length=250,null=True,verbose_name="IP Address",blank=True)
    pd_date = models.DateTimeField(verbose_name='Pickup Date',null=True)
    pd_time = models.CharField(max_length=25,null=True,blank=True)
    type = models.CharField(max_length=100,choices=[('delivery', 'Delivery'), ('pickup', 'Pickup')],default='pickup')
    status = models.CharField(max_length=100,choices=[('pending','Pending'),('done','Pick Done')],default="pending")
    done_date = models.DateTimeField(verbose_name='Pick Done Date',null=True,blank=True)
    images = models.FileField(upload_to='image/',null=True,blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)

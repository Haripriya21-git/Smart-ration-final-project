from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class Shopkeeper(models.Model):
    rationshop_no=models.CharField(max_length=50)
    shopkeeper_name=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    pincode=models.IntegerField()
    thaluk=models.CharField(max_length=50)
    ward_no=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    photo=models.CharField(max_length=500)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Cardholder(models.Model):
    cardholder_name=models.CharField(max_length=50)
    rationcard_no=models.IntegerField()
    card_type=models.CharField(max_length=50)
    # card_color=models.CharField(max_length=50,default="")
    post=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    members_no=models.IntegerField()
    members_name=models.CharField(max_length=50)
    house_no=models.CharField(max_length=50)
    ward_no=models.IntegerField()
    occupation=models.CharField(max_length=50)
    spouse_name=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    email_id=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    photo=models.CharField(max_length=500)
    status=models.CharField(max_length=100,default='pending')


class Stockdetails(models.Model):
    date=models.DateField()
    item_name=models.CharField(max_length=50)
    quantity=models.CharField(max_length=50)
    price=models.CharField(max_length=50)



class Subsidydetails(models.Model):
    date=models.DateField()
    card_color=models.CharField(max_length=50)
    beneficiaries=models.CharField(max_length=50)
    commodities=models.ForeignKey(Stockdetails,on_delete=models.CASCADE)
    quantitytype=models.CharField(max_length=50)
    quantity=models.FloatField()
    price=models.CharField(max_length=50)


class Token(models.Model):
    token_no=models.IntegerField()
    date=models.DateField()
    from_time=models.TimeField()
    to_time = models.TimeField()
    SHOPKEEPER = models.ForeignKey(Shopkeeper, on_delete=models.CASCADE)


class Token_request(models.Model):
    date=models.DateField()
    time=models.TimeField()
    CARDHOLDER = models.ForeignKey(Cardholder, on_delete=models.CASCADE)
    TOKEN = models.ForeignKey(Token, on_delete=models.CASCADE)


class complaint(models.Model):
    date=models.DateField()
    CARDHOLDER = models.ForeignKey(Cardholder, on_delete=models.CASCADE)
    complaint=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    reply=models.CharField(max_length=50)

class updatestock(models.Model):
    date=models.DateField()
    status=models.CharField(max_length=50)
    stock=models.CharField(max_length=50)
    quantity=models.CharField(max_length=50)
    SHOPKEEPER = models.ForeignKey(Shopkeeper, on_delete=models.CASCADE)
    STOCK = models.ForeignKey(Stockdetails, on_delete=models.CASCADE)


class Booking(models.Model):
    date=models.DateField()
    SOPKEEPER = models.ForeignKey(Shopkeeper, on_delete=models.CASCADE)
    CARDHOLDER = models.ForeignKey(Cardholder, on_delete=models.CASCADE)
    status=models.CharField(max_length=50)
    total_price=models.CharField(max_length=50)



class Bookingsub(models.Model):
    BOOKING = models.ForeignKey(Booking, on_delete=models.CASCADE)
    UPDATESTOCK = models.ForeignKey(updatestock, on_delete=models.CASCADE)
    quantity=models.CharField(max_length=100,default="")

class Payment(models.Model):
    date=models.DateField()
    CARDHOLDER = models.ForeignKey(Cardholder, on_delete=models.CASCADE)
    BOOKING = models.ForeignKey(Booking, on_delete=models.CASCADE)
    total_price=models.CharField(max_length=50)
    status=models.CharField(max_length=50)


class cart(models.Model):
    date=models.DateField()
    CARDHOLDER=models.ForeignKey(Cardholder,on_delete=models.CASCADE)
    # STOCK=models.ForeignKey(Stockdetails,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=50)
    UPDATESTOCK = models.ForeignKey(updatestock, on_delete=models.CASCADE)




class requeststock(models.Model):
    date=models.DateField()
    SHOPKEEPER=models.ForeignKey(Shopkeeper,on_delete=models.CASCADE)
    STOCKDETAILS=models.ForeignKey(Stockdetails,on_delete=models.CASCADE)
    status=models.CharField(max_length=50)
    quantity=models.CharField(max_length=40)



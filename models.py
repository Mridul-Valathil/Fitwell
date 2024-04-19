from django.db import models

# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)


class Trainer(models.Model):
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)


class User(models.Model):
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    gender = models.CharField(default=1, max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    # latitude = models.CharField(max_length=100)
    # longitude = models.CharField(max_length=100)


class Batch(models.Model):
    Batchname = models.CharField(max_length=100,default=1)
    Fromtime = models.CharField(max_length=100)
    Totime = models.CharField(max_length=100)


class Shops(models.Model):
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    shopname = models.CharField(default=1,max_length=100)
    email = models.CharField(default=1,max_length=100)
    password = models.CharField(default=1,max_length=100)
    contactno = models.CharField(default=1,max_length=100)
    place = models.CharField(default=1,max_length=100)
    post = models.CharField(default=1,max_length=100)
    pin = models.CharField(default=1,max_length=100)
    latitude = models.CharField(default=1,max_length=100)
    longitude = models.CharField(default=1,max_length=100)
    openingtime = models.CharField(default=1,max_length=100)
    closingtime = models.CharField(default=1,max_length=100)


class Requestt(models.Model):
    BATCH = models.ForeignKey(Batch, default=1, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    requeststatus = models.CharField(max_length=100,default=1)


class Allocate(models.Model):
    TRAINER = models.ForeignKey(Trainer, default=1, on_delete=models.CASCADE)
    BATCH = models.ForeignKey(Batch, default=1, on_delete=models.CASCADE)
    REQUEST = models.ForeignKey(Requestt, default=1, on_delete=models.CASCADE)
    Time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)


class Feedback(models.Model):
    TRAINER = models.ForeignKey(Trainer, default=1, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    Time = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    feedback = models.CharField(max_length=100)


class Rating(models.Model):
    TRAINER = models.ForeignKey(Trainer, default=1, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    rating = models.CharField(max_length=100)
    date = models.CharField(max_length=100)


class Complaint(models.Model):
    # TRAINER = models.ForeignKey(Trainer, default=1, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    complaints = models.CharField(max_length=100)
    complaintdate = models.CharField(max_length=100)
    reply = models.CharField(max_length=100,default='pending')
    replydate = models.CharField(max_length=100,default='0000-00-00')


class Questinare(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    questions = models.CharField(max_length=100)
    answers = models.CharField(max_length=100)


class Diet(models.Model):
    TRAINER = models.ForeignKey(Trainer, default=1, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    breakfast = models.CharField(max_length=100,default=1)
    lunch = models.CharField(max_length=100,default=1)
    dinner = models.CharField(max_length=100,default=1)

# class Fooditem(models.Model):
#     type = models.CharField(max_length=100)
#     foodname = models.CharField(max_length=100)
#     details = models.CharField(max_length=100)
#     image = models.CharField(max_length=100)

# class Category(models.Model):
#     categoryname = models.CharField(max_length=100)
#
# class Dietrequest(models.Model):
#     USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)



class Tips(models.Model):
    TRAINER = models.ForeignKey(Trainer, default=1, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    tips = models.CharField(max_length=1000)


class Workout(models.Model):
    TRAINER = models.ForeignKey(Trainer, default=1, on_delete=models.CASCADE)
    workoutname = models.CharField(max_length=100,default=1)
    category = models.CharField(max_length=100,default=1)
    duration = models.CharField(max_length=100,default=1)
    exercise = models.CharField(max_length=100,default=1)
    sets = models.CharField(max_length=100,default=1)
    reps = models.CharField(max_length=100,default=1)
    resttime = models.CharField(max_length=100,default=1)


class Chat(models.Model):
    TRAINER = models.ForeignKey(Trainer, default=1, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    chat = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    # time = models.CharField(max_length=100)


class Health(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    alergies = models.CharField(max_length=100)
    medicalhistory = models.CharField(max_length=100)


class Product(models.Model):
    SHOP = models.ForeignKey(Shops, default=1, on_delete=models.CASCADE)
    itemname = models.CharField(max_length=100)
    itemdescription = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.CharField(max_length=100)


class Cart(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    PRODUCT = models.ForeignKey(Product, default=1, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)


class Payment(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    paymenttype = models.CharField(max_length=100)
    paymentdate = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)


class Order(models.Model):
    USER = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    SHOP = models.ForeignKey(Shops, default=1, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    paymentdate = models.CharField(max_length=100)
    paymentstatus = models.CharField(max_length=100)


class Ordersub(models.Model):
    ORDER = models.ForeignKey(Order, default=1, on_delete=models.CASCADE)
    PRODUCT = models.ForeignKey(Product, default=1, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
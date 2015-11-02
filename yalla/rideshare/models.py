from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class User(models.Model):
    first_name = models.CharField(max_length=100) #Validates
    last_name = models.CharField(max_length=100)
    email = models.EmailField() #validates
    phone = models.CharField(max_length = 20)
    image = models.FilePathField() # make default image
    bio = models.TextField()
    password = models.CharField(max_length=30) #validates
    routes = #one to many
    messages =   # one to many
    rating = #one to many
    settings = models.OneToOneField(Settings) #one to one

class Settings(models.Model):
    user = models.OneToOneField(User)
    text_notification = models.BooleanField()
    email_notification = models.BooleanField()
    show_email = models.BooleanField()
    show_phone = models.BooleanField()
    show_firstname = models.BooleanField()
    show_lastname = models.BooleanField()

class Rating(models.Model):
    for_user_id = models.IntegerField() #validates, from a  Model
    review_star = models.IntegerField() #validates
    review_bio = models.TextField()
    from_user_id = models.IntegerField() #validates, from a Model

class Routes(models.Model):
    start = models.CharField(max_length=50) #validates
    end = models.CharField(max_length=50) #validates
    user = #one to many with models
    map_start = models.CharField(max_length= 20) #validates
    map_end = models.CharField(max_length=20) #validates
    payment = models.CharField() #turn it into choices, validates
    route_bio = models.TextField()
    date = models.DateTimeField() #make sure the model is right, it validates
    start_time = models.DateTimeField() #validates
    end_time = models.DateTimeField() #validates
    stop_model = # a one to many model

class Stop(models.Model):
    route_id = #model it is from
    stop_eng = models.CharField(max_length=30) #the name of the stop, validates
    stop_map = models.CharField(max_length= 50) # the stop x,y, validates
    stop_time = models.DateTimeField() #check the model

class Messages(models.Model):
    user_to = #the user message being sent too
    user_from = #the user message from
    message_bio = models.CharField(max_length=500) #validates
    route = #route model that the person might be messaging about,validates
    date = models.DateTimeField() # validates
    message_title = models.CharField() #validates

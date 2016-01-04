from django.db import models

# Create your models here.


class Message(object):
    def __init__(self):
        self.status = None    #ok|redirect|error
        self.to = None
        self.message = None

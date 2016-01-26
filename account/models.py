from django.db import models
from collections import OrderedDict
# Create your models here.


class Message(object):
    def __init__(self):
        self.status = None    #ok|redirect|error
        self.to = None
        self.msg = None

    def getdict(self):
        result = dict()
        result['message'] = dict(self.__dict__.items())
        return result

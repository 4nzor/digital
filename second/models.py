import os

import sys
from django.contrib.auth.models import User
from django.db import models
import random

def avatar_upload_to(instance, filename):
    rand = random.randrange(0, sys.maxsize)
    rand = str(rand)
    return os.path.join('avatars/' + instance.username, rand + os.path.splitext(filename)[1])


from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(userdata)
admin.site.register(feedbackdata)
admin.site.register(Cart)
admin.site.register(Checkout)
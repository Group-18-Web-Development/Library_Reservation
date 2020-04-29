# Register your models here.

from django.contrib import admin


from Account_App.models import User
from Book_App.models import Seat
from Book_App.models import Reservation


admin.site.register(User)
admin.site.register(Seat)
admin.site.register(Reservation)

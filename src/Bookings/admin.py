from django.contrib import admin
from .models import BookingModel, LaneModel

# Registering a models allows us to create, edit and delete them in the
# database from the django provided admin page.
admin.site.register(BookingModel)
admin.site.register(LaneModel)

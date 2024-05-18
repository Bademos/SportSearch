from django.contrib import admin
from .models import SportUser, SportType,  ProcessingStatus, Event, Review, Complaint,Application, UsersSportTypes

admin.site.register(SportType)
#admin.site.register(SenderOfReview)
#admin.site.register(ReceiverOfReview)
admin.site.register(ProcessingStatus)

admin.site.register(Event)
admin.site.register(Review)
admin.site.register(Complaint)
admin.site.register(UsersSportTypes)
admin.site.register(SportUser)



# Register your models here.

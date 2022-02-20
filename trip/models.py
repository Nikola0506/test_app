from django.db import models
from custome_user.models import CustomeUsers
from destination.models import Destination
# Create your models here.
class Trip(models.Model):
    """
    Model trip
    """

    class PaymentMethod(models.TextChoices):
        """
        way to pay for the trip
        """
        CACHE = 'Cache', "Cache"
        INSTALLMENTS = 'Installments', "Installments"


    id_trip = models.BigAutoField(primary_key=True)

    custome_user = models.ForeignKey(CustomeUsers,
                                        null=True,
                                        blank=True,
                                        on_delete=models.SET_NULL
                                        )

    price = models.FloatField('Price', default=0)

    adult_number = models.CharField(max_length=50, blank=True, null=True)

    children_number = models.CharField(max_length=50, blank=True, null=True)

    note = models.CharField("Note", max_length=252,
                                default="",
                                blank=True
                                )

    trip_plan_date = models.DateField("trip date", null=True, blank=True)

    flight_from_city = models.ForeignKey(Destination,
                             on_delete=models.CASCADE,
                             db_column='id_destination_from',
                             related_name='from_city'
                             )

    fligh_to_city_hotel = models.ForeignKey(Destination,
                             on_delete=models.CASCADE,
                             db_column='id_destination_to',
                             related_name='to_city_hotel'
                             )


    payment_method = models.CharField("Payment method", max_length=30,
                                      choices=PaymentMethod.choices,
                                      null=False, blank=False,
                                      default=PaymentMethod.CACHE
                                      )

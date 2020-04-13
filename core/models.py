from django.db import models

# Create your models here.
from authentication.models import ModelBase, User, Role, ActiveModel
from payment.models import Payment


class EventType(ActiveModel):
    type = models.CharField(unique=True, max_length=256)

    def __str__(self):
        return self.type


class Event(ActiveModel):
    name = models.CharField(max_length=256)
    type = models.ForeignKey(EventType, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=512)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=512)
    images = models.CharField(max_length=512, null=True, blank=True)
    subscription_fee = models.PositiveIntegerField()
    no_of_tickets = models.PositiveIntegerField()
    sold_tickets = models.PositiveIntegerField(default=0)
    is_cancelled = models.BooleanField(default=False)
    external_links = models.CharField(max_length=1024, null=True, blank=True)
    event_created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ("name", "type", "date", "time")

    def __str__(self):
        return "{}-{}".format(self.name, self.type)


class Invitation(ActiveModel):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    discount_percentage = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return "{}-{}-{}".format(self.event, self.user, self.discount_percentage)


class EventPreference(ActiveModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    event_type = models.ForeignKey(EventType, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{}-{}-{}".format(self.user, self.event_type)


class WishList(ActiveModel):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ("event", "user")

    def __str__(self):
        return "{}-{}-{}".format(self.user, self.event, self.is_active)


class Subscription(ActiveModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    no_of_tickets = models.FloatField()
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.event.sold_tickets += self.no_of_tickets
        self.event.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}-{}-{}".format(self.user, self.event, self.no_of_tickets)


class UserInterest(ActiveModel):
    event_type = models.ForeignKey(EventType, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserProfile(ModelBase):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True, blank=True)
    contact_number = models.CharField(max_length=10, null=True, blank=True)
    organization = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return "{}-{}-{}".format(self.user, self.name, self.contact_number)


class Notification(ModelBase):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=512)
    has_read = models.BooleanField(default=False)

    def __str__(self):
        return "{}-{}-{}".format(self.user, self.event, self.message)

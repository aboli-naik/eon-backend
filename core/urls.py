from django.conf.urls import url
from django.urls import include, path

from core.presigned_url import PresignedUrl
from core.routes import router
from core.views import EventTypeView, SubscriberReminder

from core.views_layer.subscription import SubscriptionViewSet
from core.views_layer.invitation import InvitationViewSet


urlpatterns = [
    url('^', include(router.urls)),
    url('subscription', SubscriptionViewSet.as_view(), name="subscription"),
    url('presigned-url', PresignedUrl.as_view(), name="image_upload"),

    url('invite', InvitationViewSet.as_view(), name="invite"),

    url("event-type", EventTypeView.as_view(), name="event_type"),
    url('reminder', SubscriberReminder.as_view(), name="subscriber_reminder")

]

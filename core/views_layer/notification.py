"""
Notification Module Related methods added here
"""
import jwt

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import get_authorization_header
from rest_framework_simplejwt.authentication import JWTAuthentication

from core.models import Notification
from core.serializers import NotificationSerializer
from eon_backend.settings.common import SECRET_KEY, LOGGER_SERVICE

from utils.common import api_success_response, api_error_response

logger = LOGGER_SERVICE


class NotificationView(APIView):
    """API for Notification"""

    serializer_class = NotificationSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Notification.objects.filter(has_read=False)

    def patch(self, request):
        """
        Patch api method of notification
        """

        token = get_authorization_header(request).split()[1]
        payload = jwt.decode(token, SECRET_KEY)
        user_id = payload['user_id']
        list_of_ids = request.data.get('notification_ids')

        try:
            self.queryset.filter(id__in=list_of_ids).update(has_read=True)
        except Exception as err:
            logger.log_error(str(err))
            return api_error_response(message="Something went wrong", status=500)

        logger.log_info(f"Notification status updated successfully by user_id {user_id}")
        return api_success_response(message="Notification updated successfully", status=200)

    def get(self, request):
        """
        Get api method for Notification
        """

        token = get_authorization_header(request).split()[1]
        payload = jwt.decode(token, SECRET_KEY)
        user_id = payload['user_id']

        try:
            notifications = self.queryset.filter(user=user_id).order_by("-created_on")

        except Notification.DoesNotExist:
            notifications = []

        serializer = self.serializer_class(notifications, many=True)
        logger.log_info(f"Notification fetched successfully by user_id {user_id}")
        return api_success_response(data=serializer.data)

from rest_framework.exceptions import APIException


class UnauthorizedException(APIException):
    status_code = 403
    default_detail = 'Forbidden, Please login to continue'
    default_code = 'service_unavailable'
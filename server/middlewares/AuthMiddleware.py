from rest_framework.exceptions import AuthenticationFailed
import jwt


def AuthRequired(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Authentication required')
    try:
        user = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Authentication required')
    return user

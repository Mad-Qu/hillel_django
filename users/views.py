from django.http import HttpResponse
from django.contrib.auth import get_user_model

User = get_user_model()


def users(request):
    users = User.objects.all()
    results = ", ".join([user.username for user in users])
    return HttpResponse(results)
from http import HTTPStatus
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .tasks import process_event
# Create your views here.


@csrf_exempt
def aggregate(request):
    if request.method == 'POST':
        process_event.delay(json.loads(request.body.decode('utf-8')))

        return JsonResponse({'message': 'accepted'})

    return JsonResponse({'message': 'ONLY POST ACCEPT'}, status=HTTPStatus.BAD_REQUEST)

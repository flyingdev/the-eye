from http import HTTPStatus
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from .tasks import process_event
# Create your views here.


@csrf_exempt
def aggregate(request):
    if request.method == 'POST':
        process_event.delay(request.POST)

        return JsonResponse({'message': 'accepted'})

    return JsonResponse({'message': 'ONLY POST ACCEPT'}, status=HTTPStatus.BAD_REQUEST)

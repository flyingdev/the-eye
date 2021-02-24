from the_eye import celery_app

from .models import Event
from .validators import validate_format, validator_factory


@celery_app.task
def process_event(payload):
    if not payload:
        return False

    if not validate_format(payload):
        return False

    category = payload['category']
    name = payload['name']
    key = ' '.join([category, name])
    if not validator_factory.validate(key=key, data=payload['data']):
        return False

    try:
        event = Event(session_id=payload['session_id'],
                      category=payload['category'], name=payload['name'],
                      data=payload['data'], timestamp=payload['timestamp'])
        event.save()

        return True
    except Exception as e:
        # TODO
        #  log every error
        print(str(e))

        return False

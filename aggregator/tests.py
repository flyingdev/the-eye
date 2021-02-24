from http import HTTPStatus
from django.test import TestCase, Client
from django.urls import reverse
import json

from aggregator.tasks import process_event


# Create your tests here.
class AggregatorTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_aggregate(self):
        with open('tests/events_1.json') as fp:
            data = json.load(fp)

        event_aggregate_url = reverse('event-url')
        response = self.client.post(event_aggregate_url, data)

        assert response.status_code == HTTPStatus.OK


class TasksTest(TestCase):
    def setUp(self) -> None:
        pass

    def test_process_event(self):
        with open('tests/events_1.json') as fp:
            data = json.load(fp)

        processed = process_event(data)

        assert processed is True

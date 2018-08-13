from django.test import TestCase, Client
from django.urls import reverse

import json


class BookViewTest(TestCase):

    def setUp(self):
        print("Test started")

    def testListView(self):
        client = Client()
        response = client.get(reverse("books:create"))

    def testCreateView(self):
        query = {
            "title": "title",
            "content": "content",
            "author_name": "author_name",
            "price": 10000
        }
        client = Client()
        response = client.post(reverse("books:create"), data=json.dumps(query), content_type="application/json")

    def tearDown(self):
        print("Test Ended")


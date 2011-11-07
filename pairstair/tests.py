"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from models import Programmer, Pair
from views import create_pairs

NAMES = ["Minkey", "Minnie"]

def format_input(names):
    return ",".join(names)


class TestPairStair(TestCase):
    def test_should_render_page_to_create_programmers(self):
        response = Client().get("/create/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "create_programmers.html")

    def test_should_redirect_to_pair_stair_page(self):
        response = Client().post("/create/", {"programmer_names":format_input(NAMES)})
        self.assertRedirects(response, "/stairs/")

    def test_should_render_programmers_to_pair_stairs(self):
        response = Client().post("/create/", {"programmer_names":format_input(NAMES)}, follow=True)
        for name in NAMES:
            self.assertContains(response, name)

    def test_should_save_programmers(self):
        Client().post("/create/", {"programmer_names": format_input(NAMES)})
        for name in NAMES:
            self.assertEqual(Programmer.objects.filter(name=name).count(), 1)

    def test_should_recreate_programmer_each_time(self):
        Client().post("/create/", {"programmer_names":format_input(NAMES)})
        self.assertEqual(len(NAMES), Programmer.objects.all().count())

    def test_should_redirect_to_error_page(self):
        response = Client().post("/create/", {"programmer_names": "Minkey"}, follow=True)
        self.assertTemplateUsed(response, "error.html")

    def test_should_create_pairs(self):
        programmers = []
        count = 0
        for name in NAMES:
            programmers.append(Programmer(name = name, id = count))
            count += 1
        pairs = create_pairs(programmers)
        self.assertEqual(1, len(pairs))
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
from .models import Todo


class TodoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="Learn about typescript",
            body="Check freecodecamp course",
        )
        cls.todo2 = Todo.objects.create(
            title="Second title",
            body="Second Body",
        )

    def test_todo_model_content(self):
        self.assertEqual(str(self.todo), "Learn about typescript")
        self.assertEqual(self.todo.title, "Learn about typescript")
        self.assertEqual(self.todo.body, "Check freecodecamp course")

        self.assertEqual(str(self.todo2), "Second title")
        self.assertEqual(self.todo2.title, "Second title")
        self.assertEqual(self.todo2.body, "Second Body")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 2)
        self.assertContains(response, self.todo)
        self.assertContains(response, self.todo2)

    def test_api__detailview(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}), format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.todo)

from django.urls import reverse

from django.contrib.auth.models import User

from rest_framework import response, status
from rest_framework.test import APITestCase, APIClient

from .models import *


class UserTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.username = 'admin'
        self.password = 'admin'
        self.is_staff = True

    # user login section

    def test_login_user(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        loggedin_user = auth.get_user(self.client)
        self.assertEqual(loggedin_user.username, self.client.username)

    # broadcast type section

    def test_broadcastType_list(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        url = reverse('broadcasttype-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_broadcastType_detail(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        url = f"broadcastTypes/{test_broadcastType.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_broadcastType_create(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        url = reverse('broadcasttype-list')
        data = {'name': 'TestName'}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BroadcastType.objects.count(), 1)
        self.assertEqual(BroadcastType.objects.get().name, 'TestName')

    def test_broadcastType_delete(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        url = reverse('broadcasttype-list')
        data = {'name': 'TestName'}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BroadcastType.objects.count(), 1)

        detail_url = "broadcastTypes/1/"
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(BroadcastType.objects.count(), 0)

    # broadcast section

    def test_broadcast_list(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        test_broadcast = Broadcast.objects.create(
            title='TestBroadcast', broadcast_type=test_broadcastType)

        url = reverse('broadcast-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_broadcast_detail(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        test_broadcast = Broadcast.objects.create(
            title='TestBroadcast', broadcast_type=test_broadcastType)

        url = f"broadcasts/{test_broadcast.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_broadcast_create(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        url = reverse('broadcast-list')
        data = {'title': 'TestName', 'broadcast_type': test_broadcastType}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Broadcast.objects.count(), 1)
        self.assertEqual(Broadcast.objects.get().name, 'TestName')

    def test_broadcast_delete(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        url = reverse('broadcast-list')
        data = {'title': 'TestName', 'broadcast_type': test_broadcastType}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Broadcast.objects.count(), 1)

        detail_url = "broadcasts/1/"
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Broadcast.objects.count(), 0)

    # event section

    def test_event_list(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        test_broadcast = Broadcast.objects.create(
            title='TestBroadcast', broadcast_type=test_broadcastType)

        test_event = Event.objects.create(broadcast=test_broadcast)

        url = reverse('event-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_detail(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        test_broadcast = Broadcast.objects.create(
            title='TestBroadcast', broadcast_type=test_broadcastType)

        test_event = Event.objects.create(broadcast=test_broadcast)

        url = f"events/{test_event.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_create(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        test_broadcast = Broadcast.objects.create(
            title='TestBroadcast', broadcast_type=test_broadcastType)

        url = reverse('event-list')
        data = {'title': 'TestName', 'broadcast': test_broadcast}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().name, 'TestName')

    def test_event_delete(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        test_broadcast = Broadcast.objects.create(
            title='TestBroadcast', broadcast_type=test_broadcastType)

        url = reverse('event-list')
        data = {'title': 'TestName', 'broadcast': test_broadcast}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)

        detail_url = "events/1/"
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.count(), 0)

    # comment section

    def test_comment_list(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        test_broadcast = Broadcast.objects.create(
            title='TestBroadcast', broadcast_type=test_broadcastType)

        test_comment = Comment.objects.create(
            owner=user, broadcast=test_broadcast)

        url = reverse('comment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_detail(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        test_broadcast = Broadcast.objects.create(
            title='TestBroadcast', broadcast_type=test_broadcastType)

        test_comment = Comment.objects.create(
            owner=user, broadcast=test_broadcast)

        url = f"comments/{test_comment.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_create(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        test_broadcast = Broadcast.objects.create(
            title='TestBroadcast', broadcast_type=test_broadcastType)

        url = reverse('comment-list')
        data = {'owner': user, 'data': 'TestComment',
                'broadcast': test_broadcast}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get().name, 'TestComment')

    def test_comment_delete(self):
        user = User.objects.create(
            username=self.username, password=self.password, is_staff=True)

        self.client.login(
            username=self.username, password=self.password)

        test_broadcastType = BroadcastType.objects.create(
            name='TestBroadcastType')

        test_broadcast = Broadcast.objects.create(
            title='TestBroadcast', broadcast_type=test_broadcastType)

        url = reverse('comment-list')
        data = {'owner': user, 'data': 'TestComment',
                'broadcast': test_broadcast}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)

        detail_url = "events/1/"
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.count(), 0)

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from notes.serializers import UserSerializer, GroupSerializer, NotesSerializer
from notes.models import Note



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class NotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viwed or edited.
    """
    permission_classes = (IsAuthenticated,)

    queryset = Note.objects.all()
    serializer_class = NotesSerializer
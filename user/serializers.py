from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import User as The_User
User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ( 'id','first_name', 'last_name', 'email' ,'password')
        # read_only_fields = ('id', 'created', 'updated' )
    def get_fullname(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def __init__(self, *args, **kwargs):
        super(UserCreateSerializer, self).__init__(*args, **kwargs)
        if 'context' in kwargs and 'request' in kwargs['context']:
            if kwargs['context']['request'] is not None:

                if kwargs['context']['request'].method == 'GET':
                    if 'pk' in kwargs['context']['request'].resolver_match.kwargs:
                        desired_fields = set(self.fields)
                    else:
                        # Selected fields for a all GET  request
                        desired_fields = { 'id', }

                    restricted_fields = set(self.fields) - desired_fields
                    for field_name in restricted_fields:
                        self.fields.pop(field_name)


 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = The_User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'aadhar', 'address', 'postal_code']



from rest_framework import serializers
from django.utils.html import escape

from .models import Note



class NoteSerializers(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError('erro massege')
        return escape(value.strip())
    

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError('error massege')
        return escape(value.strip())
    

class NoteCreateSerializers(NoteSerializers):
    pass


class NoteUpdateSerializers(NoteSerializers):
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
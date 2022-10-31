from rest_framework import serializers
# from musicapp.models import Artiste, Song, Lyrics
from .models import *

# create a model serializer class
class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['id', 'first_name', "last_name", "age"]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song # this is the model class in your models.py file
        fields = ['id', 'title', 'artiste',"date_released", "likes"]
        # the fields contains each variable you create in ur model.py class

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = ['id', 'song_id', 'content']

  
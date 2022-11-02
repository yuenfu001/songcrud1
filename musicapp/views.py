from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.decorators import api_view

# Create your views here.

# END POINT FOR ARTISTE
@api_view(["GET","POST"]) #we are creating a view for GET and POST REQUEST
def artist_list(request):
    # we want to get all the list of artists in our database
    if request.method == "GET":
        artists = Artiste.objects.all()
        # we also want to convert it to JSON format
        serializer = ArtisteSerializer(artists, many=True) # true meaning we want to get as much data as registered on the database
        # return JsonResponse(serializer.data, safe=False)
        return Response({"artists":serializer.data})
    
    if request.method == "POST":
        serializer = ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def uniqueArtist(request, pk):
    try:
        artist = Artiste.objects.get(id=pk)
    except Artiste.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ArtisteSerializer(artist)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ArtisteSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    # else:
    if request.method == "DELETE": 
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# END POINT FOR SONG

@api_view(["GET","POST"]) #we are creating a view for GET and POST REQUEST
def song_list(request):
    # we want to get all the list of artists in our database
    if request.method == "GET":
        songs = Song.objects.all()
        # we also want to convert it to JSON format
        serializer = SongSerializer(songs, many=True) # true meaning we want to get as much data as registered on the database
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# dynamic routing endpoint for individual songs on DB
@api_view(['GET','PUT','DELETE'])
def uniqueSong(request, pk):
    try:
        songs = Song.objects.get(id=pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        serializer = SongSerializer(songs)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = SongSerializer(songs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    # else:
    if request.method == "DELETE": 
        songs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# END POINT FOR LYRICS

@api_view(["GET","POST"]) #we are creating a view for GET and POST REQUEST
def lyrics_list(request):
    # we want to get all the list of artists in our database
    if request.method == "GET":
        lyrics = Lyrics.objects.all()
        # we also want to convert it to JSON format
        serializer = LyricSerializer(lyrics, many=True) # true meaning we want to get as much data as registered on the database
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = LyricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# dynamic routing endpoint for individual lyrics on DB

@api_view(['GET','PUT','DELETE'])
def uniqueLyrics(request, pk):
    try:
        lyrics = Lyrics.objects.get(id=pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = LyricSerializer(lyrics)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = LyricSerializer(lyrics, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    # else:
    if request.method == "DELETE": 
        songs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




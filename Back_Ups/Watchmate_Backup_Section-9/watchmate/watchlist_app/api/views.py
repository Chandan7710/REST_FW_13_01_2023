from django.shortcuts import get_object_or_404

# Rest Framework Import
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# App Import
from watchlist_app.models import Movie, Watchlist, StreamPlatform, Review
from watchlist_app.api.serializers import (MovieSerializer, WatchlistSerializer, 
                                           StreamPlatformSerializer, ReviewSerializer)
from watchlist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly

@api_view(['GET', 'POST'])
def movie_list(request):
    
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_details(request, value):
    
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=value)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=value)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=value)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# API View
class MovieListAV(APIView):
    
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class MovieDetailAV(APIView):
    
    def get(self, request, value):
        try:
            movie = Movie.objects.get(pk=value)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, value):
        movie = Movie.objects.get(pk=value)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, value):
        movie = Movie.objects.get(pk=value)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

# API View       
# Updating Model - Section

class WatchlistAV(APIView):
    
    def get(self, request):
        movies = Watchlist.objects.all()
        serializer = WatchlistSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchlistDetailAV(APIView):
    
    def get(self, request, value):
        try:
            movie = Watchlist.objects.get(pk=value)
        except Watchlist.DoesNotExist:
            return Response({'Error': 'Watchlist Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchlistSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, value):
        movie = Watchlist.objects.get(pk=value)
        serializer = WatchlistSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, value):
        movie = Watchlist.objects.get(pk=value)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformAV(APIView):
    
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        '''add this context={'request': request} inside serializer 
        when you use serializers.HyperlinkedRelatedField'''
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    
class StreamPlatformDetailAV(APIView):
    
    def get(self, request, value):
        try:
            platform = StreamPlatform.objects.get(pk=value)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'StreamPlatform Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, value):
        platform = StreamPlatform.objects.get(pk=value)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, value):
        platform = StreamPlatform.objects.get(pk=value)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
'''Views using Mixins'''
class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    '''queryset and serializer_class are attributes name we canot change 
    them with other variable name'''
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

'''Concrete View Class'''

class ReviewListNew(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewDetailNew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
  
  
'''Concrete View Class Query List''' 
  
class ReviewListQuery(generics.ListAPIView):
    
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class ReviewDetailQuery(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    #permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticatedOrReadOnly]
    #permission_classes = [AdminOrReadOnly]
    #permission_classes = [ReviewUserOrReadOnly]
    permission_classes = [IsAuthenticated]
    
    
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        movie = Watchlist.objects.get(pk=pk)
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=movie, review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("You Have Already Reviewed This Movie")
        
        if movie.number_rating == 0:
            movie.avg_rating = serializer.validated_data['rating']
        else:
            movie.avg_rating = (movie.avg_rating + serializer.validated_data['rating'])/2
        movie.number_rating = movie.number_rating + 1
        movie.save()
        
        serializer.save(watchlist=movie, review_user=review_user)


# ViewSet Class


class StreamPlatformVS(viewsets.ViewSet):
    
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(watchlist)
        return Response(serializer.data)
        
    def create(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
'''Model Viewset'''

class StreamPlatformMVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
'''Readonly Model Viewset'''

class StreamPlatformROMVS(viewsets.ReadOnlyModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
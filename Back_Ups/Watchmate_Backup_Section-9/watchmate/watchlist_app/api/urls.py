from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views
from watchlist_app.api.views import MovieListAV, MovieDetailAV
from watchlist_app.api.views import (WatchlistAV, WatchlistDetailAV, 
                                     StreamPlatformAV, StreamPlatformDetailAV, 
                                     ReviewList, ReviewDetail, ReviewListNew,
                                     ReviewDetailNew, ReviewListQuery, ReviewDetailQuery, 
                                     ReviewCreate, StreamPlatformVS, StreamPlatformMVS, 
                                     StreamPlatformROMVS)

router = DefaultRouter()
router.register('streamnew', StreamPlatformVS, basename = 'streamplatform')
router.register('streamnewmvs', StreamPlatformMVS, basename = 'streamplatformmvs')
router.register('streamnewromvs', StreamPlatformROMVS, basename = 'streamplatformromvs')

urlpatterns = [
    
    path('list/', views.movie_list, name='movie_list'),
    path('list/<int:value>/', views.movie_details, name='movie_details'),
    
    path('classlist/', MovieListAV.as_view(), name='movie_class_list'),
    path('classlist/<int:value>/', MovieDetailAV.as_view(), name='movie_class_details'),
    
    path('watchlist/', WatchlistAV.as_view(), name='watch_class_list'),
    path('watchlist/<int:value>/', WatchlistDetailAV.as_view(), name='watch_class_details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream_class_list'),
    path('stream/<int:value>/', StreamPlatformDetailAV.as_view(), name='stream_class_details'),
    
    path('review/', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
    
    path('reviewnew/', ReviewListNew.as_view(), name='review_list_new'),
    path('reviewnew/<int:pk>/', ReviewDetailNew.as_view(), name='review_detail_new'),
    
    
    path('watchlistnew/<int:pk>/review/', ReviewListQuery.as_view(), name='watch_class_list_new'),
    path('watchlistnew/review/<int:pk>/', ReviewDetailQuery.as_view(), name='watch_class_details_new'),
    
    path('watchlistnew/<int:pk>/reviewcreate/', ReviewCreate.as_view(), name='review_create'),
    
    path('', include(router.urls)),
    
]

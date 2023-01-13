from rest_framework import serializers
from watchlist_app.models import Movie, Watchlist, StreamPlatform, Review

"""  
def name_length(value):
    if len(value) < 3:
        raise serializers.ValidationError("Name is too short! Length Should be at least 3 characters")
    else:
        return value
    
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    '''
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value
            
    '''
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description cannot be the same!")
        else:
            return data
"""

'''Model serializers'''
class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    len_descr = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = "__all__"
        
        '''We can define our indivisual fields by'''
        #fields = ['id', 'name', 'description']
        #exclude = ['description']
        
    def get_len_name(self, object):
        length = len(object.name)
        return length
    
    def get_len_descr(self, object):
        length1 = len(object.description)
        return length1
        
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and description cannot be the same!")
        else:
            return data
        
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value
        
''' Modlels With Relations'''
 
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ('watchlist',)
        #fields = "__all__"
        
class WatchlistSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Watchlist
        fields = "__all__"
        
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    
    watchlist_platform = WatchlistSerializer(many=True, read_only=True)
    
    #watchlist_platform = serializers.StringRelatedField(many=True)
    #watchlist_platform = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # watchlist_platform = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='watch_class_details'
    # )
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
 

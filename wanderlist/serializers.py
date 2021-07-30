from rest_framework import serializers
from .models import State, Recommendation

class StateSerializer(serializers.HyperlinkedModelSerializer):
    recommendations = serializers.HyperlinkedRelatedField(
        view_name='recommendation_detail',
        many=True,
        read_only=True
    )

    state_url = serializers.ModelSerializer.serializer_url_field(
        view_name='state_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = State
        fields = ('id', 'name', 'state_flag', 'recommendations',
                  'state_url', 'owner')

class RecommendationSerializer(serializers.HyperlinkedModelSerializer):
    state = serializers.HyperlinkedRelatedField(
        view_name='state_detail', read_only=True)

    state_id = serializers.PrimaryKeyRelatedField(
        queryset=State.objects.all(), source='state')

    state_name = serializers.SlugRelatedField(
        queryset=State.objects.all(), slug_field='name', source='state')

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Recommendation
        fields = ('state', 'state_id', 'title',
                  'body', 'created', 'state_name', 'photo_url', 'owner')
from rest_framework import serializers
from .models import Trip, Note



class NoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Note
    fields = ['trip', 'name', 'description', 'type', 'rating']


class TripSerializer(serializers.ModelSerializer):
  note_set = NoteSerializer(many=True, read_only=True)
    
  class Meta:
    model = Trip
    fields = ['city', 'country', 'start_date', 'end_date', 'owner', 'note_set']


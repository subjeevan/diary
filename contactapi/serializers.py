from contact.models import Contact
from rest_framework import serializers
     
class Dataserializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        exclude=['country']
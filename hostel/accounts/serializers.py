from rest_framework import serializers
from .models import Inmates

class InmatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inmates 
        fields = ('pk', 'Hostel_ID', 'Name', 'Room_Num', 'Preference', 'Bill_Amount', 'MC', 'Marked')
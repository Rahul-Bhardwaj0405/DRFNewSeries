from dataclasses import field
from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields = ['name', 'age']
        # exclude = ['id',] # It will serailize all fields except id
        fields = '__all__'  #It Serializes all fields

    
    def validate(self, data):

        if data['age'] < 18:
            raise serializers.ValidationError({"error":"Age cannot be less than 18"})
        
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error": "Name cannot be numeric"})
        return data
        

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['category_name',] 


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'  
        # depth = 1


    

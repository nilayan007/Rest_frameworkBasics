from rest_framework import serializers
from .models import *
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #fields = ['name','age']
        #exclude = ['name'] #will exclude that field
      
        fields = '__all__' #for including all fields 
    def validate(self,data):
        if data['age']<18:
            raise serializers.ValidationError({'error': 'age cant be below 18'})
        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error': 'name cant be numeric'})

        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name'] 

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = book
        fields = '__all__'          
    
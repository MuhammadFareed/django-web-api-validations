from api.models import Student
from rest_framework import serializers


# Validaion by validators (This def remains outside the serializer class)
def is_name_starts_with_s(value):
    if value[0].lower() != 's':
            raise serializers.ValidationError('Name should start with the letter S')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, validators=[is_name_starts_with_s])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name) 
        instance.roll = validated_data.get('roll', instance.roll) 
        instance.city = validated_data.get('city', instance.city) 
        instance.save()
        return instance



    #########################################
    #                                       #
    #               Validations             #
    #                                       #
    #########################################



    # Field level validaion
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Roll number must be less than 200')
        return value

    # Object level validaion
    def validate(self, data):
        name = data.get('name')
        roll = data.get('roll')
        city = data.get('city')
        if name.lower() == 'fareed':
            raise serializers.ValidationError('User with this name already exist')
        if roll >= 200:
            raise serializers.ValidationError('Roll number must be less than 200')

        return data





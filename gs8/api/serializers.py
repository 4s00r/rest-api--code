from rest_framework import serializers
from .models import Student





class StudentSerializer(serializers.ModelSerializer):
  # Validators
  def start_with_r(value):
    if value[0].lower() != 'r':
      raise serializers.ValidationError('name should be start with R')

  name = serializers.CharField(validators=[start_with_r])
  class Meta:
    model = Student
    fields = ['id', 'name', 'roll', 'city']


  # id = serializers.IntegerField()
  # name = serializers.CharField(max_length=100, validators=[start_with_r])
  # roll = serializers.IntegerField()
  # city = serializers.CharField(max_length=100)

  # def create(self, validate_data):
  #   return Student.objects.create(**validate_data)

  # def update(self, instance, validated_data):
  #   print (instance.name)
  #   instance.name= validated_data.get('name',instance.name)
  #   print(instance.name)
  #   instance.roll= validated_data.get('roll',instance.roll)    
  #   instance.city= validated_data.get('city',instance.city)
  #   instance.save()
  #   return instance

  # field level validation 

  def validate_roll(self, value):
    if value >= 200:
      raise serializers.ValidationError('seat full')
    return value

    # object level validation

  def validate(self, data):
    nm = data.get('name')
    ct = data.get('name')
    if nm.lower() == 'viru' and ct.lower() !='ranchi':
      raise serializers.ValidationError('City must be Ranchi')
    return data


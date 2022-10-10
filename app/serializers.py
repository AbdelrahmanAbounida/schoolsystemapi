from email.policy import default
from .models import Student,Teacher,Subject
from rest_framework import serializers


## Serialization can be done using one of those 2 classes serializer and modelSerializer

#######################################################
#################### Serializer #######################
#######################################################

class StudentSerializer1(serializers.Serializer):
    
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    grade = serializers.FloatField(default=0) 
    ## and so on

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.save()
        return instance


#######################################################
#################### ModelSerializer ##################
#######################################################


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    teachers = serializers.PrimaryKeyRelatedField(many=True, queryset=Teacher.objects.all())
    class Meta:
        model = Subject
        fields = ['id','name','teachers']
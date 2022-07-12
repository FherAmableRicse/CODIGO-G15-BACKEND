from rest_framework import serializers

from .models import Alumno,Profesor

class AlumnoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    email = serializers.EmailField()

    def create(self,validate_data):
        return Alumno.objects.create(**validate_data)

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        #fields = ["nombre","email"]
        fields = '__all__'

from functools import partial
import io
from django.views import View
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            json_data = request.body
            stream = io.BytesIO(json_data)
            data = JSONParser().parse(stream)
            id = data.get('id', None)
            if id is not None:
                student = Student.objects.get(id = id)
                serialized_data = StudentSerializer(student)
                json_data = JSONRenderer().render(serialized_data.data)
                return HttpResponse(json_data, content_type='application/json')
            
            students = Student.objects.all()
            serialized_data = StudentSerializer(students, many=True)
            json_data = JSONRenderer().render(serialized_data.data)
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            json_data = request.body
            strem = io.BytesIO(json_data)
            python_data  = JSONParser().parse(strem)
            serialized_data = StudentSerializer(data=python_data)
            if serialized_data.is_valid():
                serialized_data.save()
                res = { 'message': 'created' }
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serialized_data.errors)
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            json_data = request.body
            strem = io.BytesIO(json_data)
            python_data  = JSONParser().parse(strem)
            student_id_to_update = python_data.get('id')
            student = Student.objects.get(id=student_id_to_update)
            serialized_data = StudentSerializer(student, data=python_data, partial=True)
            if serialized_data.is_valid():
                serialized_data.save()
                res = { 'message': 'updated' }
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serialized_data.errors)
            return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        if request.method == 'DELETE':
            json_data = request.body
            strem = io.BytesIO(json_data)
            python_data  = JSONParser().parse(strem)
            student_id_to_update = python_data.get('id')
            student = Student.objects.get(id=student_id_to_update)
            student.delete()
            res = { 'message': 'deleted' }
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
from functools import partial
import io
from django.views import View
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            json_data = request.body
            stream = io.BytesIO(json_data)
            data = JSONParser().parse(stream)
            id = data.get('id', None)
            if id is not None:
                student = Student.objects.get(id = id)
                serialized_data = StudentSerializer(student)
                json_data = JSONRenderer().render(serialized_data.data)
                return HttpResponse(json_data, content_type='application/json')
            
            students = Student.objects.all()
            serialized_data = StudentSerializer(students, many=True)
            json_data = JSONRenderer().render(serialized_data.data)
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            json_data = request.body
            strem = io.BytesIO(json_data)
            python_data  = JSONParser().parse(strem)
            serialized_data = StudentSerializer(data=python_data)
            if serialized_data.is_valid():
                serialized_data.save()
                res = { 'message': 'created' }
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serialized_data.errors)
            return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        if request.method == 'PUT':
            json_data = request.body
            strem = io.BytesIO(json_data)
            python_data  = JSONParser().parse(strem)
            student_id_to_update = python_data.get('id')
            student = Student.objects.get(id=student_id_to_update)
            serialized_data = StudentSerializer(student, data=python_data, partial=True)
            if serialized_data.is_valid():
                serialized_data.save()
                res = { 'message': 'updated' }
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer().render(serialized_data.errors)
            return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        if request.method == 'DELETE':
            json_data = request.body
            strem = io.BytesIO(json_data)
            python_data  = JSONParser().parse(strem)
            student_id_to_update = python_data.get('id')
            student = Student.objects.get(id=student_id_to_update)
            student.delete()
            res = { 'message': 'deleted' }
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Work
from .serializers import WorkSerializer

@csrf_exempt
@api_view(['GET'])
def work_list(request):
    works = Work.objects.all()
    serializer = WorkSerializer(works, many=True)
    return Response(serializer.data)

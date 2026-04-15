from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Work
from .serializers import WorkSerializer


@api_view(['GET'])
def work_list(request):
    works = Work.objects.all()

    serializer = WorkSerializer(
        works,
        many=True,
        context={'request': request}  # 🔥 BURASI VACİBDİR
    )

    return Response(serializer.data)

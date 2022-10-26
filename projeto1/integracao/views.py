from rest_framework import viewsets
from integracao.models import Video
from integracao.serializer import VideoSerializer
# Create your views here.

class VideosViewSet(viewsets.ModelViewSet):
    ''''exebindo todos os vídeos da plataforma '''
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

from firma.models import Signing


class SignView(APIView):
    def get(self, request):
        sign = Signing.objects.all()
        return Response({"signing": sign})
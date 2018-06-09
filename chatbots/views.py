from rest_framework.response import Response
from rest_framework.views import APIView


class HomeKeyboardViewSet(APIView):
    def get(self, request):
        result = {
            "type": "buttons",
            "buttons": ["날씨", "지하철", "요가"]
        }
        return Response(result)

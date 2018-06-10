from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def home_keyboard(request):
    result = {
        "type": "buttons",
        "buttons": ["날씨", "지하철", "요가"]
    }
    return Response(result)


@api_view(['POST'])
def message(request):
    result = {"message": {"text": "안녕. 지민아"}}
    return Response(result)

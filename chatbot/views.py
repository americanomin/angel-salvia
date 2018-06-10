from rest_framework.response import Response
from rest_framework.decorators import api_view
from chatbot.utils.yoga_info import YogaInfo

@api_view()
def home_keyboard(request):
    result = {
        "type": "buttons",
        "buttons": ["날씨", "지하철", "요가"]
    }
    return Response(result)

# user_key, type (text), content
@api_view(['POST'])
def message(request):
    text = "안녕. 지민아"
    if request.data['type'] == 'text' and YogaInfo.is_yoga_info_need(request.data['content']):
        text = YogaInfo().today_info()

    result = {"message": {"text": text}}

    return Response(result)

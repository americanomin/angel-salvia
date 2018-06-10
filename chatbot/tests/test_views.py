from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser

def test_home_keyboard_타입과_버튼을_리턴한다(client):
    response = client.get('/keyboard')
    stream = BytesIO(response.content)
    response_content = JSONParser().parse(stream)

    assert 'type' in response_content
    assert 'buttons' in response_content

def test_message_메시지에_텍스트를_담아서_리턴한다(client):
    response = client.post('/message')
    stream = BytesIO(response.content)
    response_content = JSONParser().parse(stream)

    message = response_content['message']
    assert 'text' in message

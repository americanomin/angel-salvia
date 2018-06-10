from chatbot.utils.yoga_info import YogaInfo

class TestYogaInfo:
    def test_is_need_yoga_info_ㅇㄱ이_포함되어있으면_true를_리턴한다(self):
        word = 'ㅇㄱ'
        assert YogaInfo.is_yoga_info_need(word) is True
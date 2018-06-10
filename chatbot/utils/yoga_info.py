import datetime


class YogaSubject:
    def __init__(self, title):
        self.title = title

    def description(self):
        description = {"AM_FLOW": "",
                       "Intro Ashtanga": "균형 감각 및 근력 향상과 유연성 강화에 도움이 되는 수업이야.",
                       "Healing": "",
                       "Therapy": "신체 불균형의 원인이 되는 근육을 이해하고 바른자세를 유지하도록 올바른 정렬을 배우는 수업이야.",
                       "hatha": "아사나와 호흡에 깊이 집중함으로써 몸과 마음에 평온을 가져다주는 수업이야.",
                       "vinyasa": "활기찬 속도감과 물 흐르듯 자연스럽게 이어지는 아사나로 몸 안의 여러 근육들의 힘을 길러주는 수업이야.",
                       "Ashtanga": "균형 감각과 근력 향상과 유연성 강화에 도움이 되는 수업이야.",
                       "Pilates": ""}
        return description[self.title]


class YogaInfo:
    WORD = "ㅇㄱ"

    AM_FLOW = YogaSubject("AM_FLOW")
    INTRO_ASHTANGA = YogaSubject("Intro Ashtanga")
    HEALING = YogaSubject("Healing")
    THERAPY = YogaSubject("Therapy")
    HATHA = YogaSubject("hatha")
    VINYASA = YogaSubject("vinyasa")
    ASHTANGA = YogaSubject("Ashtanga")
    PILATES = YogaSubject("Pilates")

    @classmethod
    def is_yoga_info_need(cls, text):
        return text in YogaInfo.WORD

    @classmethod
    def today_info(self):
        today_schedule = self._schedule()[datetime.date.today().month][self._day_of_week()]
        return "\n\n".join(
            [f"오늘의 {i+1}번째 요가 시작 시간은 {time_plan.from_time}이고, {time_plan.subject.title} 수업이야. \n{time_plan.subject.description()} " for i, time_plan in
             enumerate(today_schedule)])

    @staticmethod
    def _day_of_week():
        return datetime.datetime.today().weekday()

    @staticmethod
    def _schedule():
        june_plan = {
            0: [TimePlan("07:00", "08:00", YogaInfo.AM_FLOW),
                TimePlan("18:50", "19:50", YogaInfo.INTRO_ASHTANGA),
                TimePlan("20:05", "21:05", YogaInfo.HEALING),
                TimePlan("21:20", "22:20", YogaInfo.THERAPY)
                ],
            1: [TimePlan("18:10", "19:10", YogaInfo.HATHA),
                TimePlan("19:20", "20:20", YogaInfo.VINYASA),
                TimePlan("20:30", "21:30", YogaInfo.ASHTANGA),
                TimePlan("21:40", "22:30", YogaInfo.PILATES),

                ],
            2: [TimePlan("07:00", "08:00", YogaInfo.AM_FLOW),
                TimePlan("18:50", "19:50", YogaInfo.HATHA),
                TimePlan("20:05", "21:05", YogaInfo.VINYASA),
                TimePlan("21:20", "22:20", YogaInfo.THERAPY)
                ],
            3: [TimePlan("18:10", "19:10", YogaInfo.INTRO_ASHTANGA),
                TimePlan("19:20", "20:20", YogaInfo.VINYASA),
                TimePlan("20:30", "21:30", YogaInfo.PILATES),
                TimePlan("21:40", "22:30", YogaInfo.PILATES)
                ],
            4: [TimePlan("07:00", "08:00", YogaInfo.AM_FLOW),
                TimePlan("18:50", "19:50", YogaInfo.ASHTANGA),
                TimePlan("20:05", "21:05", YogaInfo.PILATES),
                TimePlan("21:20", "22:20", YogaInfo.THERAPY)
                ],
            5: [
                TimePlan("10:00", "11:20", YogaInfo.ASHTANGA),
                TimePlan("11:30", "12:30", YogaInfo.VINYASA)
            ],
            6: [TimePlan("10:00", "11:00", YogaInfo.INTRO_ASHTANGA),
                TimePlan("11:15", "12:15", YogaInfo.VINYASA)
                ]
        }
        return {6: june_plan}


class TimePlan:
    def __init__(self, from_time, to_time, subject):
        self.from_time = from_time
        self.to_time = to_time
        self.subject = subject

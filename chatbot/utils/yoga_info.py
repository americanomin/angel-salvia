import datetime

class YogaInfo:

    def today_info(self):
        return self._schedule()[datetime.date.today().month][self._day_of_week()]

    @staticmethod
    def _day_of_week():
        return datetime.datetime.today().weekday()

    @staticmethod
    def _schedule():
        june_plan = {
            0: [{'from': '07:00', 'to': '08:00'},
                {'from': '18:50', 'to': '19:50'},
                {'from': '20:05', 'to': '21:05'},
                {'from': '21:20', 'to': '22:20'}
                ],
            1: [{'from': '18:10', 'to': '19:10'},
                {'from': '19:20', 'to': '20:20'},
                {'from': '20:30', 'to': '21:30'},
                {'from': '21:40', 'to': '22:30'},

                ],
            2: [{'from': '07:00', 'to': '08:00'},
                {'from': '18:50', 'to': '19:50'},
                {'from': '20:05', 'to': '21:05'},
                {'from': '21:20', 'to': '22:20'}
                ],
            3: [{'from': '18:10', 'to': '19:10'},
                {'from': '19:20', 'to': '20:20'},
                {'from': '20:30', 'to': '21:30'},
                {'from': '21:40', 'to': '22:30'},
                ],
            4: [{'from': '07:00', 'to': '08:00'},
                {'from': '18:50', 'to': '19:50'},
                {'from': '20:05', 'to': '21:05'},
                {'from': '21:20', 'to': '22:20'},
                ],
            5: [
                {'from': '10:00', 'to': '11:20'},
                {'from': '11:30', 'to': '12:30'},
            ],
            6: [{'from': '10:00', 'to': '11:00'},
                {'from': '11:15', 'to': '12:15'}, ]
        }
        return {6: june_plan}

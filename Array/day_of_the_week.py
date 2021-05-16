import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekdays = {
            0:"Monday",
            1:"Tuesday",
            2:"Wednesday",
            3:"Thursday",
            4:"Friday",
            5:"Saturday",
            6:"Sunday",
        }
        day_of_the_week = datetime.datetime(year, month, day)
        return weekdays[day_of_the_week.weekday()]

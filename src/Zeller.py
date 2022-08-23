import re
from asyncio.windows_events import NULL
from unittest import result


class Zeller:
    def __init__(self, arg):
        self.inputmessage = arg

    def getDate(self):
        pattern = r'(\d{4})/([0-9]|1[0-2])/([1-2][0-9]|3[0-1]|[0-9])'
        repattern = re.compile(pattern)
        strdate = repattern.match(self.inputmessage)
        if strdate:
            date = [int(strdate[1]), int(strdate[2]), int(strdate[3])]
            if date[0]%4 == 0 and date[1] == 2 and date[2] > 29:
                return NULL
            elif date[1] == 2 and date[2] > 28:
                return NULL
            else:
                return date
        else:
            return NULL

    def calcZeller(self):
        date = self.getDate()
        if date:
            y = date[0]
            m = date[1]
            d = date[2]
            result = (y + y // 4 - y // 100 + y // 400 + (13*m + 8) // 5 + d) % 7
            return result
        else:
            return 8

    def judgeZeller(self):
        day = ["日", "月", "火", "水", "木", "金", "土"]
        mod = self.calcZeller()
        if mod == 8:
            return NULL
        else:
            result = day[mod] + "曜日"
            return result
import datetime
from TimeString import TimeString


class Lightning():
    def __init__(self):
        self.milliSparks = 0
        self.sparks = 0
        self.zaps = 0
        self.bolts = 0
        self.timeString = TimeString("0", "0", "0", "0")
        self.millisPerMilliSpark = 1318.359375

    def updateTime(self):
        time = datetime.datetime.now()
        millis = 1000 * 60 * 60 * time.hour + 1000 * 60 * time.minute + 1000 * time.second + time.microsecond / 1000
        totalMilliSparks = millis / self.millisPerMilliSpark
        totalSparks = totalMilliSparks / 16
        totalZaps = totalSparks / 16
        totalBolts = totalZaps / 16

        self.milliSparks = int(totalMilliSparks) % 16
        self.sparks = int(totalSparks) % 16
        self.zaps = int(totalZaps) % 16
        self.bolts = int(totalBolts) % 16

        self.timeString = TimeString(self.bolts, self.zaps, self.sparks, self.milliSparks)

    def getTime(self) -> str:
        self.updateTime()
        return self.timeString.__str__()
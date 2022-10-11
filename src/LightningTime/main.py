from datetime import datetime
from Lightning import Lightning 
from pythonlangutil.overload import Overload, signature

from TimeString import TimeString

class LightningTime:

    def __init__(self, startingBolt:tuple, startingZap:tuple, startingSpark:tuple) -> None:
        if (type(startingBolt[0]) != int or type(startingBolt[1]) != int or type(startingZap[0]) != int or type(startingZap[1]) != int or type(startingSpark[0]) != int or type(startingSpark[1]) != int):
            raise TypeError("Starting RGB values must be integers")
        if (startingBolt[0] > 255 or startingBolt[0] < 0 or startingBolt[1] > 255 or startingBolt[1] < 0 or startingZap[0] > 255 or startingZap[0] < 0 or startingZap[1] > 255 or startingZap[1] < 0 or startingSpark[0] > 255 or startingSpark[0] < 0 or startingSpark[1] > 255 or startingSpark[1] < 0):
            raise ValueError("Starting RGB values must be between 0 and 255")
        self.startingBoltGreen:str = hex(startingBolt[0])
        self.startingBoltBlue:str = hex(startingBolt[1])
        self.startingZapRed:str = hex(startingZap[0])
        self.startingZapBlue:str = hex(startingZap[1])
        self.startingSparkRed:str = hex(startingSpark[0])
        self.startingSparkGreen:str = hex(startingSpark[1])
    
    def getTime(self) -> str:
        currentTime = Lightning()
        return currentTime.getTime()
    
    @Overload
    @signature()
    def getBoltColor(self) -> tuple:
        currentTime = Lightning()
        currentTime.updateTime()
        return (currentTime.timeString.hour * 16 + currentTime.timeString.minute, int(self.startingBoltGreen, 16) , int(self.startingBoltBlue, 16))
    
    @getBoltColor.overload
    @signature("tuple")
    def getBoltColor(self, startingBolt:tuple) -> tuple:
        currentTime = Lightning()
        currentTime.updateTime()
        if startingBolt != None:
            if type(startingBolt[0]) != int or type(startingBolt[1]) != int:
                raise TypeError("Starting RGB values must be integers")
            if startingBolt[0] > 255 or startingBolt[0] < 0 or startingBolt[1] > 255 or startingBolt[1] < 0:
                raise ValueError("Starting RGB values must be between 0 and 255")
            return (currentTime.timeString.hour * 16 + currentTime.timeString.minute, startingBolt[0] , startingBolt[1])
        return None

    @Overload
    @signature()
    def getZapColor(self) -> tuple:
        currentTime = Lightning()
        currentTime.updateTime()
        return (int(self.startingSparkRed, 16), currentTime.timeString.minute * 16 + currentTime.timeString.second, int(self.startingZapBlue, 16))

    @getZapColor.overload
    @signature("tuple")
    def getZapColor(self, startingZap:tuple) -> tuple:
        currentTime = Lightning()
        currentTime.updateTime()
        if startingZap != None:
            if type(startingZap[0]) != int or type(startingZap[1]) != int:
                raise TypeError("Starting RGB values must be integers")
            if startingZap[0] > 255 or startingZap[0] < 0 or startingZap[1] > 255 or startingZap[1] < 0:
                raise ValueError("Starting RGB values must be between 0 and 255")
            return (startingZap[0], currentTime.timeString.minute * 16 + currentTime.timeString.second, startingZap[1])
        return None

    
    @Overload
    @signature()
    def getSparkColor(self) -> tuple:
        currentTime = Lightning()
        currentTime.updateTime()
        return (int(self.startingSparkRed, 16), int(self.startingSparkGreen, 16), currentTime.timeString.second * 16 + currentTime.timeString.millisecond)

    @getSparkColor.overload
    @signature("tuple")
    def getSparkColor(self, startingSpark:tuple) -> tuple:
        currentTime = Lightning()
        currentTime.updateTime()
        if startingSpark != None:
            if type(startingSpark[0]) != int or type(startingSpark[1]) != int:
                raise TypeError("Starting RGB values must be integers")
            if startingSpark[0] > 255 or startingSpark[0] < 0 or startingSpark[1] > 255 or startingSpark[1] < 0:
                raise ValueError("Starting RGB values must be between 0 and 255")
            return (startingSpark[0], startingSpark[1], currentTime.timeString.second * 16 + currentTime.timeString.millisecond)
        return None


    def getGradient(self) -> tuple:
        currentTime = Lightning()
        currentTime.updateTime()
        return (self.getBoltColor(), self.getZapColor(), self.getSparkColor())
    
    @staticmethod
    def toLightningTime(time: datetime) -> str:
        millis = 1000 * 60 * 60 * time.hour + 1000 * 60 * time.minute + 1000 * time.second + time.microsecond / 1000
        totalMilliSparks = millis / 1318.359375
        totalSparks = totalMilliSparks / 16
        totalZaps = totalSparks / 16
        totalBolts = totalZaps / 16

        milliSparks = int(totalMilliSparks) % 16
        sparks = int(totalSparks) % 16
        zaps = int(totalZaps) % 16
        bolts = int(totalBolts) % 16

        timeString = TimeString(bolts, zaps, sparks, milliSparks)
        return timeString

    @staticmethod
    def epochToLightningTime(epoch: int) -> str:
        return LightningTime.toLightningTime(datetime.fromtimestamp(epoch))
    


time = LightningTime((0, 0), (0, 0), (0, 0))    

print(time.getTime())
print(time.getBoltColor())
print(LightningTime.getBoltColor((0,0)))
print(time.getZapColor())
print(LightningTime.getZapColor((0,0)))
print(time.getSparkColor())
print(LightningTime.getSparkColor((0,0)))
print(time.getGradient())
print(LightningTime.toLightningTime(datetime.now()))
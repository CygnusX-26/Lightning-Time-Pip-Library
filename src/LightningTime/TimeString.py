
class TimeString:
    def __init__(self, bolts:int, zaps:int, sparks:int, milliSparks:int):
        self.hour = bolts
        self.minute = zaps
        self.second = sparks
        self.millisecond = milliSparks
        self.timeString = f'{hex(int(bolts))[2:]}~{hex(int(zaps))[2:]}~{hex(int(sparks))[2:]}|{hex(int(milliSparks))[2:]}'

    def __str__(self) -> str:
        return self.timeString

    def __repr__(self) -> str:
        return self.timeString

    def __eq__(self, other) -> bool:
        if (isinstance(other, TimeString)):
            return self.timeString == other.timeString
        else:
            return False

    def __lt__(self, other) -> bool:
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute < other.minute:
                return True
            elif self.minute == other.minute:
                if self.second < other.second:
                    return True
                elif self.second == other.second:
                    if self.millisecond < other.millisecond:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, other) -> bool:
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute > other.minute:
                return True
            elif self.minute == other.minute:
                if self.second > other.second:
                    return True
                elif self.second == other.second:
                    if self.millisecond > other.millisecond:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __le__(self, other) -> bool:
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute < other.minute:
                return True
            elif self.minute == other.minute:
                if self.second < other.second:
                    return True
                elif self.second == other.second:
                    if self.millisecond <= other.millisecond:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __ge__(self, other) -> bool:
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute > other.minute:
                return True
            elif self.minute == other.minute:
                if self.second > other.second:
                    return True
                elif self.second == other.second:
                    if self.millisecond >= other.millisecond:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
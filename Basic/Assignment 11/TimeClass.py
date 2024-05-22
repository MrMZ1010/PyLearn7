##### Mohammad Ali Mirzaei #####
class Time:

    def __init__(self, h, m, s):

        self.hours = h
        self.minutes = m
        self.seconds = s
        self.fix()

    def Sum(self, other):

        H_New = self.hours + other.hours
        M_New = self.minutes + other.minutes
        S_New = self.seconds + other.seconds
        return Time(H_New, M_New, S_New)

    def Minus(self, other):

        H_New = self.hours - other.hours
        M_New = self.minutes - other.minutes
        S_New = self.seconds - other.seconds
        return Time(H_New, M_New, S_New)

    
    def Seconds_To_Time(cls, s):
        
        Hours = s // 3600
        Minutes = (s % 3600) // 60
        Seconds = (s % 3600) % 60
        return cls(Hours, Minutes, Seconds)

    def Time_To_Seconds(self):

        return self.seconds + 60 * self.minutes + 3600 * self.hours

    def GMT_To_Tehran(self):

        H_New = self.hours + 3
        M_New = self.minutes + 30
        return Time(H_New, M_New, 00)

    def Fix(self):

        while True:
            if self.seconds >= 60:
                self.seconds -= 60
                self.minutes += 1

            if self.minutes >= 60:
                self.minutes -= 60
                self.hours += 1
            
            if self.seconds < 0:
                self.minutes -= 1
                self.seconds +=60
            
            if self.minutes < 0:
                self.hours -= 1
                self.minutes += 60
            break

    def Show(self):
        
        print(f"{self.hours}:{self.minutes}:{self.seconds}")

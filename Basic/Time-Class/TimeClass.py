##### MohammadAli Mirzaei #####

# Define a class named Time
class Time:
    
    # Define the constructor method to initialize a Time object with hours (h), minutes (m), and seconds (s)
    def __init__(self, h, m, s):
        self.hours = h
        self.minutes = m
        self.seconds = s
        # Call the fix method to adjust the time format
        self.fix()
    
    # Define a method to perform addition of two time objects
    def Sum(self, other):
        H_New = self.hours + other.hours
        M_New = self.minutes + other.minutes
        S_New = self.seconds + other.seconds
        return Time(H_New, M_New, S_New)
    
    # Define a method to perform subtraction of two time objects
    def Minus(self, other):
        H_New = self.hours - other.hours
        M_New = self.minutes - other.minutes
        S_New = self.seconds - other.seconds
        return Time(H_New, M_New, S_New)
    
    # Define a class method to convert seconds to a Time object
    @classmethod
    def Seconds_To_Time(cls, s):
        Hours = s // 3600
        Minutes = (s % 3600) // 60
        Seconds = (s % 3600) % 60
        return cls(Hours, Minutes, Seconds)
    
    # Define a method to convert a Time object to seconds
    def Time_To_Seconds(self):
        return self.seconds + 60 * self.minutes + 3600 * self.hours
    
    # Define a method to convert GMT time to Tehran time (GMT+3:30)
    def GMT_To_Tehran(self):
        H_New = self.hours + 3
        M_New = self.minutes + 30
        return Time(H_New, M_New, 0)
    
    # Define a method to fix the time format (e.g., adjusting minutes and seconds)
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
                self.seconds += 60
            if self.minutes < 0:
                self.hours -= 1
                self.minutes += 60
            break  # Exit the loop after fixing the time
        
    # Define a method to display the time in HH:MM:SS format
    def Show(self):
        print(f"{self.hours}:{self.minutes}:{self.seconds}")

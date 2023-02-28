class time_item():
    def __init__(self, rawTimeData):
        self.rawData = rawTimeData
        self.month = None
        self.date = None
        self.rawTimeData = None
        self.hour = None
        self.minute = None
        self.second = None
    
    def load_data(self):
        data = self.rawData # Load data from self.rawData
        if type(self.rawData) == str:
            data = data.split(" ") # Split data into list
            self.month = data[0] # Parse month
            self.date = data[1] # Parse date
            self.rawTimeData = data[2] # Parse raw time data
            self.load_time() # Load hour, minute, second
        elif type(self.rawData) == list:
            print(self.rawData)
            self.rawMonthData = data[0]
            self.date = data[1]
            self.rawTimeData = data[2]
            self.load_time() # Load hour, minute and second
            
            
    def load_time(self):
        if type(self.rawTimeData) == str:
            self.rawTimeData = self.rawTimeData.split(":")
            self.hour = self.rawTimeData[0]
            self.minute = self.rawTimeData[1]
            self.second = self.rawTimeData[2]
            
        elif type(self.rawTimeData) == list:
            self.hour = self.rawTimeData[0]
            self.minute = self.rawTimeData[1]
            self.second = self.rawTimeData[2]
        
class log_item():
    def __init__(self, log):
        self.rawLogData = log
        self.rawActionData = None
        self.ip = None
        self.username = None
        self.status = None
        self.type = None # Type of login
        self.rawTimeData = None
        self.time = None
        self.date = None
        

    def parse_log(self):
        rawLogData = self.rawLogData
        rawLogData = rawLogData.split(" ")
        self.rawTimeData = rawLogData[0:3]
        time = time_item(self.rawTimeData)
        time.load_data()
        self.time = f"{time.hour}.{time.minute}.{time.second}"
        self.date = f"{time.month}.{time.date}"
        self.rawActionData = rawLogData[5:]
        if self.rawActionData[0] == "Accepted":
            self.status = "Accepted"
            self.type = self.rawActionData[1]
            self.username = self.rawActionData[3]
            self.ip = self.rawActionData[5]
        
        elif self.rawActionData[0] == "Failed":
            self.status = "Failed"
            self.type = self.rawActionData[1]
            self.username = self.rawActionData[3]
            self.ip = self.rawActionData[5]
            
        elif self.rawActionData[0] == "Invalid":
            self.status = "Failed"
            self.type = "Invalid user"
            self.username = self.rawActionData[2]
            self.ip = self.rawActionData[4]
            
    def make_json(self):
        data = {"ip": self.ip, "username": self.username, "status": self.status, "type": self.type, "time": self.time, "date": self.date}
        return data
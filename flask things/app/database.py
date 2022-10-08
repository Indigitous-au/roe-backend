
class ReportItem:
    def __init__(self, time=None, platform=None, screenshot=None, username=None, suspect=None, ip=None):
        self.time = time
        self.platform = platform
        self.screenshot = screenshot
        self.username = username
        self.suspect = suspect
        self.ip = ip

#TODO put the data into the database
def to_database(data: ReportItem):
    pass
from database import ReportItem

#TODO parse the request into some kind of object for database to use
def from_request(request) -> ReportItem:
    return ReportItem(None, "someplatform", "abcde", "somebody", "someone else", "1234")
    pass
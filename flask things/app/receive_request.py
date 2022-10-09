from connect_to_database import ReportItem

#TODO figure out how to get the POST method to work
def from_request(request) -> ReportItem:
    r = ReportItem()
    if request.method == 'GET':
        arg = request.args
        time = arg.get("time")
        platform = arg.get("platform")
        ss = arg.get("screenshot")
        uname = arg.get("username")
        sus = arg.get("suspect")
        ip = arg.get("ip")
        if time is not None:
            r.time = time
        if platform is not None:
            r.platform = platform
        if ss is not None:
            r.screenshot = ss
        if uname is not None:
            r.username = uname
        if sus is not None:
            r.suspect = sus
        if ip is not None:
            r.ip = ip
    elif request.method == 'POST':
        arg = request.form
        time = arg.get("time")
        platform = arg.get("platform")
        ss = arg.get("screenshot")
        uname = arg.get("username")
        sus = arg.get("suspect")
        ip = arg.get("ip")
        if time is not None:
            r.time = time
        if platform is not None:
            r.platform = platform
        if ss is not None:
            r.screenshot = ss
        if uname is not None:
            r.username = uname
        if sus is not None:
            r.suspect = sus
        if ip is not None:
            r.ip = ip
    return r
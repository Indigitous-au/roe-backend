from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

class ReportItem:
    def __init__(self, time=None, platform=None, screenshot=None, username=None, suspect=None, ip=None):
        self.time = time
        self.platform = platform
        self.screenshot = screenshot
        self.username = username
        self.suspect = suspect
        self.ip = ip

hasura_uri = "http://hack2022.drwaryaa.com/v1/graphql"

#TODO put the data into the database - this still isn't working
def to_database(data: ReportItem):
    # get client
    transport = AIOHTTPTransport(url=hasura_uri)
    client = Client(transport=transport, fetch_schema_from_transport=True)
    # construct the query
    query = gql(
        """
        mutation insertreport {
            insert_report_one(object: {ip_address: $ip, platform: $platform, screenshot: $screenshot, username_report: $report, username_suspect: $suspect}) {
                ip_address
                platform
                screenshot
                username_report
                username_suspect
            }
        }
        """
    )
    variables = {"ip": data.ip, "platform":data.platform, "screenshot":data.screenshot, "report":data.username, "suspect":data.suspect}
    client.execute(query, variable_values=variables)
    pass
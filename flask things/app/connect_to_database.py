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

hasura_uri = "https://api.hack2022.drwaryaa.com/v1/graphql"

#TODO make it handle nulls in report
def to_database(data: ReportItem):
    # get client
    #TODO switch to non-admin authentication
    header = {'x-hasura-admin-secret':'vH646U5FSD1ATNnz809E'}
    transport = AIOHTTPTransport(url=hasura_uri, headers=header)
    client = Client(transport=transport, fetch_schema_from_transport=True)
    # construct the query
    query = gql(
        """
        mutation insertreport ($ip: String, $platform: String, $screenshot: String, $report: String, $suspect: String) {
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
from flask import Flask
import pages

app = pages.app
hostname = pages.common.hostname
port = pages.common.port
app.run(hostname, port)
import smtplib, ssl
import os
import sys


port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')
githubjob= sys.argv[1]
githubrepo = sys.argv[2]
githubwork = sys.argv[3]

message = """\
Subject: {githubjob} job of {githubrepo} had failed

{githubjob} job in worflow {githubwork} of ${githubrepo} had Failed
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME,'kanta.kumari@publicissapient.com',message)

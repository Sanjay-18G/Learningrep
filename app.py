from flask import Flask
import socket
import subprocess
import platform
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    Department =  "IT"
    user = subprocess.getoutput("whoami")
    ip = subprocess.getoutput("hostname -I")
    disk = subprocess.getoutput("df -h")
    memory = subprocess.getoutput("free -h")
    kernel = platform.release()
    os_name = platform.system()
    date = datetime.datetime.now()

    return f"""
    <h1>Linux System Information</h1>
    <pre>
Hostname : {hostname}
User     : {user}
Date     : {date}
Kernel   : {kernel}
OS       : {os_name}

IP Address
{ip}

Disk Usage
{disk}

Memory Usage
{memory}
    </pre>
    """

app.run(host="0.0.0.0", port=5000)

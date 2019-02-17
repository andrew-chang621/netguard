import sys
import os
import time
import json
import logging
import ufw_parse
import requests
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.utils.dirsnapshot import DirectorySnapshotDiff, DirectorySnapshot

PATH_TO_DIR = "/var/log"
FILENAME = "messages"
API_URL = "https://iot-alerts-service.azurewebsites.net/"

def countLines(path):
    return sum(1 for line in open(path))

def sendCallsToAPI(line):
    requests.post(url=API_URL, json=line)

if __name__ == "__main__":
    print("""\
            o    o .oPYo. ooooo .oPYo. o    o      .oo  .oPYo. ooo.   
            8b   8 8.       8   8    8 8    8     .P 8  8   `8 8  `8. 
            8`b  8 `boo     8   8      8    8    .P  8 o8YooP' 8   `8 
            8 `b 8 .P       8   8   oo 8    8   oPooo8  8   `b 8    8 
            8  `b8 8        8   8    8 8    8  .P    8  8    8 8   .P 
            8   `8 `YooP'   8   `YooP8 `YooP' .P     8  8    8 8ooo'  
            ..:::..:.....:::..:::....8 :.....:..:::::..:..:::.......::
            :::::::::::::::::::::::::8 :::::::::::::::::::::::::::::::
            :::::::::::::::::::::::::..:::::::::::::::::::::::::::::::""")
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    file_lines = open(PATH_TO_DIR + "/" + FILENAME).readlines()
    snapshot = DirectorySnapshot(PATH_TO_DIR, recursive=True)
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, PATH_TO_DIR, recursive=True)
    observer.start()

    try:
        while True:
            g = DirectorySnapshotDiff(snapshot, DirectorySnapshot(PATH_TO_DIR, recursive=True))
            for i in g.files_modified:
                print(i)
                if i == PATH_TO_DIR + "/" + FILENAME:
                    temp = open(PATH_TO_DIR + "/" + FILENAME).readlines()
                    print(len(temp) - len(file_lines))
                    if len(temp) - len(file_lines) > 10:
                        print(":::::::::::::::::::WARNING:ATTACK DETECTED:::::::::::::::::")
                        print("Shutting down all ports...")
                        os.system("sudo ufw default deny incoming")
                        last_call = [temp[-1]]
                        formatted = ufw_parse.format_log_data(last_call)
                        sendCallsToAPI({
                            "hostIP": "172.20.10.4",
                            "sampleLog": formatted
                        })
                        # print(formatted["SRC"])
                        print(formatted)
                        sys.exit("Closing run.py.")
                    file_lines = temp
            snapshot = DirectorySnapshot(PATH_TO_DIR, recursive=True)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

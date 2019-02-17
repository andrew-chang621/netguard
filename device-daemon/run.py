import sys
import os
import time
import logging
import ufw_parse
import requests
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.utils.dirsnapshot import DirectorySnapshotDiff, DirectorySnapshot

PATH_TO_DIR = "/var/log"
FILENAME = "messages"
API_URL = "____"

def countLines(path):
    return sum(1 for line in open(path))

def sendCallsToAPI(data):
    requests.post(url=API_URL, params=data)

if __name__ == "__main__":
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
                        last_call = temp[-1]
                        formatted = ufw_parse.format_log_data(last_call)
                        sendCallsToAPI({
                            "hostIP": formatted["SRC"],
                            "sampleLog": formatted[0]
                        })
                        print(formatted["SRC"])
                        print(formatted[0])
                        sys.exit("Closing run.py.")
                    file_lines = temp
            snapshot = DirectorySnapshot(PATH_TO_DIR, recursive=True)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

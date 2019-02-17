import sys
import os
import time
import logging
import ufw_parse
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.utils.dirsnapshot import DirectorySnapshotDiff, DirectorySnapshot

PATH_TO_DIR = "/var/log"
FILENAME = "messages"

def countLines(path):
    return sum(1 for line in open(path))

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
                        last_10 = temp[-10:]
                        formatted_calls = ufw_parse.format_log_data(last_10)
                        print(formatted_calls)
                    file_lines = temp
            snapshot = DirectorySnapshot(PATH_TO_DIR, recursive=True)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

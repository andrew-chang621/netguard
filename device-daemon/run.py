import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.utils.dirsnapshot import DirectorySnapshotDiff, DirectorySnapshot

PATH_TO_DIR = "###"
FILENAME = "###"

def countLines(path):
    return sum(1 for line in open(path))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    line_count = countLines(PATH_TO_DIR + "/" + FILENAME)
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
                    temp = countLines(PATH_TO_DIR + "/" + FILENAME)
                    print(temp - line_count)
                    line_count = temp
            snapshot = DirectorySnapshot(PATH_TO_DIR, recursive=True)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

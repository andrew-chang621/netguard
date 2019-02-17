import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.utils.dirsnapshot import DirectorySnapshotDiff, DirectorySnapshot

PATH_TO_DIR = "###"
FILENAME = "###"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = PATH_TO_DIR
    line_count = sum(1 for line in open(path + "/" + FILENAME))
    snapshot = DirectorySnapshot(path, recursive=True)
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            g = DirectorySnapshotDiff(snapshot, DirectorySnapshot(path, recursive=True))
            for i in g.files_modified:
                print(i)
                if i == path + "/" + FILENAME:
                    temp = sum(1 for line in open(path + "/" + FILENAME))
                    print(temp - line_count)
                    line_count = temp
            snapshot = DirectorySnapshot(path, recursive=True)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

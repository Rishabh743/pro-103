import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir="c:/"
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(event)
        print(event.src_path,"has been created")
    def on_deleted(self, event):
        print(event)
        print(event.src_path,"has been deleted")

# Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


while True:
    time.sleep(2)
    print("running...")

    
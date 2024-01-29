# Import necessary libraries for file system monitoring

import os 
import shutil 
import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 

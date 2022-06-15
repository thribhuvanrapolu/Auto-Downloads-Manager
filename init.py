import shutil #for moving files
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def log(file,location):
    Log_Format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename = "logfile.log",
                        filemode = "a",
                        format = Log_Format, 
                        level = logging.INFO)

    logger = logging.getLogger()

    logger.info("\" %s \" :saved file in %s",file,location)



class Watcher:

    def __init__(self, directory="/home/anakin513/Downloads", handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=False)
        self.observer.start()
        print("\nWatcher Running in {}/\n".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")
        logging.info('Finished')


class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        if event.src_path.endswith((".mp4",".avi",".drc",".mng",".TS",".M2TS",".MTS",".mkv",".webm",".mpg",".mpeg",".mpe",".mpv",".ogg",".ogv",".m4p",".m4v",".wmv",".mov",".qt",".flv",".swf",".avchd",".vob",".yuv")):
            original=event.src_path
            filename=event.src_path[25:]
            target="/home/anakin513/Videos"+filename
            shutil.move(original,target)
            log(filename,"Videos")
        elif event.src_path.endswith((".3gp",".aa",".aac",".aax",".act",".aiff",".alac",".amr",".ape",".au",".awb",".dss",".dvf",".flac",".gsm",".iklax",".ivs",".m4a",".m4b",".m4p",".mmf",".mp3",".mpc",".msv",".nmf",".ogg",".oga",".mogg",".opus",".ra",".rm",".raw",".rf64",".sln",".tta",".voc",".vox",".wav",".wma",".wv",".webm",".8svx",".cda")):
            original=event.src_path
            filename=event.src_path[25:]
            target="/home/anakin513/Music"+filename
            shutil.move(original,target)
            log(filename,"Music")
        elif event.src_path.endswith((".pdf",".docx","xlsx",".doc",".odt",".xls",".ods",".ppt",".pptx",".txt")):
            original=event.src_path
            filename=event.src_path[25:]
            target="/home/anakin513/Documents"+filename
            shutil.move(original,target)
            log(filename,"Documents")
        elif event.src_path.endswith((".jpg",".jpeg",".png","tiff",".psd",".webp",".cr2",".crw",".nef",".pef",".gif")):
            original=event.src_path
            filename=event.src_path[25:]
            target="/home/anakin513/Pictures"+filename
            shutil.move(original,target)
            log(filename,"Pictures")
        


if __name__=="__main__":
    w = Watcher("/home/anakin513/Downloads", MyHandler())
    w.run()

from pathlib import Path
import shutil
from threading import Thread

def shutil_copy(src, dcr):
    src = Path(src)
    dcr = Path(dcr)
    for item in src.rglob("*"):
        if item.is_file() and item.suffix == ".jpg":
            shutil.copy(item, Path(dcr/"jpg"))

        elif item.is_file() and item.suffix == ".png":
            shutil.copy(item, Path(dcr/"png"))

        elif item.is_file() and item.suffix == ".svg":
            shutil.copy(item, Path(dcr/"svg"))
if __name__ == "__main__":

    thread = Thread(target= shutil_copy, args=("picture","dist"))
    thread.start()
    # shutil_copy("picture", "dist")
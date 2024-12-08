import os.path

CUR_FILE = os.path.abspath(__file__)

CUR_DIR = os.path.dirname(CUR_FILE)

TMP_DIR = os.path.join(CUR_DIR, "temp")

if not os.path.exists("temp"):
    os.mkdir("temp")
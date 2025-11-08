from pathlib import Path
from dataclasses import dataclass
from multiprocessing import Pool
import subprocess
import tqdm
import os

@dataclass
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def run(task):
    
    p = subprocess.run(task, check=True, text=True, capture_output=True)
    print(p.stderr)
    print(p.stdout)



def main():

    os.environ["TESSDATA_PREFIX"] = "C:\\Users\\leucht\\Videos\\tessdata_best\\" # Path tessdata_best as instructed by pgsrip
    root = Path("Y:\\jellyfin\\shows\\") # Path to directory of .mkv files that you want to convert the subtitles of

    convertables = []

    for path in root.rglob("*"):

        #print(path)
        if not path.is_dir() and ".mkv" in path.name: 

            convertables.append(f"pgsrip \"{path.absolute()}\"")

    #print(convertables)

    pool = Pool()
    for _ in tqdm.tqdm(pool.imap_unordered(run, convertables), total=len(convertables)):
        pass

    print(bcolors.OKGREEN + "Finished" + bcolors.ENDC)


if __name__=="__main__":
    main()
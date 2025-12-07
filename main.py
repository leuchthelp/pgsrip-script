from pathlib import Path
from multiprocessing import Pool
import logging
import subprocess
import tqdm
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def run(task):
    
    logger.info(bcolors.OKCYAN + f"current on: {task}" + bcolors.ENDC)
    p = subprocess.run(["pgsrip", task], check=True, text=True, capture_output=True)
    logger.debug(p.stderr)
    logger.debug(p.stdout)
    logger.info(bcolors.OKGREEN + f"finished: {task}" + bcolors.ENDC)


def main():
    ### SETUP HERE ###
    os.environ["TESSDATA_PREFIX"] = "C:\\Users\\leucht\\Videos\\tessdata_best\\" # Path tessdata_best as instructed by pgsrip
    root = Path("Z:\\jellyfin\\") # Path to directory of .mkv files that you want to convert the subtitles of

    convertibles = []

    for path in root.rglob("*"):

        logger.debug(path)
        if not path.is_dir() and ".mkv" in path.name: 

            convertibles.append(path.absolute())

    logger.debug(convertibles)

    pool = Pool()
    for _ in tqdm.tqdm(pool.imap_unordered(run, convertibles), total=len(convertibles)):
        pass

    logger.info(bcolors.OKGREEN + "Finished" + bcolors.ENDC)


if __name__=="__main__":
    main()
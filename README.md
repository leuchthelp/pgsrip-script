# pgsrip-script

This is a simple script to batch execute [pgsrip](https://github.com/ratoaq2/pgsrip). pgsrip should already be capable for scanning through subfolders and ripping files in batches, however I could not get my system fully saturated with just the standard options. So I build this simple script to burn through more media at once.


## Installation

### pgsrip dependencies (copied from original repo)

MKVToolNix:
```sh
[Linux/WSL - Ubuntu/Debian]
sudo apt-get install mkvtoolnix

[Windows/Chocolatey]
choco install mkvtoolnix
```

tesseract:

PPA is used to install latest tesseract 5.x. Skip PPA repository if you decide to stick with latest official Debian/Ubuntu package
```sh
[Linux/WSL - Ubuntu/Debian]
sudo add-apt-repository ppa:alex-p/tesseract-ocr5
sudo apt update
sudo apt-get install tesseract-ocr

[Windows/Chocolatey]
choco install tesseract-ocr
```

tessdata:
```sh
git clone https://github.com/tesseract-ocr/tessdata_best.git

# Usually the script recommends setting TESSDATA_PREFIX to indicate the OCR data
export TESSDATA_PREFIX=~/tessdata_best
# The script should handle that if you go in and edit the relevant line
```


### Installation for script
```sh
python -m venv .venv

# Linux & MacOS
source .venv/bin/activate

# Windows
.\.venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt
```

Now you should be almost ready to run the script. 

Head on to the `main.py` and change the last 2 lines as you see fit. Those being the location of the OCR data from the `tessdata_best` git repo you cloned earlier on `Line 31` and the location of the directory where your media files reside on `Line 32`.

WARNING: The script will run with the max number of thread available on your machine. If you wish to change this behavior add `processes=NUMBER_OF_THREADS` to `Line 45: Pool(processes=NUMBER_OF_THREADS)`.

Afterwards simply run `python main.py` and the script will do the rest.

Huge thank you to [ratoaq2](https://github.com/ratoaq2) for the awesome [pgsrip](https://github.com/ratoaq2/pgsrip) module.
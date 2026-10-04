# how to install it

### 1. Go to your project folder

git clone https://github.com/abderrahmane-blk/youtube-downloader.git
cd youtube-downloader

### 2. Create the virtual environment

#### on linux

python3 -m venv venv

#### on windows

python -m venv venv

### 3. Activate the virtual environment

#### on linux

source venv/bin/activate

#### on windows

venv/scripts/activate

### 4. Install dependencies

pip install yt-dlp pyside6

### 5. Run the script

python main.py

## if the downloaded video is mute or is split from its sound into 2 files

then you just have to install `ffmpeg` on your system

#### for linux

pip install ffmpeg

#### it is not hard for windows , just look for it

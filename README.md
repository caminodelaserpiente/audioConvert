# Text Convert 🗣️📝
Tool for Convert Speech to Text


## Functionalities ⚙️
1. Convert Speech from .mp3 to .txt file
2. Convert Speech from .mp3 to .sbv file
3. Convert Speech from .mp4 to .txt file
4. Convert Speech from .mp4 to .sbv file


## Install 🔧
1. Installl ffmpeg on Anaconda
    ```consol
    conda install -c conda-forge ffmpeg
    ```

    Or Installl ffmpeg on GNU/Linux | Debian/Ubuntu
    ```consol
    sudo apt update && sudo apt install ffmpeg
    ```

2. Clone this repo.<br>
    ```consol
    git clone https://github.com/caminodelaserpiente/audioConvert
    ```

3. Change the working directory.<br>
    ```consol
    cd audioConvert
    ```

4. Install the requirements.<br>
    ```consol
    pip install -r requirements.txt
    ```


## Play 🎮
```consol
python3 main.py
```

            _                _  _           ____                                   _   
           / \    _   _   __| |(_)  ___    / ___|  ___   _ __  __   __  ___  _ __ | |_ 
          / _ \  | | | | / _` || | / _ \  | |     / _ \ | '_ \ \ \ / / / _ \| '__|| __|
         / ___ \ | |_| || (_| || || (_) | | |___ | (_) || | | | \ V / |  __/| |   | |_ 
        /_/   \_\ \__,_| \__,_||_| \___/   \____| \___/ |_| |_|  \_/   \___||_|    \__| 

    
        ----------------------------------------------------
            - Select type file to convert. (e.g. >>> 1)
                [0] bye
                [1] .mp3
                [2] .mp4
    Select option.
    >>> 1

        ----------------------------------------------------
            - Select option to convert. (e.g. >>> 2)
                [1] Text transcription (.txt)
                [2] Creation of subtitles (.sbv)
    Select option.
    >>> 2

    Enter path file .mp3.
    >>> test_files/audio.mp3

    [OK 1/2] Converting audio to subtitles...
    [OK 2/2] Your file has been created: ./output/subtitles/audio.sbv

 
## Saved data 💾
* The .mp3 files are saved in the `./output/mp3` folder  📁
* The .txt are saved in the `./output/textxs` folder  📁
* The .sbv are saved in the `./output/subtitles` folder  📁

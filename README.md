Vid2GifWeb
==========
Proof of concept for converting videos to gifs through uploading videos online to a webserver.

Setup
=====
Requirements
------------
 - [Python](https://www.python.org)
    - On Ubuntu: `sudo apt-get install python` 
 - [Pip](http://pip.readthedocs.org)
    - On Ubuntu: `sudo apt-get install python-pip`
 - [Virtualenv](http://www.virtualenv.org)
    - On Ubuntu: `sudo pip install virtualenv`
 - [ffmpeg](http://www.ffmpeg.org/)
    - On Ubuntu
        1. `pip install PIL --allow-external PIL --allow-unverified PIL`
        2. `sudo add-apt-repository ppa:jon-severinsson/ffmpeg`
        3. `sudo apt-get install ffmpeg`

Ubuntu Instructions
-------------------
  1. `cd [vid2gifweb_directory]`
  2. `sudo pip install Flask`
  3. `sudo pip install moviepy`
  4. `python vid2gifweb.py` and enjoy!
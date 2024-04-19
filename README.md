# Stalibov Kg23

## Name
Automatized media merger

## Description
This is a Windows compatible script that merges .mp4 and .jpg files into a single .mp4 file with .mp3 background
audio. It takes at most the first 6 seconds of every .mp4 file, shows every .jpg file for 2 seconds and
puts a single given .mp3 file into an audiotrack for the resulting .mp4 file.

## Installation
To get this project on your PC you need to clone this repository to your PC. Execute this prompt in 
PowerShell or cmd:<br> git clone https://git.miem.hse.ru/smtalibov1/stalibov-kg23.git <br><br>
Make sure that you have ImageMagick and FFmpeg installed and that you have them in your PATH variables<br><br>
The last step is to install necessary python libraries. Navigate to the directory of the application using
'cd' prompt in your command line. Execute this prompt in PowerShell or cmd:<br>pip install -r requirements.txt<br><br>
Now that you've performed all these steps you are ready to use this application!

## Usage
To use this application, you need to add all .jpg and .mp4 files you want in your video and add a single .mp3
file that you want to hear as an audiotrack of the final video inside the "Source" folder. Then you need to
navigate to the directory of the application using 'cd' prompt in your command line. Then execute
this prompt:<br>python main.py<br><br>
The resulting video in a form of an .mp4 file is waiting for you in the "Output" folder!

## License
MIT

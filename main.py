import os, sys
os.system("pip install moviepy")
os.system("pip install moviepy --upgrade")
os.system('cls || clear')
from moviepy.editor import VideoFileClip
import speech_recognition as sr
print("""
      
      
      
      Convert the movie to the sound simply!


       coded By @black_nicola(TELEGRAM)
      
      
      
    """)
try:
    video_path = sys.argv[1]
    output_path = sys.argv[2]
except:
    print('Use with --> python main.py VIDEO.MP4 OUTPUT.MP3')
try:
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_path)
except:
    print('''
Error! FFmpeg is not installed on your system!
    Please read it: https://www.wikihow.com/Install-FFmpeg-on-Windows''')
    sys.exit()
print('Ok!')

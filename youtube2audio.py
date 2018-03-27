import os
import time

target = "C:\\tmp\\MP3"

print("""
                         ________________
                    .-- _______________ .|
                  _____F________       T:]
                 F              Y .-\"\"\"\"-.
                 \[ \\:.-.=''     ]'        `c
                 \[              :           a
                 \[ A            :   .aa.     )
                 \[ S            ]   8()8     J
 _a:f___________ \[ C        88  ]   `9P'     s  ____________________
                 \[ I        88  ]           v                    __
                 \[ I        88  ]         .'                    (__.`
.._              L______________J `-.__.-'      _..aaaaaaaaa.._     \\`.
8888b.                                       .888888888P888888888`   |]
)88888)      .---c--c---c -,-,-,--a         c8888888a`_'_'a8888888a  |]
d8888P)    .'  .  .   .   n / /  / '       /`a88888888888888888889'  |/
88P\"_/   .'  .' .'  .'_  / n n  / '        `. `\"Y888888888888PP\"'./
---'  ,.'  ======== /_/=====   ( .           `--.____________.--'
      _\\______________________/_

      ++++++++++++++++++++++++++++++++++
      + Welcome to YouTube Downloader! +
      ++++++++++++++++++++++++++++++++++
""")

anstypeconversion = 0
while 1:
    anstypeconversion = input("\n Convert YouTube links to (1) Video or (2) Audio format? ")
    if int(anstypeconversion) in [1, 2]:
        break

if int(anstypeconversion) == 1:  # convert to video
    downloadcmd = "youtube-dl -ci -o \"%(playlist_index)s-%(title)s.%(ext)s\" "
    messageusr = 'Successful downloaded and converted to video in'
elif int(anstypeconversion) == 2:  # convert to audio
    downloadcmd = "youtube-dl -ci --extract-audio --audio-format mp3 -o \"%(playlist_index)s-%(title)s.%(ext)s\" "
    messageusr = 'Successful downloaded and converted to MP3 in'

urlink = input("\nYoutube URL: ")

while len(urlink) > 0:
    cmdline = downloadcmd + urlink
    print('Running:')
    if os.system(cmdline) == 0:
        print(messageusr, target)
    else:
        print('Download FAILED')

    urlink = input("\n (Just press ENTER if you do not want to download any other YouTube link). \nYoutube URL: ")

import os
import time
import getpass

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, 'sugar.exe')
congrats_path = os.path.join(desktop_path, 'FLAG.txt')

ascii_art = '''
             ________________________________________________
            /                                                \
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:\> S3CT10n31{G07_c1ph3r5?}           |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'

'''

congrats_message = ascii_art + '\nCongratulations, you found the hidden file!\n\n' \
    + 'Thanks for playing! We hope you enjoyed this little game.\n' \
    + '-------------------------------------------------------------\n'

while True:
    if os.path.isfile(file_path):
        while True:
            time.sleep(5)
            if not os.path.isfile(file_path):
                with open(congrats_path, 'w') as f:
                    f.write(congrats_message)
                break
        break
    time.sleep(5)

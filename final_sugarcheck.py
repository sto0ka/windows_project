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
    file_exists = os.path.isfile(file_path)
    if file_exists:
        while True:
            time.sleep(5)
            file_exists = os.path.isfile(file_path)
            if not file_exists:
                with open(congrats_path, 'w') as f:
                    f.write(congrats_message)
                break
    time.sleep(5)
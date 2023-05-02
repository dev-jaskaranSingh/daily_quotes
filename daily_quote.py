import requests
import os
import random
import time
from datetime import date

# check if required packages are installed and install them if necessary
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

# set the working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

while True:
    # fetch a random quote using an API
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        data = response.json()
        quote = f'{data["content"]} - {data["author"]}'
    else:
        quote = 'Error fetching quote.'
    
    # create a new file with the current date as the filename
    filename = date.today().strftime('%Y-%m-%d') + '.md'
    with open(filename, 'a') as f:
        # append the quote to the file
        f.write(f'* {quote}\n')

    # add the new file to the staging area
    os.system(f'git add {filename}')

    # commit the changes with a timestamped message
    message = f'Daily quote commit on {date.today().strftime("%Y-%m-%d %H:%M:%S")}'
    os.system(f'git commit -m "{message}"')

    # push the changes to the remote repository
    os.system('git push origin master')

    # wait 10 minutes before running the script again
    time.sleep(600)

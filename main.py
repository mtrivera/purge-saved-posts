import praw
import urllib.request

def is_connected(host='https://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def main():
    if not is_connected():
        print('No internet connection. Script cannot run while offline.')
        return
    print('Success! Internet connection established.')

main()
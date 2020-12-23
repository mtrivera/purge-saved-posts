import praw
import urllib.request

def is_connected(host='https://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def sub_exists(r, sub):
    try:
        r.subreddits.search_by_name(sub, exact=True)
        return True
    except:
        return False

def read_file(r, file):
    dict = {}
    with open(file, "r") as infile:
        line = infile.readline()
        while line:
            sub = line.strip('\n')
            if sub_exists(r, sub):
                dict[sub] = 0
            line = infile.readline()
    return dict

def get_saved_post_count(r, sub):
    counts = []
    for post in r.user.me().saved(limit=None):
        if post.subreddit == sub:
            counts.append(post)
    return len(counts)

def main():
    if not is_connected():
        print('No internet connection. Script cannot run while offline.')
        return
    print('Success! Internet connection established.')

    reddit = praw.Reddit("purge")

    subs = read_file(reddit, "subreddits.txt")



main()
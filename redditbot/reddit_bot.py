import praw
import config
import time
import os
import requests

def bot_login():
    print "Logging in..."
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "futurecsstudent11's joke comment responder")
    print "Logged in!"
    return r

def run_bot(r, comments_replied_to):
    print "Replying to 10 comments..."

    for comment in r.subreddit('norristesting').comments(limit = 10):
        if "!joke" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print "String with \"!joke\" found in comment " + comment.id

            comment_reply = "You requested a Chuck Norries joke! Here it is:\n\n"

            joke = requests.get('http://api.icndb.com/jokes/random').json()['value']['joke']

            comment_reply += ">" + joke

            comment_reply += "\n\nThis joke came from [ICNDb.com](http://icndb.com)."

            comment.reply(comment_reply)
            print "Replied to comment " + comment.id

            #comment.reply("[Look](https://i.redditmedia.com/K34UbwACP2UEF-Y5HiXlktKWTc9P9RkKx5U_OG--3S4.jpg?s=9c8b94dc4fc7c724100b1d3eddc64773) at this picture of a cute dog!")
            #print "Replied ty comment " + commenrebt.id

            comments_replied_to.append(comment.id)

    print comments_replied_to

    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)
    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print comments_replied_to

while True:
    run_bot(r, comments_replied_to)

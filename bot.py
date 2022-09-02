import praw
import pyjokes
from praw.models import MoreComments

# Instantiate an instance of PRAW's Reddit class
reddit = praw.Reddit(client_id = 'T6u5hwv_zwez-RrT33NCaA', 
                    client_secret = 'B--LwQpjQDaDCjMmmhkcPIsy61GrMQ', 
                    username = 'badger-bot-2022', 
                    password = 'kOV7Nc5#m',
                    user_agent = 'badger-bot-2022')

# Functionality:
# 1. If a comment is made on a hot post in r/CFB that contains the word 'Minnesota' or 'Wisconsin', reply to the comment "Paul Bunyan's Axe is ours! On Wisconsin!"
# 2. If a comment is made in a new r/test subreddit post that contains the word 'joke' or 'Joke', reply with a randomly generated joke.

CFB_subreddit = reddit.subreddit('CFB')

# # Iterate through the last 10 hot posts that are not stickied in CFB_subreddit
for submission in CFB_subreddit.hot(limit= 10):
    # If the submission is stickied, skip it
    if not submission.stickied:
        # Iterate through all comments in the submission
        for comment in submission.comments:
            # If the comment is a MoreComments object, skip it REF: https://praw.readthedocs.io/en/latest/tutorials/comments.html
            if isinstance(comment, MoreComments):
                continue
            # If the comment contains the word 'Minnesota', reply to the comment
            if comment.author != 'badger-bot-2022':
                if 'Minnesota' in comment.body:
                    comment.reply(body ="Did somebody say Minnesota? Paul Bunyan's Axe is ours! On Wisconsin!")
                # If the comment contains the word 'Wisconsin', reply to the comment
                elif 'Wisconsin' in comment.body:
                    comment.reply(body="Did somebody say Wisconsin? Paul Bunyan's Axe is ours for the taking! On Wisconsin!")

test_subreddit = reddit.subreddit('test')

for submission in test_subreddit.new(limit = 10):
    if not submission.stickied:
        for comment in submission.comments:
            if isinstance(comment, MoreComments):
                continue
            if comment.author != 'badger-bot-2022':
                if 'joke' in comment.body or 'Joke' in comment.body :
                    # Generate a joke
                    joke = pyjokes.get_joke(language = "en", category = "neutral")
                    my_comment = comment.reply(body = "Did somebody say joke?\n\nAllow me to assist: " + joke)
            


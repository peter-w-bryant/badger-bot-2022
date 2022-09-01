import praw
# Instantiate an instance of PRAW's Reddit class
reddit = praw.Reddit(client_id = 'T6u5hwv_zwez-RrT33NCaA', 
                    client_secret = 'B--LwQpjQDaDCjMmmhkcPIsy61GrMQ', 
                    username = 'badger-bot-2022', 
                    password = 'kOV7Nc5#m',
                    user_agent = 'badger-bot-2022')

# submission = reddit.subreddit("test").submit("Test Submission", url="https://reddit.com")

# submission.reply(body="Test Reply")

# for moderator in reddit.subreddit("uwmadison").moderator():
#     print(moderator)

# Repy to the weekly top comment for the subreddit "CFB" with "Go Badgers! On Wisconsin!"
for comment in reddit.subreddit("CFB").top(time_filter ="week"):
    comment.reply(body ="Go Badgers! On Wisconsin!")
    break

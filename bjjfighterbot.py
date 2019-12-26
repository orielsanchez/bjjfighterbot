# BJJFightersBot
# coding: utf-8

import praw
import config
import csv
import time
import requests

# Retrieve heroku env variables
reddit_username = os.environ['reddit_username']
reddit_password = os.environ['reddit_password']
client_id = os.environ['client_id']
client_secret = os.environ['client_secret']
target_sub = 'bjj'
target_word = '!bjjfighterbot'

# reddit api login
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=reddit_password,
                     username=reddit_username,
                     user_agent=f'{target_word}bot by (/u/iamjacksheart)')
print('Logged in')

# subreddits you want your bot to live in
subreddit = reddit.subreddit(target_sub)


with open('./fighters.csv', 'r') as f:
    reader = csv.reader(f)
    result = {}
    for row in reader:
        result[row[0]] = row[1:]

print('Opened fighters.csv')

start_time = int(time.time())
print('Start time is: ' +
      str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))))

for comment in reddit.subreddit(target_sub).stream.comments():
    if start_time < int(comment.created_utc):
        body = comment.body
        if target_word in body:
            query = body.replace(f'{target_word} ', '')
            print('Found target word... ' +
                  str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))))
            if query in result:
                print('Processing request...')
                message = query + ': ' + \
                    str(result.get(query)[1]) + \
                    "\n\n" + str(result.get(query)[0])
                comment.reply(message)
                print(message)
            else:
                comment.reply(
                    f'Sorry. There was no result for {query}. I am case-sensitive.')
                print('No result')

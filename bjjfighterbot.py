# BJJFightersBot
# coding: utf-8

import praw
import config
import csv
import time
import requests

# declare config variables
CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
PASSWORD = config.PASSWORD
USERNAME = config.USERNAME
target_sub = 'bjj'
target_word = '!bjjfighterbot'

# reddit api login
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     password=PASSWORD,
                     username=USERNAME,
                     user_agent=f'{target_word}bot by (/u/iamjacksheart)')

# subreddits you want your bot to live in
subreddit = reddit.subreddit(target_sub)


with open('./fighters.csv', 'r') as f:
    reader = csv.reader(f)
    result = {}
    for row in reader:
        result[row[0]] = row[1:]

start_time = int(time.time())

for comment in reddit.subreddit(target_sub).stream.comments():
    if start_time < int(comment.created_utc):
        body = comment.body
        if target_word in body:
            query = body.replace(f'{target_word} ', '')
            if query in result:
                message = query + ': ' + \
                    str(result.get(query)[1]) + \
                    "\n\n" + str(result.get(query)[0])
                comment.reply(message)
                print(message)
            else:
                comment.reply(
                    f'Sorry. There was no result for {query}. I am case-sensitive.')
                print('No result')

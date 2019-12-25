# BJJFightersBot

a reddit bot for r/bjj to pull up any fighter's bjjheroes page

## How to use this bot

As of now, on the r/bjj subreddit, comment with !bjjfighterbot following by a bjj practicioners name, and this little guy will pull up their bjjhero page and a short summary.

Example: !bjjfighterbot Marcelo Garcia

Currently case-sensitive and only accepts full names. Nicknames are being worked on.

#

## 5 things to remember when making your bot

### 1. Read the Reddit [Bottiquete](https://www.reddit.com/wiki/bottiquette)!

There are lots of restrictions on Reddit Bots, so read the Reddit Bottiquete when planning your project. Essentially, make sure your bot is useful, and does not spam or comment when it is not invoked.

### 2. Target specific subreddits that would benefit the most from your bot.

To prevent your bot from being banned, allow it to only function in specific subreddits. Lots of times, bots are banned because they are spamming communities or are being invoked out-of-context. Limiting functionality to certain communities can prevent this from happening.

### 3. Make a separate Reddit account for your bot!

Reddit bots are registered as 'scripts' running under a Reddit user account. So, when setting up your `config.py` file, first create a new Reddit account, and use those credentials. Also, remember not to share or upload the `config.py` file on Github!

### 4. Use pushshift.io to collect Reddit data.

If you want to scan all of reddit, using just PRAW can be very slow. Luckily, [pushshift.io](http://pushshift.io) has a [clean API](https://github.com/pushshift/api) that allows you to search all of Reddit. Use the `after` keyword in the query to find results from after the last time the bot was invoked so the query runs quickly!

### 5. You can automate the bot using Heroku!

This is something I plan to do in the upcoming days.

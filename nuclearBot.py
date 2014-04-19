""""
This scans for stuff I'm interested in on reddit and messages me so I can join
the discussion. 

Based on tutorial program for PRAW:
See https://github.com/praw-dev/praw/wiki/Writing-A-Bot/
"""

import time

import praw

r = praw.Reddit(user_agent='/u/Nuclear_Info_Bot by whatisnuclear.com')
r.login()
already_done = []

thWords = ['thorium', 'molten salt reactor', ' msr ',' lftr ','terrapower','traveling wave reactor',
           ' twr ']
subreddits = ['energy','technology','worldnews','NuclearPower','politics','todayilearned',
              'explainlikeimfive']
while True:
    for srName in subreddits:
        print('Scanning '+srName)
        subreddit = r.get_subreddit(srName)
        for submission in subreddit.get_hot(limit=30):
            op_text = submission.title.lower()
            has_th = any(string in op_text for string in thWords)
            if submission.id not in already_done and has_th:
                msg = u'Th thread alert: [{0}]({1})'.format(submission.title, submission.short_link)
                print(submission.title)
                r.user.send_message('whatisnuclear', msg)
                already_done.append(submission.id)
            time.sleep(3)
    time.sleep(1800)
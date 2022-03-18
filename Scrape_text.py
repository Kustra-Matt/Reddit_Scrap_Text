#!/Users/kuskus/.conda/envs/Reddit_scrape/bin/python
#Loading packages
import praw
import os
os.chdir('/Users/kuskus/PycharmProjects/Reddit_scrape')
from twilio.rest import Client
reddit = praw.Reddit(client_id='INSERTID', client_secret='INSERTCLIEN', user_agent='lawinfo')


new_posts = reddit.subreddit('lawschooladmissions').new(limit=30)
post_ids=list()
with open('posts.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        post_ids.append(currentPlace)
post_dict=dict()
schools=["UCLA","Berk","Mich","Duke","UC"]
for post in new_posts:
    if post.id in post_ids:
        continue
    elif any(x in post.title for x in schools) or any(x in post.selftext for x in schools):
        post_dict[post.title]= post.url
        post_ids.append(post.id)
        #print(post.url)
        #print(post.selftext)
        #print(post.id)

if len(post_ids)>30:
    post_ids=post_ids[29:]
with open('posts.txt', 'w') as filehandle:
    for post in post_ids:
        filehandle.write('%s\n' % post)

strdict = " , ".join(("{} = {}".format(*i) for i in post_dict.items()))
#Texting part
if bool(strdict):
    client=Client('XXXX','XXXx')

    client.messages.create(to="+PHONENUMBER",from_="+PHONENUMBER",body=strdict)
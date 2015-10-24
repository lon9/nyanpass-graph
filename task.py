from twitter import Twitter 
import os
import re
import matplotlib.pyplot as plt
import numpy as np

def makeNyanpassList(tweets):
	pattern = re.compile(r"[0-9]+")
	l = []
	for tweet in reversed(tweets):
		matched = pattern.findall(tweet._json['text'])
		l.append(int(matched[0]))
	return np.array(l)

def createWeekList():
	import datetime
	now = datetime.datetime.now()
	weekList = []
	for i in reversed(range(7)):
		weekList.append((now - datetime.timedelta(days=i)).strftime("%m/%d"))
	return weekList

if __name__ == "__main__":
	consumerKey = os.environ.get("CONSUMER_KEY")
	consumerSecret = os.environ.get("CONSUMER_SECRET")
	accessToken = os.environ.get("ACCESS_TOKEN")
	accessTokenSecret = os.environ.get("ACCESS_TOKEN_SECRET")
	userId = os.environ.get("USER_ID")
	twitter = Twitter(consumerKey, consumerSecret, accessToken, accessTokenSecret)
	tweets = twitter.getTweet(userId=userId, num=7)

	# Getting nyanpass list
	nList = makeNyanpassList(tweets)
	weekList = createWeekList()
	
	x = np.arange(7)
	plt.bar(x, nList, align="center")
	plt.title('Nyanpass counter')
	plt.xlabel('Day')
	plt.ylabel('Nyanpass')
	plt.xticks(x, weekList)
	plt.savefig("nyanpass.png")
	# plt.show()
	
	twitter.postPicture("nyanpass.png", weekList)

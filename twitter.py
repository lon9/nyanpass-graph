import tweepy

class Twitter:
	def __init__(self, consumerKey, consumerSecret, accessToken, accessTokenSecret):
		auth=tweepy.OAuthHandler(consumerKey, consumerSecret)
		auth.set_access_token(accessToken, accessTokenSecret)
		self.api=tweepy.API(auth)

	def getMe(self):
		return self.api.me()

	def getTweet(self, userId, **args):
		if 'num' in args:
			timeline = self.api.user_timeline(user_id=userId, count=args['num'])
			return timeline
		return self.api.user_timeline(id=userId)

	def postPicture(self, path, rang):
		text = '{0}〜{1}のにゃんぱす'.format(rang[0], rang[6])
		self.api.update_with_media(path, status=text)

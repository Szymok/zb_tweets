import sys, tweepy
import private

#authenthication function

def twitter_auth():
    try:
        consumer_key = private.consumer_key
        consumer_secret_key = private.consumer_secret_key
        access_token = private.access_token
        access_secret_token = private.access_secret_token
    except KeyError:
        sys.stderr.write('Brak zmiennej środowiskowej TWITTER_*\n')
        sys.exit(1)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_secret_token)

    return auth

def get_twitter_client():
    auth = twitter_auth()
    client = tweepy.API(auth, wait_on_rate_limit=True)

    return client

#Konto Zbigniewa Bońka: 'BoniekZibi'

if __name__ == '__main__':
    user = input('Podaj użytkownika: ')
    client = get_twitter_client()
    for status in tweepy.Cursor(client.user_timeline, screen_name=user).items():
        print(status.text)

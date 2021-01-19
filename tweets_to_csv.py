import tweepy
import csv
import zibi_tweets

#Tweet object - https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object

def tweets_to_csv(screen_name):
    #autoryzacja danych z Twittera
    auth = zibi_tweets.twitter_auth()

    #inicjalizacja tweepy
    api = tweepy.API(auth)

    #pusta lista do zbierania tweetów
    all_tweets = []

    #ostatnie tweety, wykorzystując user_timeline możemy ściągnąć 200 tweetów
    last_tweets = api.user_timeline(screen_name = screen_name, count=200)

    #tweety
    all_tweets.extend(last_tweets)

    # zapisujemy id najstarszego tweeta - 1
    oldest = all_tweets[-1].id - 1

    # pętla zapisujące tweety aż do wyczerpania twweetów
    while len(last_tweets) > 0:
        print(f'Zapisuje tweet {oldest}')

        #max_id, aby zapobiec duplikatom
        last_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        #nowe tweety
        all_tweets.extend(last_tweets)

        # aktualizacja id najstarszego tweeta - 1
        oldest = all_tweets[-1].id - 1

        print(f'Zapisano dotychczas {len(all_tweets)} tweetów')

    # zapis tweetów do 2 wymiarowej matrycy
    output_tweets = [[tweet.id_str, tweet.created_at, tweet.text, tweet.source, tweet.in_reply_to_user_id_str,
                      tweet.retweet_count, tweet.favorite_count] for tweet in all_tweets]

    # zapis do pliku csv
    with open(f'new_{screen_name}_tweets_2.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id_str', 'created_at', 'text', 'source', 'in_reply_to_user_id_str',
                         'retweet_count', 'favorite_count'])
        writer.writerows(output_tweets)

if __name__ == '__main__':
	#Konto Zbigniewa Bońka: 'BoniekZibi'
	tweets_to_csv("BoniekZibi")
import tweepy
import settings
import json


#設定
POST_TIMES=40
client = tweepy.Client(
    consumer_key=settings.CONSUMER_KEY,
    consumer_secret=settings.CONSUMER_SECRET,
    access_token=settings.ACCESS_TOKEN,
    access_token_secret=settings.ACCESS_TOKEN_SECRET,
)

#tweet_content
def _tweet_content(id, tag, title, content):
    content = {
        'id': id,
        'tag': tag,
        'title': title,
        'content': content,
    }
    return content

#post
def post_tweet(post_times):
    for i in range(post_times):
        i += 1
        if i==1:
            tweet = str(
                json.dumps(
                    _tweet_content(id=i, tag='#コンテンツ入門2023', title='にょき', content='jsonでtweet書いてみたw'),
                    indent=4,
                    ensure_ascii=False
                )
            )
        elif i==10:
            tweet = str(
                json.dumps(
                    _tweet_content(id=i, tag='#コンテンツ入門2023', title='にょき', content='やっと10tweet'),
                    indent=4,
                    ensure_ascii=False
                )
            )
        elif i==20:
            tweet = str(
                json.dumps(
                    _tweet_content(id=i, tag='#コンテンツ入門2023', title='にょき', content='折り返し地点!'),
                    indent=4,
                    ensure_ascii=False
                )
            )
        elif i==30:
            tweet = str(
                json.dumps(
                    _tweet_content(id=i, tag='#コンテンツ入門2023', title='にょき', content='残り10tweet!'),
                    indent=4,
                    ensure_ascii=False
                )
            )
        elif i==40:
            tweet = json.dumps(
                    _tweet_content(id=i, tag='#コンテンツ入門2023', title='にょき', content='40tweetは草'),
                    indent=4,
                    ensure_ascii=False
                )
        else:
            content=f'にょき×{i}'
            tweet = json.dumps(
                    _tweet_content(id=i, tag='#コンテンツ入門2023', title='にょき', content=content),
                    indent=4,
                    ensure_ascii=False
            )
        #post
        client.create_tweet(text=tweet)

#実行
exec = post_tweet(post_times=POST_TIMES)

#jsonに書き込み
def wright_json(post_times):
    tweet_list = []
    for i in range(post_times):
        i += 1
        if i==1:
            tweet = _tweet_content(id=i, tag='#コンテンツ入門2023', title='にょき', content='プレーンテキストでjson書いてみたw')
        elif i==10:
            tweet = _tweet_content(id=i, tag='#コンテンツ入門2023', title='にょき', content='やっと10tweet')
        elif i==20:
            tweet = _tweet_content(id=i, tag='#コンテンツ入門2023', title='にょき', content='折り返し地点!')
        elif i==30:
            tweet = _tweet_content(id=i, tag='#コンテンツ入門2023', title='にょき', content='残り10tweet!')
        elif i==40:
            tweet = _tweet_content(id=i, tag='#コンテンツ入門2023', title='にょき', content='40tweetは草')
        else:
            content=f'にょき×{i}'
            tweet = _tweet_content(id=i, tag='#コンテンツ入門2023', title='にょき', content=content)
        tweet_list.append(tweet)
    result = {'data': tweet_list}
    return result

#書き込み
data = wright_json(post_times=POST_TIMES)
with open('./data.json', 'w') as f:
    json.dump(data, f, indent=4)

'''
source: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference
'''

import requests, json, yaml
    

def get_bearer_token():
    with open('config.yml') as f:    
        config_vars = yaml.safe_load(f)
        
    return config_vars['bearer_token']


def get_twitter_api_request(uri):
    bearer = get_bearer_token()
    headers = {'Authorization': f'Bearer {bearer}'}
    api_base_url = "https://api.twitter.com/2"        
    uri = f'{api_base_url}/{uri}'    
    response = requests.get(uri, headers=headers)
    print(f'GET {uri} ...')

    return response       


def request_tweet(tweet_id):    
    uri = f'tweets/{tweet_id}'     
    response = get_twitter_api_request(uri)    
    print(f'Status Code: {response.status_code}')    
    response_json = response.json() 
    
    return response_json


def search_tweets():
    uri = f'tweets/search/recent?query=from:TwitterDev&tweet.fields=created_at&expansions=author_id&user.fields=created_at'
    response = get_twitter_api_request(uri)    
    print(f'Status Code: {response.status_code}')    
    response_json = response.json() 
    
    return response_json
     



#tweet = request_tweet(1461460720445440013)  
#print(tweet)   

tweets = search_tweets()
print(tweets)    
    


    






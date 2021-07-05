# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 19:51:03 2021

@author: sachin
"""
import requests
import pandas as pd


class Reddit:
    def __init__(self, client_id, secret_token, username, password):
        # first create authentication object
        auth = requests.auth.HTTPBasicAuth(client_id, secret_token)
        # build login dictionary
        login = {'grant_type': 'password',
                 'username': username,
                 'password': password}
        # setup header info (incl description of API)
        headers = {'User-Agent': 'MyApp/0.0.1'}
        # send request for OAuth token
        res = requests.post(f'https://www.reddit.com/api/v1/access_token',auth=auth, data=login, headers=headers)
        # pull auth bearer token from response
        token = res.json()['access_token']
        # add authorization to headers dictionary
        headers['Authorization'] = f'bearer {token}'
        # add headers dict to internal attributes
        self.headers = headers
        # and api
        self.api = 'https://oauth.reddit.com'

    def get_new(self, subreddit, iters):
        # initialize dataframe to store data
        df = pd.DataFrame()
        # initialize parameters dictionary
        params = {'limit': 100}
        # iterate through several times to make sure we get all the data available
        for i in range(iters):
            # make request
            res = requests.get(f'{self.api}/r/{subreddit}/new',
                               headers=self.headers,
                               params=params)
            # check that we returned something (if not we reached end)
            if len(res.json()['data']['children']) == 0:
                print('No more found')
                return df
            # iterate through each thread recieved
            for thread in res.json()['data']['children']:
                # add info to dataframe
                df = df.append({
                    'id': thread['data']['name'],
                    'created_utc': int(thread['data']['created_utc']),
                    'subreddit': thread['data']['subreddit'],
                    'title': thread['data']['title'],
                    'selftext': thread['data']['selftext'],
                    'upvote_ratio': thread['data']['upvote_ratio'],
                    'ups': thread['data']['ups'],
                    'downs': thread['data']['downs'],
                    'score': thread['data']['score']
                }, ignore_index=True)
            # get earliest ID
            earliest = df['id'].iloc[len(df)-1]
            # add earliest ID to params
            params['after'] = earliest
        return df
    
   

import { backendLookup } from '../lookup'


export function apiTweetCreate(newTweet, callback) {
    backendLookup('POST', '/tweets/create/', callback, {content: newTweet});
};

export function apiTweetAction(tweet_id, action, callback) {
    const data = {
        id: tweet_id,
        action: action
    }
    backendLookup('POST', '/tweets/action/', callback, data);
};

//Tweet Lookup function
export function apiTweetList(callback) {
    backendLookup('GET', '/tweets/', callback);
};
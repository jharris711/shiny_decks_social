import { backendLookup } from '../lookup'


export function apiTweetCreate(newTweet, callback) {
    backendLookup('POST', '/tweets/create/', callback, {content: newTweet});
};

//Tweet Lookup function
export function apiTweetList(callback) {
    backendLookup('GET', '/tweets/', callback);
};
#code appropriated from https://marcobonzanini.com/2015/06/16/mining-twitter-data-with-python-and-js-part-7-geolocation-and-interactive-maps/
#also useful: http://socialmedia-class.org/twittertutorial.html
#Twitter json field guide: https://dev.twitter.com/overview/api/tweets AND https://dev.twitter.com/overview/api/entities-in-twitter-objects

#this is to get locations, media URL, device used IF they geotagged and IF they posted media 

import json

with open('stream_feesmustfall_part2.json', 'r') as f: #did this for stream_feesmustfall_part?.json, ? = part 1 and 2
    arr = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        tweet = json.loads(line)
        if 'text' in tweet:
            if 'media' in tweet['entities'] and tweet['place']:
                json_feature = {
                        "name": tweet['user']['name'],
                        "screen_name": tweet['user']['screen_name'],
                        "text": tweet['text'],
                        "city name": tweet['place']['name'],
                        "place name": tweet['place']['full_name'],
                        "place type": tweet['place']['place_type'],
                        "country": tweet['place']['country'],
                        "source": tweet['source'],
                        "media": tweet['entities']['media'],
                        #"media url": tweet['entities']['media']['media_url'],
                        #"media type": tweet['entities']['media']['type'],
                }
                arr['features'].append(json_feature)
 
# Save geo data
with open('media_place_and_source_2.json', 'w') as fout: #again, saved this separately
    fout.write(json.dumps(arr, indent=4))
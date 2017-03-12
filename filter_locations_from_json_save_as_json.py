#code appropriated from https://marcobonzanini.com/2015/06/16/mining-twitter-data-with-python-and-js-part-7-geolocation-and-interactive-maps/
#also useful: http://socialmedia-class.org/twittertutorial.html
#Twitter json field guide: https://dev.twitter.com/overview/api/tweets AND https://dev.twitter.com/overview/api/entities-in-twitter-objects

#this is to get locations of tweets that aren't necessarily geocoded and put into json file

import json

with open('stream_feesmustfall_part1.json', 'r') as f: #did this for stream_feesmustfall_part?.json, ? = part 1 and 2
    place_list = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        tweet = json.loads(line)
        if 'text' in tweet:
            if tweet['place']:
                json_feature = {
                        "city name": tweet['place']['name'],
                        "place name": tweet['place']['full_name'],
                        "place type": tweet['place']['place_type'],
                        "country": tweet['place']['country'],
                }
                place_list['features'].append(json_feature)
 
# Save geo data
with open('geo_data_FMF_locations_1.json', 'w') as fout: #again, saved this separately
    fout.write(json.dumps(place_list, indent=4))
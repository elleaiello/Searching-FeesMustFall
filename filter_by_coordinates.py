#code appropriated from https://marcobonzanini.com/2015/06/16/mining-twitter-data-with-python-and-js-part-7-geolocation-and-interactive-maps/
#also useful: http://socialmedia-class.org/twittertutorial.html
#Twitter json field guide: https://dev.twitter.com/overview/api/tweets AND https://dev.twitter.com/overview/api/entities-in-twitter-objects

#LATEST CODE for creating geoJson file that includes name, tweet, location

import json

with open('stream_feesmustfall_part1.json', 'r') as f: #did this for stream_feesmustfall_part?.json, ? = part 1 and 2
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        tweet = json.loads(line)
        if 'text' in tweet:
            if tweet['coordinates']:
                geo_json_feature = {
                    "type": "Feature",
                    "geometry": tweet['coordinates'],
                    "properties": {
                        "name": tweet['user']['name'],
                        "screen_name": tweet['user']['screen_name'],
                        "text": tweet['text'],                        
                        "city name": tweet['place']['name'],
                        "place name": tweet['place']['full_name'],
                        "place type": tweet['place']['place_type'],
                        "country": tweet['place']['country'],
                        "source": tweet['source'],
                    }
                }
                geo_data['features'].append(geo_json_feature)
 
# Save geo data
with open('geo_data_FMF_name_place_and_source_1.json', 'w') as fout: #again, saved this separately
    fout.write(json.dumps(geo_data, indent=4))
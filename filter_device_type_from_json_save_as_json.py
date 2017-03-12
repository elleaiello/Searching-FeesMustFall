#code appropriated from https://marcobonzanini.com/2015/06/16/mining-twitter-data-with-python-and-js-part-7-geolocation-and-interactive-maps/
#also useful: http://socialmedia-class.org/twittertutorial.html
#Twitter json field guide: https://dev.twitter.com/overview/api/tweets AND https://dev.twitter.com/overview/api/entities-in-twitter-objects


# for finding device type even if no coordinates --> puts it in JSON format

import json

with open('stream_feesmustfall_part1.json', 'r') as f: #did this for stream_feesmustfall_part?.json, ? = part 1 and 2
    data_json = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        tweet = json.loads(line)
        if 'text' in tweet:
                json_feature = {
                    #"type": "Feature",
                    #"name": tweet['user']['name'],
                    #"@screen_name": tweet['user']['screen_name'],
                    #"text": tweet['text'],                        
                    "source": tweet['source'],
                }
                data_json['features'].append(json_feature)
 
# Save geo data
with open('json_data_FMF_device_1.json', 'w') as fout: #again, saved this separately
    fout.write(json.dumps(data_json, indent=4))
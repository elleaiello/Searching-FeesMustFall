#code appropriated from https://marcobonzanini.com/2015/06/16/mining-twitter-data-with-python-and-js-part-7-geolocation-and-interactive-maps/
#also useful: http://socialmedia-class.org/twittertutorial.html
#Twitter json field guide: https://dev.twitter.com/overview/api/tweets AND https://dev.twitter.com/overview/api/entities-in-twitter-objects


# for finding device type even if no coordinates in tweet. puts in CSV format.

import json

with open('stream_feesmustfall_part1.json', 'r', encoding='utf-8') as f: #did this for stream_feesmustfall_part?.json, ? = part 1 and 2
    data_csv = []
    for line in f:
        tweet = json.loads(line)
        if 'text' in tweet:                       
            created_at = tweet['created_at']
            data_csv.append(created_at)

#convert array to string
data_string = "\n".join(data_csv)

# Save array data (converted into string) in file
file = open("date_1.csv", "w", encoding='utf-8') #change between 1 and 2 when appropriate
file.write(data_string)
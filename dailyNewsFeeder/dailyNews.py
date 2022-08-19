import yaml
from feeders import rss,coinGecko


#Parsing yaml file (convert it into one big python dictionary)
with open('settings/sources.yaml' , mode="rb") as file :
    fileContent = yaml.safe_load(file)

for el in fileContent :
    if fileContent[el]['type'] == 'rss' :
        rss.rssFeeder(fileContent[el]['url'], fileContent[el]['deth'])
    elif fileContent[el]['type'] == 'coingecko' :
        coinGecko.coinGeckoCheck(fileContent[el]['token'],fileContent[el]['posses'],fileContent[el]['vs'])



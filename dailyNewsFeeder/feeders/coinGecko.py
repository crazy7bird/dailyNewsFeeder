import requests
import yaml



def coinGeckoCheck(token : str , posses = 0, vs_currency = 'eur') :
    infos = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={token}&vs_currencies={vs_currency}&include_24hr_change=true")
    print(token,':',infos.json()[token][vs_currency], vs_currency)
    print(infos.json()[token][vs_currency] * posses, vs_currency , '(', posses,token,')')
    print(round(infos.json()[token][f'{vs_currency}_24h_change'],2),'% 24H')
    print()


if __name__ == '__main__':
    coinGeckoCheck('turtlecoin' , 10_000_000, 'eur')

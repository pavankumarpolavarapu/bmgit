from typing import List, Dict
from tinydb import TinyDB, Query
import requests
import json
data_str = {} 
# url = 'https://mg.bharatmatrimony.com/search/matches/<ID>'
url = 'https://srch.bharatmatrimony.com/search/viewed-matches/<ID>'


def build_post_data(i):
    data_str['APPVERSIONCODE']='0'
    data_str['SORT']='1'
    data_str['REFINE']='0'
    data_str['APPVERSION']='6.1'
    data_str['ID']='<ID>'
    data_str['LIMIT']='20'
    data_str['BLOCKED']='1'
    data_str['IGNORED']='1'
    data_str['START']=i
    data_str['SHORTLISTED']='0'
    data_str['VIEWED']='0'
    data_str['CONTACTED']='0'
    data_str['VIEWEDAPITIMESTAMP']=''
    data_str['PRIMETAG']=''
    data_str['ANCESTRALSTATE']=''
    data_str['APPTYPE']='300'
    data_str['Lang']='en'
    data_str['ENCID']=''
    data_str['TOKENID']=''
    data_str['APIVERSION']='1.2'
    data_str['TIMECREATED']=''
    data_str['UIVERSION']='NEW'
    data_str['WEBPFLAG']='0'


    
    return data_str 

def get_data(i):
    headers = { 'Host': 'srch.bharatmatrimony.com',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Content-Length': '779',
                'Origin': 'https://matches.telugumatrimony.com',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Referer': 'https://matches.telugumatrimony.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'cross-site'
            }
    res = requests.post(url, headers=headers, data=build_post_data(i)) 
    return res

def main():
    db = TinyDB('matches.json')
    with open('res.txt', 'a') as f:
        for i in range(0, 132):
            print("loading first {} entries".format(i*20)) 
            res = get_data(i*20)
            try:
                if res.status_code != 200:
                    f.write(res.text)
                    res = get_data(i*20)
                if res.status_code == 200:
                    data = json.loads(res.text)
                    for item in data["SEARCHRES"]["PROFILE"]:
                        db.insert(item)
            except ValueError:
                print("failed to load {}".format(data))
            except KeyError:
                print("failed with response {}".format(data))

if __name__ == '__main__':
    exit(main())

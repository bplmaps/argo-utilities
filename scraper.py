#!/usr/bin/env python3

import argparse
from sys import stdin
# import sickle
from os import mkdir
import datetime
import requests
import pandas as pd
import time

parser = argparse.ArgumentParser(description='Scrape metadta from collections and create an export')
parser.add_argument('-c', '--collection', required=True, dest='collection')

args = parser.parse_args()




    # for line in input:
    #     oai_identifier = get_oai_identifier(line.strip())
    #     print (oai_identifier)

    #     s = sickle.Sickle(oai_base)
    #     record = s.GetRecord(identifier=oai_identifier, metadataPrefix='oai_dc')

    #     with open(f'{dirname}/{oai_identifier}.xml','wb') as dumpFile:
    #         dumpFile.write(record.raw.encode('utf8'))

    #     with open(f'{dirname}/{oai_identifier}_manifest.txt','w') as dumpFile2:
    #         dumpFile2.write(get_iiif_manifest(line.strip()))


if __name__ == "__main__":

    dirname = f'{args.collection}_{datetime.datetime.now()}'
    mkdir(dirname)

    if args.collection == "clements":

        dfs = []
        
        for line in stdin:

            u = line.strip()

            print(u)

            exploded_url = u.split('/')
            iiif_manifest_url = f'https://quod.lib.umich.edu/cgi/i/image/api/search/wcl1ic:{exploded_url[-2].split("-")[1]}'

            r = requests.get(iiif_manifest_url)
            j = r.json()

            m = {}
            for f in j["sequences"][0]["canvases"][0]["metadata"]:
                m[f["label"]] = f["value"]

            m["iiif_manifest_url"] = iiif_manifest_url

            dfs.append(pd.DataFrame([m]))
            time.sleep(1.01)


        all_df = pd.concat(dfs)
        all_df.to_csv(f'{dirname}/exported.csv')

        # oai_base = 'https://quod.lib.umich.edu/cgi/o/oai/oai'
        # def get_oai_identifier(collection_uri):
        #     exploded_url = collection_uri.split('/')
        #     return f'IC-{exploded_url[-3].upper()}-{exploded_url[-2].upper()}%5D{exploded_url[-1].upper()}'

        # def get_iiif_manifest(collection_uri):
        #     exploded_url = collection_uri.split('/')
        #     return f'https://quod.lib.umich.edu/cgi/i/image/api/search/wcl1ic:{exploded_url[-2].split("-")[1]}'
    
    else:
        print("Invalid collection flag")
        exit()




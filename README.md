# Collections tools for ARGO partner harvest

# scraper.py

### Requirements

* [Sickle](https://sickle.readthedocs.io/en/latest/tutorial.html)

### Usage

Pass a collections URI or list of collections URIs through `stdin` and set the `-c` flag to the collection name.

Examples:

`./scraper.py -c clements < http://quod.lib.umich.edu/w/wcl1ic/x-975/wcl001069`
`./scraper.py -c clements < clements-test-list.txt`

Expected result: timestamped directory of XML files containing OAI metadata export, plus TXT files with IIIF Manifest URL for each identifier.
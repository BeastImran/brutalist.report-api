from helpers.fetch import BrutalistFetch
from pprint import pprint
from datetime import date

brutalist_fetch = BrutalistFetch()

print(brutalist_fetch.fetch_sources(topic="https://brutalist.report/topic/tech?"))

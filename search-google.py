from googleapiclient.discovery import build
import pprint
import json

my_api_key = "AIzaSyCCKhGJcXiM-kJONEo3WK0fzL8JEd7zu-w"
my_cse_id = " 000435949175518162357:bozmt59629a"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **
                             kwargs, searchType="image").execute()
    return res


results = google_search(
    'stackoverflow site:en.wikipedia.org', my_api_key, my_cse_id, num=20)

with open("data.json", 'w+') as fd:
    json.dump(results, fd)

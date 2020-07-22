import Auth

class Search(object):
    def __init__(self):
        auth = Auth
    def search_for_track(self,query):
        sp = auth.spotify_auth()
        result = sp.search(query)
        return result

y = Search()
print(y.search_for_track("Kygo"))
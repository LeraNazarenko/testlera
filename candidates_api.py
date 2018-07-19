import requests


class CandidatesApi():

    def get_all_candidates(self):
        r = requests.get('http://qainterview.cogniance.com/candidates')
        return r

    def add_new_candidate(self, name, position):
        name = 'name'
        position = 'position'
        p = requests.post('http://qainterview.cogniance.com/candidates', json={'name': 'lera', 'position': 'qa'})
        return p

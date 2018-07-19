import candidates_api
import json

def test_get_all_candidates():
    api = candidates_api.CandidatesApi()
    response = api.get_all_candidates()
    assert response.status_code == 200


def test_add_new_candidate():
    api = candidates_api.CandidatesApi()
    response = api.add_new_candidate('lera', 'qa')
    assert response.status_code == 201
    json_response = json.loads(response.content)
    assert json_response['candidate']['id'] > 0
    assert json_response['candidate']['name'] == 'lera'
    assert json_response['candidate']['position'] == 'qa'



test_get_all_candidates()
test_add_new_candidate()


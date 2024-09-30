from project0.extract import extract_incidents

def test_extract():
    with open('resources/test_incidents_extract', 'r') as f:
        expected_data = f.read().split('},')

    expected_keys = {"DateTime", "IncidentNumber", "Location", "Nature", "IncidentType"}

    actual_data = extract_incidents('resources/test_incidents_download.pdf')
    
    assert len(actual_data)>0
    assert isinstance(actual_data,list)
    assert set(actual_data[0].keys()) == expected_keys
    assert len(actual_data) == len(expected_data)





    

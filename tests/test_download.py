from project0.download import fetch_incidents

def test_download():
    url ="https://www.normanok.gov/sites/default/files/documents/2024-09/2024-09-01_daily_incident_summary.pdf"
    
    fetch_incidents(url)

    with open('resources/incident.pdf', 'rb') as f:
        actual_data = f.read()
    
    with open('resources/test_incidents_download.pdf', 'rb') as f:
        expected_data = f.read()

    assert actual_data == expected_data






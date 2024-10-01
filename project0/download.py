import urllib.request

def fetch_incidents(url):
    """
    Fetch the PDF data from the provided URL.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)

    with open('resources/incidents.pdf', 'wb') as f:
        f.write(response.read())
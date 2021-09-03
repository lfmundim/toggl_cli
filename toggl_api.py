import requests
import base64
import urllib

base_url = 'https://api.track.toggl.com/api/v8'
zero_hour_BRT = 'T00:00:00-03:00'

def get_base_headers():
    return {
        "content-type": "application/json",
        "Accept-Charset": "UTF-8"
    }

def create_authorization(token):
    auth_header = token + ':api_token'
    byte_array = auth_header.encode()
    base64_bytes = base64.b64encode(byte_array)
    base64_key = base64_bytes.decode()
    return base64_key

def get_time_entries_from_period(start, end, authorization):
    # TODO: replace with REGEX
    # Add Time as API Requests
    if len(start) == 10:
        start = start + zero_hour_BRT
    if len(end) == 10:
        end = end + zero_hour_BRT

    query_params = { 'start_date' : start, 'end_date' : end}
    encoded_params = urllib.parse.urlencode(query_params)

    url = base_url +'/time_entries?' + encoded_params
    headers = get_base_headers()
    headers["Authorization"] = "Basic " + authorization

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to retrieve timesheet from toggl: Status ' + str(response.status_code))
        return None

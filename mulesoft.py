import requests, json


def catalog():
    # get credentials
    username = input("Username: ")
    password = input("Password: ")

    # get token
    url = 'https://anypoint.mulesoft.com/accounts/login'
    payload = f'username={username}&password={password}'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    token_response = requests.post(url, headers=headers, data=payload)
    token = json.loads(token_response.text).get('access_token')


    # get orgids
    url = 'https://anypoint.mulesoft.com/accounts/api/me'
    headers = {'Authorization': 'Bearer ' + token}
    orgid_response = requests.get(url, headers=headers)
    orgids = {}
    for index, item in enumerate(json.loads(orgid_response.text).get('user').get('memberOfOrganizations')):
        orgids[item.get('id')] = item.get('name')


if __name__ == '__main__':
    catalog()

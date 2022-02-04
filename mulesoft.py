import getpass
import json
import requests


def catalog():
    # initialize csv
    csv = 'Organization;Environment;API Name;State;Version;Runtime\n'

    # get credentials
    username = input("Username: ")
    password = getpass.getpass("Password: ")

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

    # get envids
    for orgid, org_name in orgids.items():
        url = f'https://anypoint.mulesoft.com/accounts/api/organizations/{orgid}/environments'
        headers = {'Authorization': 'Bearer ' + token}
        envids_response = requests.get(url, headers=headers)
        envids = {}
        for index, item in enumerate([i.get('id') for i in json.loads(envids_response.text).get('data')]):
            envids[item] = [i.get('name') for i in json.loads(envids_response.text).get('data')][index]

        # get applications
        for envid, env_name in envids.items():
            url = 'https://anypoint.mulesoft.com/cloudhub/api/applications'
            headers = {'authorization': 'Bearer ' + token,
                       'x-anypnt-env-id': envid,
                       'x-anypnt-org-id': orgid}
            application_response = requests.get(url=url, headers=headers)
            for i in json.loads(application_response.text):
                csv += f'{org_name};{env_name};{i.get("domain")};{i.get("status")};{i.get("muleVersion")};{i.get("muleVersion")[0]}\n'

    # write csv to file
    with open("./API_catalog.csv", "w") as file:
        file.write(csv)

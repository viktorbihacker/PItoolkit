import getpass
import json
import os

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


def secure():
    HIGHLIGHT = '\033[7m'
    END = '\033[0m'

    direction = input(f"{HIGHLIGHT}e{END}ncrypt {HIGHLIGHT}d{END}ecrypt: ").lower()
    direction = 'encrypt' if direction == 'e' else 'decrypt' if direction == 'd' else quit()

    file_or_string = input(f"{HIGHLIGHT}f{END}ile {HIGHLIGHT}s{END}tring: ").lower()
    file_or_string = 'file' if file_or_string == 'f' else 'string' if file_or_string == 's' else quit()

    string_or_filename = "properties_encrypted.yaml properties_decrypted.yaml" if direction == "decrypt" else "properties_decrypted.yaml properties_encrypted.yaml"

    if file_or_string == "string":
        string_or_filename = input("String to be encoded: ") if direction == 'encrypt' else input(
            "String to be decoded: ")

    algorithm = input(
        f"{HIGHLIGHT}A{END}ES {HIGHLIGHT}B{END}lowfish(default) {HIGHLIGHT}D{END}ES D{HIGHLIGHT}E{END}Sede {HIGHLIGHT}R{END}C2 R{HIGHLIGHT}C{END}A: ").lower()
    algorithm = 'AES' if algorithm == 'a' else 'Blowfish' if algorithm == 'b' or algorithm == '' else 'DES' if algorithm == 'd' else 'DESede' if algorithm == 'e' else 'RC2' if algorithm == 'r' else 'RCA' if algorithm == 'c' else quit()

    mode = input(f"{HIGHLIGHT}C{END}BC(default) C{HIGHLIGHT}F{END}B {HIGHLIGHT}E{END}CB {HIGHLIGHT}O{END}FB: ").lower()
    mode = 'CBC' if mode == 'c' or mode == '' else 'CFB' if mode == 'f' else 'ECB' if mode == 'e' else 'OFB' if mode == 'o' else quit()
    os.system(
        f'java -cp secure-properties-tool.jar com.mulesoft.tools.SecurePropertiesTool {file_or_string} {direction} {algorithm} {mode} mulesoft {string_or_filename}')

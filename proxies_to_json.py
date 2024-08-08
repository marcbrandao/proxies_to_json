import os
import json
import dotenv
import hashlib
import requests

dotenv.load_dotenv()

# Credentials are pulled from a local .env file
USERNAME = os.getenv("MLXUSERNAME")
PASSWORD = os.getenv("MLXPASSWORD")

# Insert Your FolderID here
FOLDERID = "91f042e6-xxx-4e1f-adee-5eed6bb47d60"

# Insert your profile_ids.json filepath here
LIST_PATH = "C:/.../files/pid_list.json"

# Paste your string values manually:
LIST_MANUAL = [
    "95f6d02c-xxxx-47c4-b1d4-369801f2a37c",
    "48da90d8-xxxx-40a2-8ccb-2d9e7e3eaebb",
    "e2f9d96a-xxxx-4439-ae74-10beda6bf109",
    "fffca377-xxxx-495e-a408-3a98716e14ea",
    "f3559ca3-xxxx-479c-8a8a-c4b831e8f78b",
    "1c1e09dc-xxxx-4495-979b-7cb805a3a8a1",
    "a66ba910-xxxx-48ac-a6d1-615f996b3a1d",
    "f17140f4-xxxx-47c5-96d5-1b9fd184203b",
    "0a505d93-xxxx-4ba9-bd25-d37bf8bb168d"]



# API-Related Objects
LOCALHOST  = "http://127.0.0.1"
MLX_BASE   = "https://api.multilogin.com"
LAUNCHERV1 = "https://launcher.mlx.yt:45001/api/v1"                 
HEADERS    = {'Accept': 'application/json','Content-Type': 'application/json'}

# Login Function
def signin() -> str:
    payload = {
        'email': USERNAME,
        'password': hashlib.md5(PASSWORD.encode()).hexdigest()}

    r = requests.post(f'{MLX_BASE}/user/signin', json=payload)
    
    if r.status_code != 200:
        print(f'\nError during login: {r.text}\n')
        return ""
    else:
        response = r.json()['data']
        token = response['token']
        return token
    
# Search Profiles called "TempName": recently created by the Bulk Create function.
def profile_search():
    url = "https://api.multilogin.com/profile/search"
    body = {
        "is_removed": False,        # Do you wish to search for removed profiles? True/False
        "limit": 100,               # How many profile results do you wish to get?
        "offset": 0,                # Check MLX Documenter page for a full parameter breakdown
        "search_text": "",         
        "storage_type": "all", 
        "order_by": "created_at",
        "sort": "asc"
    }
    response = requests.request("POST", url, headers=HEADERS, json=body)
    resp_json = json.loads(response.content)
    return resp_json

# Obtain a list of ProfileIDs retrieved by the Profile Search endpoint 
def get_profile_ids():
    profile_list = profile_search()
    
    if profile_list['data']['total_count'] == 0:
        print("No more profiles found: error in response or end of task.")
        return []
    else:
        if profile_list and 'data' in profile_list and 'profiles' in profile_list['data']:
            profile_ids = [profile['id'] for profile in profile_list['data']['profiles']]
            return profile_ids
        else:
            print("Error - Please check Get Profile IDs function.")

# Use Profile Metas endpoint to get the Proxy information registrered.
def search_proxy_metas(option_call):
    url = "https://api.multilogin.com/profile/metas"
    
    if option_call == "1":
        payload = json.dumps({"ids": LIST_MANUAL}) 
    
    elif option_call == "2":
        payload = json.dumps({"ids": get_profile_ids()}) 
    
    elif option_call == "3":
        with open(LIST_PATH, 'r') as file:
            proxies = json.load(file)
        payload = json.dumps({"ids": proxies})
    else:
        print("Invalid option. Restart.")
        return

    response = requests.request("POST", url, headers=HEADERS, data=payload)
    response_object = response.text
    extracted_data = json.loads(response_object) # Full Profile Metas object (not only proxies)
    
    query_result = []
    
    for profile in extracted_data['data']['profiles']:
        proxy_metas = profile['parameters']['proxy']
        query_result.append(proxy_metas)
    
    proxy_json = json.dumps(query_result, indent=4)
    print(proxy_json)
    
    # Write the JSON with results
    with open('proxy_credentials.json', 'w') as json_file:
        json_file.write(proxy_json)

    print(f'Total of {len(query_result)} proxies were saved on proxy_credentials.json \n')

# Main function
def main():
    token = signin()
    if token:
        HEADERS.update({"Authorization": f'Bearer {token}'})
    else:
        print("Failed to sign in.")

    option_call = input(
        "\n\n Select method to find proxy list: \n  (1) from PATH \n  (2) from Profile Search \n  (3) Manual List (line 17) \n Write Selection: \n   ")
    
    search_proxy_metas(option_call)

if __name__ == "__main__":
    main()
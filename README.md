## Export all proxy credentials from a list of Profile IDs
Generate .JSON proxy credentials lists from any set of Multilogin X browser Profile IDs. 

## Features
- Supports ProfileID lists from inline pasting, file path specification or result objects from Profile Search endpoint.
- Allows integration of Multilogin Proxy credentials into other profiles or tools, such as Multilogin Desktop.
- Quick generation of proxy credentials lists as .JSON objects.
- Facilitates Profile Transfer requests

## Installation
- Python environment
- Packages:
  - os
  - json
  - dotenv
  - hashlib
  - requests

## Usage
  1. Download proxies_to_json.py and .env and paste on your folder.
  2. Add your information:
    • Make sure the credentials are in .env. 
    • Add a Workspace Folder ID (line 14).
    • Check your Profile ID list source (path, text or search).
    • Ensure the matching fields have correct information.
    • When using profile_search, change the function parameters.
  3. Open your script on a Terminal.
  4. Select the desired input option.
  5. Check the results in the file proxy_credentials.json stored on the folder.

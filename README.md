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
  2. Make sure the credentials are in .env.
  3. Add your information:	
  		3.1	Add a Workspace Folder ID (line 14).
			3.2 Check your Profile ID list source (path, text or search).
			3.3 When using profile_search, change the function parameters.	
	 		3.4 Ensure the matching fields have correct information.
  4. Open your script on a Terminal.
  5. Select the desired input option.
  6. Check the results in the file proxy_credentials.json stored on the folder.

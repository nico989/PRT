# Primary Refresh Token Exploit
Generate Primary Refresh Token. The Python script must be run locally on a Windows Machine joined to Azure Entra ID or Hybrid. The Primary Refresh Token generated has the same permissions as the Azure AD user signed in the Windows Machine. The Windows component `browsercore.exe` is leveraged to generate a valid Primary Refresh Token.

# Usage
1. Check if the Windows machine is Azure Entra ID or Hybrid joined running:
	```
	dsregcmd.exe /status
	```

2. Get the target domain Tenant ID. AADInternals OSINT can be used: https://aadinternals.com/osint/ .

3. Generate the Primary Refresh Token locally passing the Tenant ID:
	```
	$ python3 prt.py --help
	usage: prt.py [-h] -i ID

	Primary Refresh Token Generator.

	options:
	-h, --help      show this help message and exit
	-i ID, --id ID  Tenant ID

	$ python3 prt.py -i <Tenant ID>
	```

4. Visit https://portal.azure.com. Copy the `x-msRefreshToken` from the script output and paste it into the browser. Then, refresh the https://portal.azure.com page to get access.


# Credits
- Abusing Azure AD SSO with the Primary Refresh Token: https://dirkjanm.io/abusing-azure-ad-sso-with-the-primary-refresh-token 
- Digging further into the Primary Refresh Token: https://dirkjanm.io/digging-further-into-the-primary-refresh-token/ 

# Todo
- Add the possibility to dump the Refresh Token remotely.

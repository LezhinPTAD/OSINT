##Code By Lezhin!
##Ganti = NIGGER
import sys
import os
import json
import time
import requests

api_url = "https://ipgeolocation.abstractapi.com/v1/"
api_key = "b2f69a3c230f4b9b8984fc81804f8e96"

os.system("clear")
def banner():
	print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░      ░░░      ░░        ░   ░░░  ░        ░
▒  ▒▒▒▒  ▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒    ▒▒  ▒▒▒▒  ▒▒▒▒
▓  ▓▓▓▓  ▓▓      ▓▓▓▓▓  ▓▓▓▓  ▓  ▓  ▓▓▓▓  ▓▓▓▓
█  ████  ███████  ████  ████  ██    ████  ████
██      ███      ██        █  ███   ████  ████
██████████████████████████████████████████████
""")

banner()
print("\nWelcome to OSINT! Most useful IP Address OSINT")
print("Thanks for EXEREIWA Brotherhood,Garuda Security")

print("\nPlease select your osint")
print("""1. IP Osint
2. Web Scrape
3. Phone Validation/Information""")

def webscrape(websc):
	try:
		responseWEB = requests.get(f"https://scrape.abstractapi.com/v1/?api_key=5874f75355324330870b7e79a3dc27db&url={websc}")
		if responseWEB.status_code == 200:
			hasilWeb = str(responseWEB.content)
			os.system("clear")
			banner()
			print(f"Web Scraping Result for Website {websc}")
			print("=========================================================")
			print(hasilWeb)
			print("==========================================================")
		else:
			print(f"Uh Oh. Looks like we're unable to fetching the scrape data! API Response : {responseWEB.status_code}")
	except requests.exceptions.RequestException as api_error:
		print(f"There was an error contact: {api_error}")
		raise SystemExit(api_error)

def iptrack(ipaddress):
	try:
		response = requests.get(api_url, params = params)
		responseAPI = requests.get(f"https://api.ip2location.io/?key=D40AF5092474E4F51D304B20082D4D81&ip={ipaddress}&format=json")
		if response.status_code == 200:
			osint_data = response.json()
			API_data = responseAPI.json()

			os.system("clear")
			banner()
			print(f"\n🌐 OSINT Results for IP Address: {osint_data['ip_address']} 🌐")
			time.sleep(0.3)
			print("=========================================")
			time.sleep(0.3)
			print(f" Timezone: {osint_data['timezone']['name']}")
			time.sleep(0.3)
			print(f" ISP: {osint_data['connection']['isp_name']}")
			time.sleep(0.3)
			print(f" Organization: {osint_data['connection']['organization_name']}")
			time.sleep(0.3)
			print(f" AS (Autonomous System): {API_data['as']}")
			time.sleep(0.3)
			print(f" VPN: {osint_data['security']['is_vpn']}")
			time.sleep(0.3)
			print(f" PROXY: {API_data['is_proxy']}")
			time.sleep(0.3)
			print("=========================================")
			time.sleep(2)
			print("Do you want to know more information?")
			var = input("Option(y/n) : ")
			if var != "y":
				time.sleep(1)
				print("Thanks for using IPTrack Lezhin.")
				sys.exit()
			else:
				time.sleep(2)
				print(f"\nBasic Information For {osint_data['ip_address']}")
				print("======================================================")
				time.sleep(0.3)
				print(f"City/ID : {osint_data['city']}, {osint_data['city_geoname_id']}")
				time.sleep(0.3)
				print(f"Region/ISO/ID : {osint_data['region']}, {osint_data['region_iso_code']}, {osint_data['region_geoname_id']}")
				time.sleep(0.3)
				print(f"Postal Code : {osint_data['postal_code']}")
				time.sleep(0.3)
				print(f"Currency Name: {osint_data['currency']['currency_name']}")
				time.sleep(0.3)
				print(f"Currency Code: {osint_data['currency']['currency_code']}")
				time.sleep(0.3)
				print(f"Country/Code/ID: {osint_data['country']}, {osint_data['country_code']}, {osint_data['country_geoname_id']}")
				time.sleep(0.3)
				print(f"Europe: {osint_data['country_is_eu']}")
				time.sleep(0.3)
				print(f"Continent/Code/ID: {osint_data['continent']}, {osint_data['continent_code']}, {osint_data['continent_geoname_id']}")
				time.sleep(0.3)
				print(f"Longitude: {osint_data['longitude']}")
				time.sleep(0.3)
				print(f"Latitude: {osint_data['latitude']}")
				time.sleep(0.3)
				print(f"Google Maps: https://www.google.com/maps/place/{osint_data['latitude']},{osint_data['longitude']}/")
				time.sleep(0.3)
				print("======================================================")
				time.sleep(0.3)
				print("\nPlease wait while we're processing other information")
				time.sleep(2)
				print("\nTime Zone Information")
				time.sleep(0.3)
				print("======================================================")
				time.sleep(0.3)
				print(f"Name: {osint_data['timezone']['name']}")
				time.sleep(0.3)
				print(f"Abbreviation: {osint_data['timezone']['abbreviation']}")
				time.sleep(0.3)
				print(f"GMT Offset: {osint_data['timezone']['gmt_offset']}")
				time.sleep(0.3)
				print(f"Current Time: {osint_data['timezone']['current_time']}")
				time.sleep(0.3)
				print(f"DST: {osint_data['timezone']['is_dst']}")
				time.sleep(0.3)
				print("======================================================")
				time.sleep(0.3)
				print("\nPlease wait while we're processing other information")
				time.sleep(2)
				print("\nConnection Information")
				time.sleep(0.3)
				print("======================================================")
				time.sleep(0.3)
				print(f"ASN: {osint_data['connection']['autonomous_system_number']}")
				time.sleep(0.3)
				print(f"ASO: {osint_data['connection']['autonomous_system_organization']}")
				time.sleep(0.3)
				print(f"Connection Type: {osint_data['connection']['connection_type']}")
				time.sleep(0.3)
				print(f"ISP: {osint_data['connection']['isp_name']}")
				time.sleep(0.3)
				print(f"Organization: {osint_data['connection']['organization_name']}")
				time.sleep(0.3)
				print("======================================================")
				time.sleep(3)
				print("IP Address OSINT Done!!...")
				time.sleep(5)
				print("Credit : SC By ./Lezhin")
		else:
			print(f"\nUh Oh, Looks like we're unable to fetch the data!. API Response : {response.status_code}")
	except requests.exceptions.RequestException as api_error:
		print(f"There was an error contact: {api_error}")
		raise SystemExit(api_error)

def phonevalid(pValid):
	try:
		responseNum = requests.get(f"https://phonevalidation.abstractapi.com/v1/?api_key=3ad8bed5ed154d1b87ae44c88b1cf446&phone={pValid}")
		if responseNum.status_code == 200:
			data_valid = responseNum.json()

			os.system("clear")
			banner()
			print(f"\nPhone Information About {data_valid['phone']}")
			time.sleep(0.3)
			print("===================================")
			time.sleep(0.3)
			print(f"Valid : {data_valid['valid']}")
			time.sleep(0.3)
			print(f"International : {data_valid['format']['international']}")
			time.sleep(0.3)
			print(f"Local : {data_valid['format']['local']}")
			time.sleep(0.3)
			print(f"Location : {data_valid['location']}")
			time.sleep(0.3)
			print(f"Country : {data_valid['country']['name']}")
			time.sleep(0.3)
			print(f"Code : {data_valid['country']['code']}")
			time.sleep(0.3)
			print(f"Prefix : {data_valid['country']['prefix']}")
			time.sleep(0.3)
			print(f"Carrier : {data_valid['carrier']}")
			time.sleep(0.3)
			print(f"Type : {data_valid['type']}")
			time.sleep(0.3)
			print("===================================")
		else:
			print(f"Uh Oh, Looks like we're unable to fetching number data! API Response : {responseNum.status_code}")
	except requests.exceptions.RequestException as api_error:
			print(f"There was an error contact: {api_error}")
			raise SystemExit(api_error)

pilihan = input("\n<=={ OSINT }==> : ")

if pilihan == "1":
	os.system("clear")
	banner()
	print("\nIP Address OSINT")
	ipaddress = input("\n<=={ OSINT }==> : ")
	time.sleep(1)

	params = {
        	'api_key': api_key,
		'ip_address': ipaddress
	}

	iptrack(ipaddress)
elif pilihan == "2":
	os.system("clear")
	banner()
	print("\nWeb Scraping")
	websc = input("\n<=={ OSINT }==> : ")
	time.sleep(1)
	webscrape(websc)

elif pilihan == "3":
	os.system("clear")
	banner()
	print("\nPhone Validation")
	print("Note : Input number without '+'. Example : 6289*********")
	pValid = input("\n<=={ OSINT } ==> : ")
	time.sleep(1)
	phonevalid(pValid)

else:
	print("Pilihan Salah!")
	sys.exit

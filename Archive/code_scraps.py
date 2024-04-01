# Get Domain Categorization via WHOISXMLAPI
## Note: WHOISXMLAPI is heavily limited in free version
## Check available usage: https://user.whoisxmlapi.com/products
## This was neat to try, but not worth rate limiting and unreliable source
# from Keys.whoisxml import api_key
# def get_categorization_whoisxmlapi():
#     domain = 'github.com'
#     url = f'https://website-categorization.whoisxmlapi.com/api/v3?apiKey={api_key}&url=https://{domain}'
#     response = requests.get(url)
#     data = response.json()
#     try:
#         infrastructure = {
#             'Provider': data['as']['domain'],
#             'ProviderName': data['as']['name'],
#             'ProviderRoute': data['as']['route'],
#             'ProviderType': data['as']['type']
#         }
#         target = {
#             'DomainName': data['domainName'],
#             'WebsiteResponse': data['websiteResponded'],
#             'DomainType': data['categories'][0]['name']
#         }
#         print('Infrastructure:', json.dumps(infrastructure, indent=2))
#         print('Target:', json.dumps(target, indent=2))
#     except KeyError:
#         print(data)


# # Whois (OLD)
# import requests, os, json, re

# # Query parameters
# whois_param = 'wowhead.com'

# # Valid query types: 'ip', 'org'
# whois_type = 'ip'

# # Query from nslookup loot if whoisparam != IP address
# with open(f'Loot/nslookup/{whois_param}', 'r') as file:
#     nslookup_output = json.load(file)

# whois_addresses = nslookup_data.get('Addresses',[])

# def query_whois(query, query_type):
#     base_url = 'http://whois.arin.net/rest'
#     # Query types
#     if query_type == 'ip':
#         response = requests.get(f'{base_url}/ip/{query}.json')
#     elif query_type == 'org':
#         response = requests.get(f'{base_url}/org/{query}.json')
#     else:
#         print('[-] Choose a valid query type')
#     # Error handling
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return f'Error: {response.status_code}'

# # Ensure the loot dir exists for whois and create it
# output_dir = 'Loot/whois'
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# # Create caching based off loot
# if not os.path.exists(f'{output_dir}/{whois_param}'):
#     if not whois_addresses:
#         whois_query = query_whois(whois_param, whois_type)
#         if whois_query == 'Error: 400':
#             print('[-] Unspecified query error')
#         elif whois_query == 'Error: 404':
#             print('[-] Misconfigured URL or deleted resource')
#         else:
#             with open(f'Loot/whois/{whois_param}','w') as file:
#                 file.write(json.dumps(whois_query, indent=4))
#                 print(f'[*] Loot stored at Loot/whois/{whois_param}')
#     else:
#         for address in whois_addresses:
#             whois_query = query_whois(address, 'ip')
#             #print(address)
#             if whois_query == 'Error: 400':
#                 print('[-] Unspecified query error')
#             elif whois_query == 'Error: 404':
#                 print('[-] Misconfigured URL or deleted resource')
#             else:
#                 with open(f'Loot/whois/{address}','w') as file:
#                     file.write(json.dumps(whois_query, indent=4))
#                     print(f'[*] Loot stored at Loot/whois/{address}')
# else:
#     print(f'[*] Output located Loot/whois/{whois_param}')

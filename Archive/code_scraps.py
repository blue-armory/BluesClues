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
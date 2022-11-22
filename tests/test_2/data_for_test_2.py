from random import choice

brewery_id = ["madtree-brewing-cincinnati", "10-56-brewing-company-knox", "incheonbrewery-jung-gu"]

brewery_types = ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'closed']

BASE_URL_2 = "https://api.openbrewerydb.org"

ENDPOINTS_2 = {
    "Single Brewery": f"{BASE_URL_2}/breweries/{choice(brewery_id)}",
    "List Breweries": f"{BASE_URL_2}/breweries",
    "Random Brewery": f"{BASE_URL_2}/breweries/random"
}

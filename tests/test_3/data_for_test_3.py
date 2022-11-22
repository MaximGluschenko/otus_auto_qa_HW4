from random import randint

BASE_URL_3 = "https://jsonplaceholder.typicode.com"

ENDPOINTS_3 = {
    "Getting a resource": f"{BASE_URL_3}/posts/{randint(1, 10)}",
    "Listing all resources": f"{BASE_URL_3}/posts",
    "Listing nested comments": f"{BASE_URL_3}/posts/{randint(1, 10)}/comments",
    "Listing nested photos": f"{BASE_URL_3}/albums/{randint(1, 10)}/photos",
    "Listing nested albums": f"{BASE_URL_3}/users/{randint(1, 10)}/albums",
    "Listing nested todos": f"{BASE_URL_3}/users/{randint(1, 10)}/todos",
    "Listing nested posts": f"{BASE_URL_3}/users/{randint(1, 10)}/posts",
}

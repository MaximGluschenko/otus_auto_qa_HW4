from random import choice, randint

breeds_all = ["beagle", "dingo", "ovcharka"]
breeds_with_sub_breed_only = ["elkhound", "pointer", "ovcharka"]

BASE_URL_1 = "https://dog.ceo/api"

ENDPOINTS_1 = {
    "List all breeds": f"{BASE_URL_1}/breeds/list/all",
    "Display single random image from all dogs collection": f"{BASE_URL_1}/breeds/image/random",
    "By breed": f"{BASE_URL_1}/breed/{choice(breeds_all)}/images",
    "List all sub-breeds": f"{BASE_URL_1}/breed/{choice(breeds_with_sub_breed_only)}/list",
    "Multiple images from a breed collection": f"{BASE_URL_1}/breed/{choice(breeds_all)}/images/random/{randint(1, 50)}",
    "Breeds list": f"{BASE_URL_1}/breed/{choice(breeds_all)}/images/random"
}

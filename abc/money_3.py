import sys
def success(id, hotel_name, room_name,plan_name, total_price):
    print('The cheapest plan has been successfully reserved.')
    print("- reservation id:", id)
    print("- hotel name:", hotel_name)
    print("- room name: <ルーム名>", room_name)
    print("- plan name:", plan_name)
    print("- total price:", total_price)
def not_success():
    print("The cheapest plan is fully booked.")
def not_found():
    print("Plan not found.")
import requests
import json
url_search = "https://challenge-server.tracks.run/hotel-reservation/hotels"
url_reserve = "https://challenge-server.tracks.run/hotel-reservation/reservations"
def main(argv):
    data = json.loads(argv[1])
    header_for_search = {
        "Content-Type": "application/json",
        "x-access-token": argv[0]
        }
    param_for_search = {
        "keyword":data["keyword"],
        "number":data["number"],
        "condition":data["condition"]
    }
    r= requests.get(url_search, params=param_for_search,headers=header_for_search).json()
    L = len(r)
    if L==0:
        not_found()
        exit()
    d = r
    #print(L)
    price = 10**24
    cheap_id = 10**24
    for d in r:
        if not ("plans" in d):
            continue
        for q in d["plans"]:
            for p in q:
                if int(p["price"])<price or (int(p["price"]) == price and int(p["id"]) < cheap_id):
                    price = int(p["price"])
                    cheap_id = int(p["id"])


if __name__ == '__main__':
    main(sys.argv[1:])
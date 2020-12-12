import requests

def get_coord_by_address(address):
    api_url = 'https://nominatim.openstreetmap.org/search?q=%s&format=json&countrycodes=kr'
    response = requests.get(api_url % address) #get 방식으로 데이터 가져옴
    if response.status_code == 200: #성공 할경우
        json = response.json()
        if len(json) > 0: #json 길이가 0 이상
            first = json[0] #데이터 가져옴
            return (first['lat'], first['lon']) #lat 와 lon 데이터 가져옴
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    print(get_coord_by_address('청와대'))

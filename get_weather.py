import requests
import voice
import map

def get_weather_by_code(code):
    api_url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=%s"
    app_id = "보안"
    unit = "metric"	# 미터법을 이용하겠다 명시

    response = requests.get(api_url % (code, app_id, unit))
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_weather_by_coord(lat, lon):
    api_url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=%s"
    app_id = "보안"
    unit = "metric"	# 미터법을 이용하겠다 명시

    response = requests.get(api_url % (lat, lon, app_id, unit))
    if response.status_code == 200:
        return response.json()
    else:
        return None

def create_weather_text(weather_info, address):
    response = "현재 %s의 온도는 %d 도이고, 습도는 %d 퍼센트입니다."
    if weather_info != None:
        return response % (address, weather_info['main']['temp'], weather_info['main']['humidity'])
    else:
    	return "날씨를 알 수 없습니다."

def main():
    voice.speech("어디의 날씨를 알려드릴까요?")
    address = voice.get_text_from_voice()

    coord = map.get_coord_by_address(address) #존재하는 도시인지 체크
    if coord == None: #지역이 없을경우
        voice.speech("%s을 찾지 못했습니다." % address)
    else:
        weather_info = get_weather_by_coord(coord[0], coord[1]) # 경도와 위도 정보 가져오기

        response_text = create_weather_text(weather_info, address) #weater_info 온도,습도 주소 말하기
        voice.speech(response_text)


if __name__ == "__main__":
    main()

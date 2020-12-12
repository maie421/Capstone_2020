import voice
import get_weather as weather
import food_recognize

def main():
    while True:
        if voice.detect_wake_up_word():
            input_text = voice.get_text_from_voice()
            print(input_text) #voice 출력 문자열
            if input_text.find("날씨") != -1: #날씨 문자열이 있을겨우
                    weather.main()
            elif input_text.find("냉장고") != -1:#냉장고 문자열이 있을겨우
                   food_recognize.main()
            else:
                result_answer = voice.query_by_text(input_text) 
                voice.speech(result_answer) #다시 말씀해 주세요
if __name__ == "__main__":
    main()

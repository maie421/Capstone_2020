import voice
import get_weather as weather
import food_recognize

def main():
    while True:
        if voice.detect_wake_up_word():
            input_text = voice.get_text_from_voice()
            print(input_text)
            if input_text.find("날씨") != -1:
                    weather.main()
            elif input_text.find("냉장고") != -1:
                   food_recognize.main()
            else:
                result_answer = voice.query_by_text(input_text)
                voice.speech(result_answer)
if __name__ == "__main__":
    main()
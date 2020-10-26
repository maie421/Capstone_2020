import voice
import time

def start_timer(input_text) :
    hms = [0, 0, 0]
    if input_text.find("타이머") != -1 :
        for word in input_text.split(" ") :
            if word.find("시간") != -1 :
                hour = int(word.replace("시간", ""))
                hms[0] = hour
            elif word.find("분") != -1 :
                minute = int(word.replace("분", ""))
                hms[1] = minute
            elif word.find("초") != -1 :
                second = int(word.replace("초", ""))
                hms[2] = second
        print(hms)
        voice.speech("타이머가 %d시간 %d분 %d초로 설정됩니다."%(hms[0], hms[1], hms[2]))
        timer_sec = hms[0] * 3600 + hms[1] * 60 + hms[2]
        print(timer_sec)
        time.sleep(timer_sec)
        print("timer end")
        voice.speech("땡땡땡 타이머가 종료되었습니다.")
    else:
      voice.speech("타이머가 설정되지 않았습니다.")

def main():
    voice.speech("타이머를 시작합니다. 설정할 시간을 말해주세요")
    input_text = voice.get_text_from_voice()
    start_timer(input_text)

if __name__ == "__main__" :
    main()

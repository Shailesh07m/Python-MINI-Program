import time
import datetime
import pygame



def set_alarm(alarm_time):
    print(f"Alarm Set for {alarm_time}")

  
    sound_file="blue.mp3"
    pygame.mixer.init()

    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time:", current_time)

        if current_time == alarm_time:
            print("Wake UP!!")
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            break

        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM format): ")
    set_alarm(alarm_time)

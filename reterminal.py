import seeed_python_reterminal
from time import sleep
import os

def shutdown():
    os.system('sudo halt')

def main():
    f1_button = seeed_python_reterminal.Button(seeed_python_reterminal.Button.F1)
    buzzer = seeed_python_reterminal.Buzzer()
    
    while True:
        if f1_button.read():
            buzzer.on()
            sleep(1)
            buzzer.off()
            shutdown()

if __name__ == '__main__':
    main()
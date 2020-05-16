import keyboard,serial
import datetime
print("opening")
ser = serial.Serial("COM4", 74880, timeout=0.1)
print("waiting")
morse = {
        # Letters
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        # Numbers
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Punctuation
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
    }
reverse_morse = {v: k for k, v in morse.items()}
history = []
current_msg = ""
current_char=None
last_message_time = None
def dot_or_line(length):
    if int(length)>220:
        return "-"
    return "."
while True:
    line=ser.readline().decode("utf-8").replace("\r\n", "")
    if "," in line:
        now = datetime.datetime.now()
        if last_message_time is not None: print((now-last_message_time).microseconds/1000)
        if last_message_time is not None and (now-last_message_time).microseconds/1000>1200:
            print("space")
            keyboard.write(" ")
        l = line.split(",")[1]
        current_msg+=dot_or_line(l)
        print(current_msg)
        last_message_time=datetime.datetime.now()
    if last_message_time is not None and current_msg!="":
        print(current_msg)
        now = datetime.datetime.now()
        
        if (now-last_message_time).microseconds/1000>800:
            try:
                current_char = reverse_morse[current_msg]
            except KeyError:
                current_msg=""
                last_message_time=now
            else:
                current_msg=""
                last_message_time=now
                keyboard.write(current_char)
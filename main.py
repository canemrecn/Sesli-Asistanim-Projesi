import speech_recognition as sr
import os
import time
from datetime import datetime
import random
import webbrowser
import pyautogui
import pyowm
import pyttsx3
import keyboard
#Gerekli kütüphaneleri import et
engine = pyttsx3.init()
# Metin konuşma motorunu başlat
r = sr.Recognizer()
# Ses tanıma için bir Recognizer objesi oluştur
def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
# Eğer `ask` argümanı True ise, kullanıcıya bir soru sorulacaksa, soruyu konsola yazdırır.
        audio = r.listen(source)
# Mikrofondan ses kaydı alır.
        voice = ""
# Tanınan metin için bir değişken oluşturur.
        try:
            voice = r.recognize_google(audio, language="tr-TR")
# Ses kaydını tanır ve metne dönüştürür.
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım. Tekrar eder misiniz?")
# Tanınamayan metin hatası durumunda hata mesajını yazdırır.
        except sr.RequestError:
            print("Asistan: Üzgünüm, sistem çöktü.")
# Google Web Speech API'ye istek gönderme hatası durumunda hata mesajını yazdırır.
        return voice
# Tanınan metni döndürür.
def response(voice):
    owm_api_key = "2cc4adf144046eff5e703ab19f123697"
# OpenWeatherMap API anahtarını tanımlar.
    owm = pyowm.OWM(owm_api_key)
# PyOWM kütüphanesiyle OpenWeatherMap nesnesini oluşturur.

    if "merhaba" in voice or 'selam' in voice:
        speak("hi")
# Eğer kullanıcının girişi "merhaba" veya "selam" içeriyorsa, "hi" yanıtını seslendirir.
    if "kendinden" in voice or 'kimsin' in voice or 'bahset' in voice:
        speak("i am a voice assistant artificial intelligence written by emrecan.who are you")

    if "ben" in voice or 'adım' in voice:
        speak("nice to meet you. what can I do for you")

    if "nasılsın" in voice or 'nasıl gidiyor' in voice:
        speak("thank you, ı'm fine. how are you")

    if "iyiyim" in voice or 'iyi' in voice:
        speak("I'm glad you're okay. what can I do for you")

    if "kötü" in voice or 'kötüyüm' in voice:
        speak("what can I do for you")

    if "dur" in voice:
        speak("stopped")
        keyboard.press_and_release(" ")

    if "devam" in voice:
        speak("continuing")
        keyboard.press_and_release(" ")

    if "dünyanın" in voice:
        speak("i'm looking for the most beautiful woman in the world")
        url = "C:/Users/user/Downloads/ceren.jpeg"
        webbrowser.get().open(url)

    if "yenile" in voice:
        speak("i'm refreshing the page")
        keyboard.press_and_release("F5")

    if "önceki" in voice:
        speak("going to the previous page")
        keyboard.press_and_release("Alt+Left")

    if "geri" in voice:
        keyboard.press_and_release("Left")

    if "sonraki" in voice:
        speak("going to the next page")
        keyboard.press_and_release("Alt+Right")

    if "ileri" in voice:
        keyboard.press_and_release("Right")

    if "yap" in voice:
        speak("i'm doing a full screen")
        keyboard.press_and_release("F11")

    if "çık" in voice:
        speak("i'm coming out of the full screen")
        keyboard.press_and_release("F11")

    if "pencereyi" in voice:
        speak("closing the window")
        keyboard.press_and_release("Alt+F4")

    if "geçmiş" in voice:
        speak("opening the past")
        keyboard.press_and_release("Ctrl+T")

    if "ss" in voice or "görüntü" in voice or "screenshot" in voice:
        speak("taking a screenshot")
        keyboard.press_and_release("Windows+Print Screen")

    if "tamam" in voice or 'evet' in voice or 'enter' in voice:
        keyboard.press_and_release("Enter")

    if 'konum' in voice or 'harita' in voice or 'yol' in voice:
        speak("Opening the Maps application.")
        os.system("start bingmaps://?rtp=adr~")

    if '4' in voice:
        pyautogui.move(-50, 0, duration=1)

    if '40' in voice:
        pyautogui.move(-100, 0, duration=1)

    if '400' in voice:
        pyautogui.move(-300, 0, duration=1)

    if 'sola' in voice or 'sol' in voice:
        pyautogui.move(-500, 0, duration=1)

    if '6' in voice:
        pyautogui.move(50, 0, duration=1)

    if '60' in voice:
        pyautogui.move(100, 0, duration=1)

    if '600' in voice:
        pyautogui.move(300, 0, duration=1)

    if 'sağ' in voice or 'sağa' in voice:
        pyautogui.move(500, 0, duration=1)

    if '8' in voice:
        pyautogui.moveRel(0, -50, duration=1)

    if '80' in voice:
        pyautogui.move(0, -100, duration=1)

    if '800' in voice:
        pyautogui.move(0, -300, duration=1)

    if 'yukarı' in voice:
        pyautogui.move(0, -500, duration=1)

    if '2' in voice:
        pyautogui.move(0, 50, duration=1)

    if '20' in voice:
        pyautogui.move(0, 100, duration=1)

    if '200' in voice:
        pyautogui.move(0, 300, duration=1)

    if 'aşağı' in voice:
        pyautogui.move(0, 500, duration=1)

    if 'tıkla' in voice:
        pyautogui.click(button='left')

    if 'çift' in voice:
        for i in range(2):
            pyautogui.click(button='left')

    if 'seçenek' in voice:
        pyautogui.click(button='right')

    if '5' in voice or 'beş' in voice or 'kıs' in voice:
        for i in range(8):
            keyboard.press_and_release("down")

    if '7' in voice or 'yedi' in voice or 'yükselt' in voice:
        for i in range(8):
            keyboard.press_and_release("up")

    if 'ayarlar' in voice:
        keyboard.press_and_release("Windows + ı")

    if 'oku' in voice or 'okuyucu kapat' in voice:
        keyboard.press_and_release("Windows + Ctrl + Enter")

    if 'küçült' in voice:
        keyboard.press_and_release("Windows + Shift + Down")

    if 'simge' in voice:
        keyboard.press_and_release("Windows + '+'")

    if 'yakınlaştır' in voice:
        keyboard.press_and_release("Windows+plus")

    if 'uzaklaştır' in voice:
        keyboard.press_and_release("Windows + -")

    if 'büyüteci kapat' in voice:
        os.system("TASKKILL /F /IM Magnify.exe")

    if 'bul' in voice:
        keyboard.press_and_release('CTRL + W')

    if 'sekmeyi kapat' in voice or 'tekmeyi kapat' in voice:
        keyboard.press_and_release('CTRL + w')

    if 'sekme aç' in voice or 'tekme aç' in voice:
        keyboard.press_and_release('CTRL + t')

    if 'klasör oluştur' in voice:
        keyboard.press_and_release('CTRL + Shift + n')

    if 'kopyala' in voice:
        keyboard.press_and_release('CTRL + c')

    if 'yapıştır' in voice:
        keyboard.press_and_release('CTRL + v')

    if 'kes' in voice:
        keyboard.press_and_release('CTRL + x')

    if 'tümünü seç' in voice:
        keyboard.press_and_release('CTRL + a')

    if 'geri al' in voice:
        keyboard.press_and_release('CTRL + z')

    if 'kaydet' in voice:
        keyboard.press_and_release('CTRL + s')

    if 'geçiş' in voice:
        keyboard.press_and_release('ALT + Tab')

    if 'dosya özellikleri' in voice:
        keyboard.press_and_release('ALT + Enter')

    if 'yeniden adlandır' in voice:
        keyboard.press_and_release('F2')

    if 'adres çubuğu' in voice:
        keyboard.press_and_release('F4')

    if 'görev yöneticisi' in voice:
        keyboard.press_and_release('CTRL + Shift + Esc')

    if 'çalıştır' in voice:
        keyboard.press_and_release('Windows + r')

    if 'geri sar' in voice:
        for i in range(8):
            keyboard.press_and_release('left')

    if 'baş' in voice or 'baştan' in voice or 'başa' in voice:
        for i in range(100):
            keyboard.press_and_release('left')

    if 'ileri sar' in voice:
        for i in range(8):
            keyboard.press_and_release('right')

    def record_audio():
        # Mikrofondan kayıt al
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Dinliyorum...")
            audio = r.listen(source)

        # Sesi metne çevir
        try:
            text = r.recognize_google(audio, language='tr-TR')
            print(f"Söylediğiniz: {text}")
            return text
        except sr.UnknownValueError:
            print("Ne dediğinizi anlayamadım.")
        except sr.RequestError as e:
            print(f"Ses algılama servisinde bir hata oluştu; {e}")

        return ""

    if "hava" in voice:
        speak("Which city's weather would you like to know about?")
        city = record_audio()

        # Hava durumu bilgisini al
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        weather = observation.weather

        # Hava durumu bilgisini sesli olarak oku
        speak(f"{city} the weather forecast of the city is as follows: {weather.detailed_status}, "
              f"temperature {weather.temperature('celsius')['temp']} degree, "
              f"humidity ratio {weather.humidity} measured as.")

    if "günlerden" in voice or "gündeyiz" in voice:
        today = time.strftime("%A")
        today.capitalize()

        if today == "Monday":
            today = "Monday"

        elif today == "Tuesday":
            today = "Tuesday"

        elif today == "Wednesday":
            today = "Wednesday"

        elif today == "Thursday":
            today = "Thursday"

        elif today == "Friday":
            today = "Friday"

        elif today == "Saturday":
            today = "Saturday"

        elif today == "Sunday":
            today = "Sunday"

        speak(today)

    if "metin oluştur" in voice:
        speak("i created a text file")
        with open ("metin_dosyasi.txt","w") as f:
            f.write(" ")

    if "metin dosyasını aç" in voice:
        speak("opening the text file")
        url = "C:/Users/user/Projelerim/As Projeler/Sesli Asistanım/metin_dosyasi.txt"
        webbrowser.get().open(url)

    if "belgelerimi" in voice:
        speak("my documents are being opened")
        url = "C:/Users/user"
        webbrowser.get().open(url)

    if "şarkı" in voice or "kafana" in voice:
        speak("i'm opening a song")
        urls = [
            "https://www.youtube.com/watch?v=i6CSvLvSNZ4&list=PLRnQM3gfzjtWB-8fhygDBx7VXpnZY0ohl&index=4",
            "https://www.youtube.com/watch?v=9TSf2k03HPA",
            "https://www.youtube.com/watch?v=vlyaJ2NPkO0",
            "https://www.youtube.com/watch?v=rThjDgw-sBM",
            "https://www.youtube.com/watch?v=wAzYFXHLFKU",
            "https://www.youtube.com/watch?v=niF38c2clBQ",
            "https://www.youtube.com/watch?v=fxXGGjVb9TI",
            "https://www.youtube.com/watch?v=vn9lvxuPPso",
            "https://www.youtube.com/watch?v=qrDXdmyqxTE"
            "https://www.youtube.com/watch?v=niF38c2clBQ"
            "https://www.youtube.com/watch?v=vn9lvxuPPso"
            "https://www.youtube.com/watch?v=fxXGGjVb9TI"
            "https://www.youtube.com/watch?v=75ynAc-9kJk"
            "https://www.youtube.com/watch?v=5X7qAZWOT_I"
            "https://www.youtube.com/watch?v=d8Upm7AKgH8"
            "https://www.youtube.com/watch?v=ZZwtZWUezoo"
            "https://www.youtube.com/watch?v=Z15prbkFPbw"
            "https://www.youtube.com/watch?v=qrDXdmyqxTE"
            "https://www.youtube.com/watch?v=XeggNKcU-xo"
            "https://www.youtube.com/watch?v=ptU5VXXHA90"
            "https://www.youtube.com/watch?v=kLGvPVQ7Djs"
            "https://www.youtube.com/watch?v=tMUtzjSkjnY"
            "https://www.youtube.com/watch?v=qUsE49lUQUY"
            "https://www.youtube.com/watch?v=TKmh5VhMpp8"
            "https://www.youtube.com/watch?v=ME1WaoCudmw"
            "https://www.youtube.com/watch?v=0gSyfcrK07s"
            "https://www.youtube.com/watch?v=FVY4be1yFFY"
            "https://www.youtube.com/watch?v=fZYZPANBF6g"
            "https://www.youtube.com/watch?v=XGWQXjyUip8"
            "https://www.youtube.com/watch?v=yoNzzWRye7c"
            "https://www.youtube.com/watch?v=3YL4Btzcf2Q"
            "https://www.youtube.com/watch?v=BTmml0itL2U"
            "https://www.youtube.com/watch?v=FQcdTxzzL4I"
            "https://www.youtube.com/watch?v=sr6w-6tBTDk"
            "https://www.youtube.com/watch?v=g4aBjmVZRvw"
            "https://www.youtube.com/watch?v=VoIK-Qw9Jec"

        ]
        url = random.choice(urls)
        webbrowser.get().open(url)

    if "video" in voice:
        speak("i'm opening a video")
        urls = [
            "https://www.youtube.com/watch?v=KqjGpL9H-Gs",
            "https://www.youtube.com/watch?v=N9uPBwr1OaY&t=1646s",
            "https://www.youtube.com/watch?v=a0OJlKSYiOY&t=7s",
            "https://www.youtube.com/watch?v=Ho80TCgAilc",
            "https://www.youtube.com/watch?v=-I838TicMSo",
            "https://www.youtube.com/watch?v=QuC0_0XVKj0",
            "https://www.youtube.com/watch?v=sKaftalYjZQ",
            "https://www.youtube.com/watch?v=J1_q85dVgGk&t=6s",
            "https://www.youtube.com/watch?v=6mDKbC93d1c&t=1898s"
            "https://www.youtube.com/watch?v=9ybbK7XlQvo"
            "https://www.youtube.com/watch?v=SFEjWFzkj6g&t=6s"
            "https://www.youtube.com/watch?v=5qlnMcwxPrI"
            "https://www.youtube.com/watch?v=-HmK5oF1j9I&t=29s"
            "https://www.youtube.com/watch?v=BUZjSfRQ1xA&t=768s"
            "https://www.youtube.com/watch?v=STcSmXQlA3U"
            "https://www.youtube.com/watch?v=pyi-u4_XpnI"
            "https://www.youtube.com/watch?v=GVNphcaOhmY&t=689s"
            "https://www.youtube.com/watch?v=lxwQimTOj3I"
            "https://www.youtube.com/watch?v=9bQXappobQk"
            "https://www.youtube.com/watch?v=kbYgpQ5R8eE&t=537s"
            "https://www.youtube.com/watch?v=j4dAHvMCkhQ"
            "https://www.youtube.com/watch?v=0LTmJtYnpjo"
            "https://www.youtube.com/watch?v=lHdCpJTLXLs"
            "https://www.youtube.com/watch?v=czustW7dcak&t=1198s"
            "https://www.youtube.com/watch?v=rT8YqrB-iNY&t=1s"
            "https://www.youtube.com/watch?v=0TO_vu8pVrE&t=881s"
            "https://www.youtube.com/watch?v=OHLb3K3KcKE&t=551s"
            "https://www.youtube.com/watch?v=KrHAkAuCR_s"
            "https://www.youtube.com/watch?v=VCAViLh4SUI"
            "https://www.youtube.com/watch?v=1Uan0dR5Dqs&t=263s"
            "https://www.youtube.com/watch?v=gwRGUnqbcUM"
            "https://www.youtube.com/watch?v=GdWDtwlTbcg"
            "https://www.youtube.com/watch?v=oxYNxJM8lQ8"
            "https://www.youtube.com/watch?v=6mDKbC93d1c&t=1898s"
            "https://www.youtube.com/watch?v=QP47Rcje0Tg"
            "https://www.youtube.com/watch?v=RIYXzfWJJK4"

        ]
        url = random.choice(urls)
        webbrowser.get().open(url)

    if "saat" in voice:
        selection = ["The time is now: "]
        clock=datetime.now().strftime("%H:%M")
        selection=random.choice(selection)
        speak(selection+clock)

    if "arama" in voice or "ara" in voice or "google" in voice:
        speak("what do you want me to look for")
        search = record("ne aramamı istersin")
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        print(search + " için bulduklarım")

    if "youtube" in voice or "gir" in voice:
        speak("what do you want me to open on youtube")
        search = record("youtubeda neyi açmamı istersin")
        url = "https://www.youtube.com/" + search
        webbrowser.get().open(url)
        print(search + " için bulduklarım")

    if "twitter " in voice:
        speak("i'm opening it on twitter")
        url = "https://twitter.com/?lang=tr"
        webbrowser.get().open(url)

    if "fifa" in voice:
        speak("opening the fifa")
        url = "steam://rungameid/1506830"
        webbrowser.get().open(url)

    if "internet" in voice:
        speak("opening the internet")
        url = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
        webbrowser.get().open(url)

    if "tlc" in voice:
        url = "https://www.tlctv.com.tr/canli-izle"
        webbrowser.get().open(url)

    if "bilgisayarı kapat" in voice:
        os.system("shutdown /s /t 1")

    if 'yeniden başlat' in voice:
        os.system('shutdown /r /t 1')

    if "çeviri" in voice:
        speak("opening the translation")
        url = "https://ceviri.yandex.com.tr/translator/Turkce-Ingilizce"
        webbrowser.get().open(url)



def speak(text):
    engine.say(text)
# Pyttsx3 motoruyla metni seslendirir.
    engine.runAndWait()
 # Seslendirmenin tamamlanmasını bekler.

while True:
    voice = record()
# Kullanıcının ses girişini kaydeder.
    if voice != "":
        voice = voice.lower()
# Kullanıcı girişini küçük harflere dönüştürür.
        print(voice)
# Kullanıcı girişini ekrana yazdırır.
        if voice == "görüşürüz":
            speak("I'm shutting down the system. See you.")
# Eğer kullanıcının girişi "görüşürüz" ise, "I'm shutting down the system. See you." metnini
# seslendirir.
            break
        response(voice)
# Kullanıcının girişine yanıt vermek için response() fonksiyonunu çağırır.
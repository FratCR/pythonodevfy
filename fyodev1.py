
import requests # to get url request
import webbrowser # to going web site
import pyautogui # to take screenshot           # pyautogui library is very useful to automation
from PIL import ImageGrab
import time
from selenium import webdriver

url = "https://www.youtube.com/watch?v=-_jddlcOhwQ&t=44s&ab_channel=%D0%A0%D0%95%D0%9C%D0%9B%D0%90%D0%91%D0%A1%D0%95%D0%A0%D0%92%D0%98%D0%A1" # url link

response = requests.get(url) # Get request

if response.status_code == 200:
    print("Yonlendirme basarili.")
    time.sleep(3)

    driver = webdriver.Chrome()
    
    driver.switch_to.window(driver.window_handles[0])
    
    driver.get(url)

    screenshot = driver.get_screenshot_as_png()
    with open('screenshot.png', 'wb') as f:
        f.write(screenshot)
    
    driver.quit()
    
else:
    print("Yonlendirme basarisiz. Hata kodu:", response.status_code)


"""
import requests
import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

url = "https://www.youtube.com/watch?v=-_jddlcOhwQ&t=44s&ab_channel=%D0%A0%D0%95%D0%9C%D0%9B%D0%90%D0%91%D0%A1%D0%95%D0%A0%D0%92%D0%98%D0%A1"  # Yönlendirilecek site URL'i

response = requests.get(url)  # GET isteği gönderme

# İsteğin sonucuna göre işlem yapma
if response.status_code == 200:
    print("Yönlendirme başarılı.")
    time.sleep(20)  # 20 saniye bekleyin (isteğin sonuçlarını görmek için)

    # Mevcut Chrome sekmesini açık olarak kullanma
    options = webdriver.ChromeOptions()
    options.add_argument("--remote-debugging-port=9222")  # Hata ayıklama portunu belirleme

    # ChromeDriver servisini başlatma
    service = Service('/path/to/chromedriver')  # ChromeDriver'ın dosya yolu
    service.start()

    # Chrome tarayıcısını başlatma
    driver = webdriver.Remote(service.service_url, options=options)

    # Yönlendirilen sayfayı açma
    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)

    # Ekran görüntüsünü alma
    driver.save_screenshot('screenshot.png')

    # Tarayıcıyı kapatma
    driver.quit()

    # ChromeDriver servisini durdurma
    service.stop()

else:
    print("Yönlendirme başarısız. Hata kodu:", response.status_code)
"""
import requests
from stem.control import Controller
from stem import Signal
import tqdm
from progress.bar import IncrementalBar
import time



def get_tor_session():
    # инициализировать сеанс запросов
    session = requests.Session()
    # установка прокси для http и https на localhost: 9050
    # для этого требуется запущенная служба Tor на вашем компьютере и прослушивание порта 9050 (по умолчанию)
    session.proxies = {"http": "socks5://localhost:9050", "https": "socks5://localhost:9050"}
    return session

def renew_connection():
    with Controller.from_port(port=9051) as c:
        c.authenticate()
        # отправить сигнал NEWNYM для установления нового чистого соединения через сеть Tor
        c.signal(Signal.NEWNYM)
        #time.sleep(5)

#bar = IncrementalBar('IP testing', max = 10)
for n in range(10):
	#bar.next()
	#renew_connection()
	s = get_tor_session()
	ip = s.get("http://icanhazip.com").text
	print("IP:", ip)
	renew_connection()
	s = get_tor_session()
	ip = s.get("http://icanhazip.com").text
	print("IP:", ip)
	#time.sleep(1)
	print('\n iteration end \n')
	#time.sleep(5)
	renew_connection()
	
#bar.finish()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import tweepy
import requests
import json
import sqlite3
import pandas as pd

# Definimos la URL-principal y la ruta al driver de chrome
main_url = 'https://twitter.com/?lang=es' # URL principal
chromedriver = './chromedriver'
# Abrimos una ventana con la URL-principal
browser = webdriver.Chrome()
browser.get(main_url)

time.sleep(3)

login_button = browser.find_element(By.XPATH, '//a[@data-testid="loginButton"]')
login_button.click()

# Espera un tiempo para que la nueva página se cargue completamente
time.sleep(5)

email = "amtoniovx@gmail.com"
user = "@AntonioVGHX"
password = "AValentin86"

email_field = browser.find_element(By.NAME, 'text')
email_field.send_keys(email)
time.sleep(3)
email_field.send_keys(Keys.RETURN)
time.sleep(3)

user_field = browser.find_element(By.NAME, 'text')
user_field.send_keys(user)
time.sleep(3)
user_field.send_keys(Keys.RETURN)
time.sleep(3)

password_field = browser.find_element(By.NAME, 'password')
password_field.send_keys(password)
time.sleep(3)
password_field.send_keys(Keys.RETURN)
time.sleep(10)

# Configurar las credenciales de la API de Twitter
consumer_key = 'kM3XtOEiuXGtsbcxIEvTSSMW2'
consumer_secret = 'RQorwNAsbesLSfkqLDThK0U1MzGKlX9rmgRUCOcb18bjyYnP2v'
access_token = '1747292494067355648-C9n7Z9aLeeSJkfjW5LKmqEstvdaZee'
access_token_secret = 'Oig4po7bjpYbNK7UKZeIvl0jZ3HHYorlUYuPHSaWFQaDC'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAOn6rwEAAAAATfq1NeQ5K53OzLMyCb9CP11SQNM%3D1ssD1FhMzLLRiDIzCaBofRx1I0yFeBrbc2tJuMKAsAXYfkNWmo'
client = tweepy.Client(bearer_token=bearer_token)


# Autenticar con la API de Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Nombre de usuario de la cuenta que quieres seguir
nombre_usuario = '@SSC_CDMX'

# Hacemos clic en el icono de búsqueda
search_icon = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div')
search_icon.click()
time.sleep(10)



buscar = browser.find_element(By.XPATH, '//input[@data-testid="SearchBox_Search_Input"]')
buscar.send_keys(nombre_usuario)
time.sleep(3)
buscar.send_keys(Keys.RETURN)
time.sleep(10)

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="UserCell"]')))

# Seleccionamos el primer resultado de la búsqueda
primer_resultado = browser.find_element(By.XPATH, '(//div[@data-testid="UserCell"])[1]')

# Hacemos clic en el primer resultado para ir al perfil del usuario
primer_resultado.click()
time.sleep(40)


scrolls = 2
altura_de_desplazamiento = 1000  # Ajusta este valor según tus necesidades

# Desplázate hacia abajo en la página
for _ in range(scrolls):
    browser.execute_script(f"window.scrollBy(0, {altura_de_desplazamiento});")
    time.sleep(10)
num_tweets = 10

tweets = []

for i in range(1, num_tweets + 1):
    # Construye el XPath con el número de div ascendente
    xpath = f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div/div/div[{i}]'

    # Obtiene el tweet
    tweet = browser.find_element(By.XPATH, xpath)

    # Añade el texto del tweet a la lista de tweets
    tweets.append(tweet.text)

    # Imprime el texto del tweet
    print(f"Tweet {i}: {tweet.text}")

# Imprime todos los tweets
print(tweets)

# Crear un DataFrame de pandas con los tweets
df = pd.DataFrame({'Tweets': tweets})

# Guardar el DataFrame en un archivo Excel
excel_filename = 'tweets_data.xlsx'
df.to_excel(excel_filename, index=False)

print(f'Los tweets se han guardado en {excel_filename}')
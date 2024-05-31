import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json
from machine import Pin, PWM
from random import randint

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'Ssdc'
password = 'Sdc.190299'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://hp-api.lainocs.fr/characters"

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

pwm_led_blue = PWM(Pin(16,mode=Pin.OUT)) # on prescise au programme que la pin 17 est une sortie de type PWN
pwm_led_green = PWM(Pin(17,mode=Pin.OUT))
pwm_led_red = PWM(Pin(18,mode=Pin.OUT))

pwm_led_blue.freq(1_000) # dont la frequence est de 1000 (default)
pwm_led_blue.duty_u16(0) # on lui donne une valeur comprise entre 0  et 65535 qui est converti entre 0 et 3.3v

pwm_led_green.freq(1_000)
pwm_led_green.duty_u16(0)

pwm_led_red.freq(1_000)
pwm_led_red.duty_u16(0)

colors = [11000,11000,11000]

#dictionnaire qui associe chaque maison à sa couleur avec un tableau [RVB] :

dictionnary = {"Gryffindor": [11000,0,0], "Ravenclaw": [0,0,11000], "Hufflepuff": [11000,5000,0], "Slytherin": [0,11000,0] }


while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        random = randint(0, len(r.json())-1)#prend un personnage aléatoire dans l'api
        print(r.json()) # traite sa reponse en Json
        #print(r.json()[1]["house"])
        #print(r.json()[1]["name"])
        house = r.json()[random]["house"] #va chercher la maison du personnage
        name = r.json()[random]["slug"] #va chercher le nom du personnage
        print(house) #me sort la maison
        print(name) #me sort le nom
        pwm_led_red.duty_u16(dictionnary[house][0]) #associe la led rouge au tableau dans le dictionnaire
        pwm_led_green.duty_u16(dictionnary[house][1]) #associe la led verte au tableau dans le dictionnaire
        pwm_led_blue.duty_u16(dictionnary[house][2]) #associe la led bleu au tableau dans le dictionnaire
        r.close() # ferme la demande
        utime.sleep(5)  
    except Exception as e:
        print(e)
    
    
    
    
        

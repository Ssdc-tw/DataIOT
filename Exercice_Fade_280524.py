from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import utime # importe dans le code la lib qui permet de gerer le temps

pwm_led = PWM(Pin(17,mode=Pin.OUT)) # on prescise au programme que la pin 17 est une sortie de type PWN
pwm_led.freq(1_000) # dont la frequence est de 1000 (default)
pwm_led.duty_u16(10000) # on lui donne une valeur comprise entre 0  et 65535 qui est converti entre 0 et 3.3v
x = 11000 # declarer x

while True :
    if x == 11000 : #si la frequence x est 11000, tant qu'elle reste supérieure à 0, alors cette fréquence diminue de 1000 avec une intervalle de temps de 0.2sec
        while x > 0:
            x -= 1000  
            pwm_led.duty_u16(x)
            print (x)
            utime.sleep(.2)
    if x == 0: #si la frequence x est 0, tant qu'elle reste inférieur à 11000, alors cette fréquence augmente de 1000 avec une intervalle de temps de 0.2sec
        while x < 11000 :
            x += 1000	
            pwm_led.duty_u16(x)
            print(x)
            utime.sleep(.2)

from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import utime # importe dans le code la lib qui permet de gerer le temps

pwm_led_blue = PWM(Pin(16,mode=Pin.OUT)) # on prescise au programme que la pin 17 est une sortie de type PWN
pwm_led_green = PWM(Pin(17,mode=Pin.OUT))
pwm_led_red = PWM(Pin(18,mode=Pin.OUT))

pwm_led_blue.freq(1_000) # dont la frequence est de 1000 (default)
pwm_led_blue.duty_u16(0) # on lui donne une valeur comprise entre 0  et 65535 qui est converti entre 0 et 3.3v

pwm_led_green.freq(1_000)
pwm_led_green.duty_u16(0)

pwm_led_red.freq(1_000)
pwm_led_red.duty_u16(0)

x = 11000 # declarer x

while True :

    if x == 11000 : #si la frequence x est 11000, tant qu'elle reste supérieure à 0, alors cette fréquence diminue de 1000 avec une intervalle de temps de 0.2sec
        while x > 0:
            x -= 1000  
            pwm_led_red.duty_u16(x) #led rouge
            print (x)
            utime.sleep(.2) 
            
#allume puis éteint la led verte
    if x == 0:
        while x < 11000 : #si la frequence x est 0, tant qu'elle reste inférieur à 11000, alors cette fréquence augmente de 1000 avec une intervalle de temps de 0.2sec
            x += 1000	
            pwm_led_green.duty_u16(x) #led verte
            print(x)
            utime.sleep(.2)
        pwm_led_green.duty_u16(0)
    if x == 11000 : 
        while x > 0:
            x -= 1000  
            pwm_led_green.duty_u16(x)
            print (x)
            utime.sleep(.2)
#allume puis éteint la led bleu            
    if x == 0:
        while x < 11000 :
            x += 1000	
            pwm_led_blue.duty_u16(x) #led bleu
            print(x)
            utime.sleep(.2) 
    pwm_led_blue.duty_u16(0)

    if x == 11000 :
        while x > 0:
            x -= 1000  
            pwm_led_blue.duty_u16(x)
            print (x)
            utime.sleep(.2)
             
#allume puis éteint la led en violet           
    if x == 0 :
        while x < 11000:
            x += 1000  
            pwm_led_red.duty_u16(x)
            pwm_led_blue.duty_u16(x)
            print (x)
            utime.sleep(.2) 

    if x == 11000 :
        while x > 0:
            x -= 1000  
            pwm_led_red.duty_u16(x) 
            pwm_led_blue.duty_u16(x) #les deux couleurs donnent le violet
            print (x)
            utime.sleep(.2)
#allume puis éteint la led en blanc            
    if x == 0 :
        while x < 11000:
            x += 1000  
            pwm_led_red.duty_u16(x)
            pwm_led_blue.duty_u16(x)
            pwm_led_green.duty_u16(x) #les trois couleurs donnent le blanc
            print (x)
            utime.sleep(.2)
            
    if x == 11000 :
        while x > 0:
            x -= 1000  
            pwm_led_red.duty_u16(x)
            pwm_led_blue.duty_u16(x)
            pwm_led_green.duty_u16(x)
            print (x)
            utime.sleep(.2)
            
    if x == 0 :
        while x < 11000:
            x += 1000  
            pwm_led_red.duty_u16(x)
            print (x)
            utime.sleep(.2) 

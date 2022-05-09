
from time import sleep 
def unlock(pin_param):
    pin=pin_param
    for i in range (0,10):
        for j in range (10):
            for k in range(10):
                for l in range (10):
                    guess = str(i)+str(j)+str(k)+str(l)
                    print(guess)
                    sleep(0.001)
                    if guess==pin:
                        result = "El pin es: " + guess
                        return result 
print(unlock("2812"))
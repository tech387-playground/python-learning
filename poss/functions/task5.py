
import time




def pozivalica(vrijemeUms, okidac):
    vrijemeUms = vrijemeUms / 1000
    time.sleep(vrijemeUms)
    kvadrat = lambda x: x * x
    return kvadrat(okidac)


print(pozivalica(5000,5))
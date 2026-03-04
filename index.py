import math
import statistics
from datetime import datetime, timedelta

agora = datetime.now()
amanha = agora + timedelta(days=1)
print(agora)
print(amanha)


print(math.sqrt(25))

numeros = [2,4,1,8,10]
print(statistics.mean(numeros))
print(statistics.median(numeros))


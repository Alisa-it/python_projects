#  30. Рандомайзер

import random

ch = ['поесть', 'поспать', 'погулять с собакой', 'поучиться', 'покормить кота']
for i in range(3):
    print(random.choice(ch))
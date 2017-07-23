import random
import time
import webbrowser


url = ['http://youtu.be/kYtGl1dX5qI?t=13s',
       'https://www.youtube.com/watch?v=SDTZ7iX4vTQ',
       'https://youtu.be/tg00YEETFzg?t=50s',
       'https://youtu.be/e82VE8UtW8A',
       'https://youtu.be/KMOOr7GEkj8'
       ]


count = 0
sprint = 25
work_break = 5

while count <= 3:
    print(count)
    time.sleep(sprint * 60)
    webbrowser.open(url[random.randrange(6)], new=True, autoraise=True)
    time.sleep(work_break * 60)
    count += 1

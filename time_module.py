import time
# time.sleep
for i in range(4):
    print(f'Step {i+1} Passed ->')
    time.sleep(0.01)

# time.localtime
t = time.localtime()
formatted_time = time.strftime('%Y %m %d %H : %M : %S',t)
print(formatted_time)

# date_time module
from datetime import datetime
current_time = datetime.now()
print('Current Time:', current_time)

# time.time()
init = time.time()
print('Time to run program ',time.time() - init)

# calendar
import calendar

m = calendar.month_name[9]
print(m)

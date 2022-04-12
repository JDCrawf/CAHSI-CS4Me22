from tello import Tello
import time
import logging
from flightPath import Path  #we imported our custom code from flightPath

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')
log = logging.getLogger('Drone app')
log.info('Starting')

t = Tello()
p = Path()

try:
	start_battery = t.get_battery()
	print("Battery percentage: %s" % start_battery)
	t.takeoff() #"launch from airport"
	p.firstPathway() #navigate to the hospital
	t.land() #"land at hospital"
	t.takeoff() #leaving the hospital
	p.secondPathway() #navigate to the airport
	t.land() #landing at the airport

  

  
except Exception as e:
	log.error(e)
t.land()
end_battery = t.get_battery()
print("Battery percentage: %s" % end_battery)
print("Battery used for flight %s" % (start_battery - end_battery))

from tello import Tello


class Path:

  def __init__(self): #initialize the class
    t = Tello()

  def firstPathway(self): #move from airport to hospital
    self.firstTowerLoop()
    self.overSecondTowers()
    self.aroundWindTunnel()
    self.approachHospital()

  def secondPathway(self): #move from hospital to airport
    self.leavingHospital()
    self.approachAirport()

  def firstTowerLoop(): #after takeoff go through loop +2pnt
    t.move_down(2)
    t.move_forward(50)

  def overSecondTowers(): #after going through loop, approach and move over red towers 
    t.move_forward(68)
    t.rotate_cw(45)
    t.move_forward(72)

  def aroundWindTunnel(): #move around wind tunnel and face hospital
    t.move_forward(50)
    t.rotate_cw(135)

  def approachHospital(): #move above hospital
    t.move_forward(68)

  def leavingHospital(): #leaving the hospital after relaunching
    t.move_forward(41)
    t.rotate_ccw(90)

  def approachAirport(): #move through the city and arrive over airport
    t.move_forward(72)
    t.move_right(15)
    t.move_forward(32)
    t.rotate_ccw(90)
    t.move_backward(57)


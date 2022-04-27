from tello import Tello

class Path:

  def __init__(self, t): #initialize the class
    self.t = t

  def firstPathway(self): #move from airport to hospital
    self.firstTowerLoop()
    self.overSecondTowers()
    self.aroundWindTunnel()
    self.approachHospital()

  def secondPathway(self): #move from hospital to airport
    self.leavingHospital()
    self.approachAirport()

  def firstTowerLoop(self): #"after takeoff go through loop +2pnt"
    self.t.move_down(2)
    self.t.move_forward(50)
    
  def overSecondTowers(self): #"after going through loop, approach and move over red towers" 
    self.t.move_forward(68)
    self.t.rotate_cw(45)
    self.t.move_forward(72)

  def aroundWindTunnel(self): #"move around wind tunnel and face hospital"
    self.t.move_forward(50)
    self.t.rotate_cw(135)

  def approachHospital(self): #"move above hospital"
    self.t.move_forward(68)

  def leavingHospital(self): #leaving the hospital after relaunching
    self.t.move_forward(41)
    self.t.rotate_ccw(90)

  def approachAirport(self): #move through the city and arrive over airport
    self.t.move_forward(72)
    self.t.move_right(15)
    self.t.move_forward(32)
    self.t.rotate_ccw(90)
    self.t.move_backward(57)


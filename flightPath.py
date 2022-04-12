from tello import Tello


class Path: 
  
  def firstPathway(): #move from airport to hospital
    firstTowerLoop()
    overSecondTowers()
    aroundWindTunnel()
    approachHospital()

  def secondPathway(): #move from hospital to airport
    leavingHospital()
    approachAirport()
    
    
  def firstTowerLoop(): #"after takeoff go through loop +2pnt"
    d.move_down(2)
    d.move_forward(50)

  def overSecondTowers(): #"after going through loop, approach and move over red towers" 
    d.move_forward(68)
    d.rotate_cw(45)
    d.move_forward(72)

  def aroundWindTunnel(): #"move around wind tunnel and face hospital"
    d.move_forward(50)
    d.rotate_cw(135)

  def approachHospital(): #"move above hospital"
    d.move_forward(68)

  def leavingHospital(): #leaving the hospital after relaunching
    d.move_forward(41)
    d.rotate_ccw(90)

  def approachAirport(): #move through the city and arrive over airport
    d.move_forward(72)
    d.move_right(15)
    d.move_forward(32)
    d.rotate_ccw(90)
    d.move_backward(57)
    

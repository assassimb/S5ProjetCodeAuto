'''
**********************************************************************
* Filename    : projet
* Description : Essai et tests afin de resoudre la problematique
* Author      : Assim et co
**********************************************************************
'''

from SunFounder_Line_Follower import Line_Follower
from picar import front_wheels
from picar import back_wheels
import time
import picar

picar.setup()

REFERENCES = [200, 200, 200, 200, 200]
lf = Line_Follower.Line_Follower()
lf.references = REFERENCES

forward_speed = 80
backward_speed = 70
turning_angle = 40

delay = 0.0005

fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
fw.ready()
bw.ready()

def main():
        bw.speed = forward_speed
        print(lf.read_analog())



'''

Aucune caliss d'idee de ce que jfais a partir d'ici genre

'''

def destroy():
    bw.stop()
    fw.turn(90)

if __name__ == '__main__':
    try:
        try:
            while True:
                main()
                #straight_run()
        except Exception as e:
            print(e)
            print('error try again in 5')
            destroy()
            time.sleep(5)
    except KeyboardInterrupt:
        destroy()
        

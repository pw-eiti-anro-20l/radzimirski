#!/usr/bin/env python
import rospy
import curses
from geometry_msgs.msg import Twist

#metoda turtle_publisher - do publikacji wiadomosci o sterowaniu dla zolwia
def turtle_publisher():

    rospy.loginfo("in turtle_publisher")
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=5)
    rospy.init_node('turtlepub', anonymous=True)
    rate = rospy.Rate(40)

    stdcr = curses.initscr()
    stdcr.nodelay(1)

    controlButtons = rospy.get_param('turtlepub')
    rospy.loginfo("setup done")
 
#glowna petla sterowania zolwiem, wykonujaca sia gdy wlaczony jest rospy
    while not rospy.is_shutdown():
        
	#pobranie wiadomosci o wcisnietym przycisku
        button = stdcr.getch()
	
	#ustawienie wiadomosci
        TurtleMsg = Twist()
	if button == ord(controlButtons['fwd']):
            TurtleMsg.linear.x = 1.5
	    TurtleMsg.angular.z = 0.0
        elif button == ord(controlButtons['tr']):
            TurtleMsg.angular.z = -1.5
	    TurtleMsg.angular.x = 0.0
        elif button == ord(controlButtons['tl']):
            TurtleMsg.angular.z = 1.5
	    TurtleMsg.angular.x = 0.0
        elif button == ord(controlButtons['bck']):
            TurtleMsg.linear.x = -1.5
	    TurtleMsg.angular.z = 0.0
	else:
	    TurtleMsg.linear.x = 0.0
	    TurtleMsg.angular.z = 0.0
	
	#publikacja wiadomosci po ustawieniu wlasciwosci sterowania zolwia
        pub.publish(TurtleMsg)
        rate.sleep()

if __name__ == '__main__':

    launchstr = "node running"
    excstr = "Shutdown!"

    #sprawdzanie, czy udalo sie prawidlowo uruchomic rospy
    rospy.loginfo(launchstr)
    try:
        turtle_publisher()
    except rospy.ROSInterruptException:
        rospy.loginfo(excstr)






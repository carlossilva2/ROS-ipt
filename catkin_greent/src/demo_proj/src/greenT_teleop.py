#!/usr/bin/env python
import rospy
import roslib
from std_msgs.msg import Int16
from geometry_msgs.msg import Twist 

#############################################################
#############################################################
class GreenTteleop():
#############################################################
#############################################################

    #############################################################
    def __init__(self):
    #############################################################
        rospy.init_node("greenT_teleop")
        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)
    
        self.w = rospy.get_param("~base_width", 0.23)
    
        self.pub_lmotor = rospy.Publisher('lwheel_vtarget', Int16, queue_size=10)
        self.pub_rmotor = rospy.Publisher('rwheel_vtarget', Int16, queue_size=10)
        rospy.Subscriber('twist', Twist, self.twistCallback)
    
    
        self.rate = rospy.get_param("~rate", 30)
        self.timeout_ticks = rospy.get_param("~timeout_ticks", 10)
        self.left = 0
        self.right = 0
        
    #############################################################
    def spin(self):
    #############################################################
    
        r = rospy.Rate(self.rate)
        idle = rospy.Rate(30)
        then = rospy.Time.now()
        self.ticks_since_target = self.timeout_ticks
    
        ###### main loop  ######
        while not rospy.is_shutdown():
        
            while not rospy.is_shutdown() and self.ticks_since_target < self.timeout_ticks:
                self.spinOnce()
                r.sleep()
            idle.sleep()
                
    #############################################################
    def spinOnce(self):
    #############################################################
    
        # dx = (l + r) / 2
        # dr = (r - l) / w
            
        self.right = 1.0 * self.dx + self.dr * self.w / 2 
        self.left = 1.0 * self.dx - self.dr * self.w / 2
        # rospy.loginfo("publishing: (%d, %d)", left, right) 
                
        self.pub_lmotor.publish(self.left)
        self.pub_rmotor.publish(self.right)
            
        self.ticks_since_target += 1

    #############################################################
    def twistCallback(self,msg):
    #############################################################
        # rospy.loginfo("-D- twistCallback: %s" % str(msg))
        self.ticks_since_target = 0
        self.dx = msg.linear.x
        self.dr = msg.angular.z
        self.dy = msg.linear.y

if __name__ == '__main__':
    
    try:
        GreenTteleop = GreenTteleop()
        GreenTteleop.spin()
    except rospy.ROSInterruptException:
        pass
#import the necessary modules
from convert import *
from time import sleep
import freenect
import cv2
import numpy as np
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
import sys
import roslib
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

class image_converter:
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_color",Image,self.callback)

    def callback(self,data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "rgb8")
            cv2.imwrite("frame.jpg", cv_image)
            self.decision = processimage()
            print self.decision
        except CvBridgeError:
            pass
    

    
    

"""def callback(data):
    #twist = Twist()
    convertArray2Img(data)
    #twist.linear.x = 255*data.axes[1]
    #twist.angular.z = -255*data.axes[0]
    #pub.publish(twist)


def start():
        
    global pub
    pub = rospy.Publisher('twist', Twist, queue_size=10)
    rospy.Subscriber("camera/rgb/image_mono", Image, callback) #penso que seja camera
    rospy.init_node('greenT_Kinect')
    #rate = rospy.get_param('~rate',30)

    rospy.spin()

if __name__ == '__main__':
    start()"""
def main(args):
    ic = image_converter()
    rospy.init_node('image_converter', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down"

if __name__ == '__main__':
    main(sys.argv)

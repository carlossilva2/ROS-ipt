#!/usr/bin/env python
import roslib
import sys 
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:
  
  def __init__(self):
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera/rgb/image_mono",Image,self.callback)
    self.i = 0

  def callback(self,data):
    try:
        cv_image = self.bridge.imgmsg_to_cv2(data, "mono8")
        cv2.imwrite("img/frame{0}.jpg".format(self.i), cv_image)
        print "image saved!"
        self.i += 1
    except CvBridgeError:
        pass

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print "Shutting down"

if __name__ == '__main__':
    main(sys.argv)

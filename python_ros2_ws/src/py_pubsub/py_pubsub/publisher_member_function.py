import rclpy
import struct
import threading
from rclpy.node import Node
from std_msgs.msg import String

#global variables
joy_event = [0,0,0,0]
m_joy = [0,0]

############  read joystick callback  ###################        
#read joystick thread
def readJoystick():
    # count = 3
    with open("/dev/input/js0", "rb") as f:
        while True:
            a = f.read(8)
            t, value, code, index = list(struct.unpack("<Ihbb", a))
            print("t: {:10d} ms, value: {:6d}, code: {:1d}, index: {:1d}".format(t, value, code, index))
            global m_joy
            if code == 2:
                if index == 0 or index == 1:
                    m_joy[index] = value
            else:
                pass

############  ros publish thread  ###################
class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')

        #ros publisher
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        # self.i = 0
        # read joystick thread
        self.thread = threading.Thread(target=readJoystick)
        self.thread.start()

    def timer_callback(self):
        msg = String()
        msg.data = "x: {:6d}, y: {:6d}".format(m_joy[0], m_joy[1])
        self.publisher_.publish(msg)
        # self.get_logger().info('Publishing: "%s"' % msg.data)
        # self.i += 1


def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

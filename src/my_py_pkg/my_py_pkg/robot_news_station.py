#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station")
        self.declare_parameter("name", "MARK")
        self.robot_name = self.get_parameter("name").value
        self.publisher = self.create_publisher(String, "robot_news", 10)
        self.timer = self.create_timer(2, self.publish_news)
        self.get_logger().info("Robot News Station has been started!")

    def publish_news(self):
        msg = String()
        msg.data = f"Hello, this is {self.robot_name} from the Robot News Station!"
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

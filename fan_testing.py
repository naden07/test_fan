import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fan import Fan

def main():
    print("==========================================")
    print("   APPLIANCE CONTROL INTERFACE v1.0  ")
    print("==========================================\n")

    fan1 = Fan()
    fan1.set_speed(Fan.FAST)
    fan1.set_radius(10.0)
    fan1.set_color("yellow")
    fan1.set_on(True)

    fan2 = Fan()
    fan2.set_speed(Fan.MEDIUM)
    fan2.set_radius(5.0)
    fan2.set_color("blue")
    fan2.set_on(False)

    print("UNIT 01 CONFIGURATION:")
    print(fan1.display_dashboard())
    print()

    print("UNIT 02 CONFIGURATION:")
    print(fan2.display_dashboard())
    print("\n==========================================")

if __name__ == "__main__":
    main()
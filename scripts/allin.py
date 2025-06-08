from xarm import Controller, Servo
import time

arm = Controller('USB')

def move_sequence():
    s1 = Servo(1, 500)
    s2 = Servo(2, 500)
    s3 = Servo(3, 500)
    s4 = Servo(4, 500)
    s5 = Servo(5, 500)
    s6 = Servo(6, 500)
    arm.setPosition([s1, s2, s3, s4, s5, s6], duration=1000, wait=True)

    print("[INFO] Step 1: Setting servo 5 to 380, servo 4 to 0, servo 1 to 0...")
    s1 = Servo(1, 0)
    s4 = Servo(4, 0)
    s5 = Servo(5, 380)
    arm.setPosition([s1, s4, s5], duration=1000, wait=True)
    time.sleep(0.5)

    print("[INFO] Step 2: Setting servo 5 to 850...")
    s5 = Servo(5, 850)
    arm.setPosition([s5], duration=1000, wait=True)
    time.sleep(0.5)

    print("[INFO] Step 3: Setting servo 4 to 340...")
    s4 = Servo(4, 340)
    arm.setPosition([s4], duration=1000, wait=True)
    time.sleep(0.5)

    print("[INFO] Step 4: Returning to home position...")
    s1 = Servo(1, 500)
    s2 = Servo(2, 500)
    s3 = Servo(3, 500)
    s4 = Servo(4, 500)
    s5 = Servo(5, 500)
    s6 = Servo(6, 500)
    arm.setPosition([s1, s2, s3, s4, s5, s6], duration=1000, wait=True)
    print("[INFO] Sequence complete.")

if __name__ == "__main__":
    move_sequence()

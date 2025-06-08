from xarm import Controller, Servo
import time

arm = Controller('USB')

# Servo behavior:
# 1 (claw): bigger number = closed
# 2 (angle): bigger number = right
# 3 (wrist): smaller number = forward
# 4 (elbow): smaller number = back
# 5 (shoulder): bigger number = back
# 6 (base): bigger number = rotate left

range_map = {
    1: (0, 700),
    2: (0, 1000),
    3: (0, 1000),
    4: (0, 1000),
    5: (0, 850),
    6: (0, 1000)
}

opened = 0
closed = 700

current_positions = {i: 500 for i in range(1, 7)}

def clamp(joint, pos):
    lo, hi = range_map[joint]
    return max(lo, min(pos, hi))

def move_all(joint_positions, duration=2000):
    servos = [Servo(joint, pos) for joint, pos in joint_positions.items()]
    arm.setPosition(servos, duration=duration, wait=True)

def move_joint(joint_number, position, duration=1000):
    old = current_positions[joint_number]
    new = clamp(joint_number, position)
    print(f"[INFO] Moving joint {joint_number} from {old} to {new}...")
    current_positions[joint_number] = new
    move_all(current_positions, duration)
    time.sleep(0.001)
    print(f"[INFO] Joint {joint_number} now at {new}.")


def press_button():
    print("[INFO] Pressing button with shoulder movement...")
    original = current_positions[shoulder]

    # Move to button-press position
    move_joint(shoulder, 650, duration=300)

    # Wait briefly to simulate pressing
    print("[INFO] Simulating button press...")
    time.sleep(0.001)
    print("[INFO] Button pressed.")

    # Return to original position
    move_joint(shoulder, original, duration=300)

    print("[INFO] Button press complete.")

def set_initial_pose():
    print("[INFO] Setting initial pose...")
    initial = {
        1: 700,
        2: 88,
        3: 632,
        4: 205,
        5: 500,
        6: 864
    }
    for j, pos in initial.items():
        current_positions[j] = clamp(j, pos)
    move_all(current_positions)
    print("[INFO] Initial pose set.")

claw = 1
hand = claw
angle = 2
wrist = 3
elbow = 4
shoulder = 5
base = 6
bottom = base

if __name__ == "__main__":

    s1 = Servo(1, 500)
    s2 = Servo(2, 500)
    s3 = Servo(3, 500)
    s4 = Servo(4, 500)
    s5 = Servo(5, 500)
    s6 = Servo(6, 500)
    arm.setPosition([s1, s2, s3, s4, s5, s6], duration=1000, wait=True)

    while True:
        set_initial_pose()
        press_button()
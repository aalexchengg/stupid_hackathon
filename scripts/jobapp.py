from xarm import Controller, Servo
import time
import threading
import subprocess
import os
import signal

arm = Controller('USB')

def shake_servo6(cycles=10, delay=0.2, duration=200):
    for i in range(cycles):
        print(f"[SHAKE] Cycle {i+1}: Move to 400")
        arm.setPosition(Servo(6, 400), duration=duration, wait=True)
        time.sleep(delay)
        print(f"[SHAKE] Cycle {i+1}: Move to 600")
        arm.setPosition(Servo(6, 600), duration=duration, wait=True)
        time.sleep(delay)
    print("[SHAKE] Shake complete.")

def play_audio_async(filepath):
    print(f"[AUDIO] Playing audio: {filepath}")
    return subprocess.Popen(['afplay', filepath])

def stop_audio(proc):
    if proc and proc.poll() is None:
        print("[AUDIO] Stopping audio playback...")
        os.kill(proc.pid, signal.SIGTERM)

def setup_and_shake():
    audio_proc = play_audio_async(os.path.abspath("static/awwhellnah.mp3"))  # replace with your file path

    print("[INFO] Starting initial positioning of servos 1–5, and 6 to 500")
    servos_init = [
        Servo(1, 0),
        Servo(2, 551),
        Servo(3, 928),
        Servo(4, 413),
        Servo(5, 500),
        Servo(6, 500)
    ]

    shake_thread = threading.Thread(target=shake_servo6, args=(7, 0.2, 200))
    shake_thread.start()

    arm.setPosition(servos_init, duration=500, wait=True)
    print("[INFO] Initial positioning complete.")

    shake_thread.join()
    print("[INFO] All movements complete.")

    stop_audio(audio_proc)

    print("[INFO] Returning to home position...")
    home_servos = [
        Servo(1, 500),
        Servo(2, 500),
        Servo(3, 500),
        Servo(4, 500),
        Servo(5, 500),
        Servo(6, 500)
    ]
    arm.setPosition(home_servos, duration=500, wait=True)
    print("[INFO] Returned to home.")

if __name__ == "__main__":
    setup_and_shake()

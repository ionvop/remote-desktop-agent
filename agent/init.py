import requests
import config


def main() -> None:
    data = {
        "command": None,
        "screen": ""
    }

    requests.put(config.JSONBLOB_URL, json=data)
    print("JSONBLOB initialized")


if __name__ == "__main__":
    main()
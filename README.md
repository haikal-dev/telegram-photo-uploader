# Telegram Photo Uploader

A simple Python script to upload and send photos to a Telegram bot.

## Description

This script allows you to send a photo to a specified Telegram chat using the Telegram Bot API. You provide the path to the photo as a command-line argument, and the script takes care of uploading the photo to the specified chat.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/haikal-dev/telegram-photo-uploader.git
    cd telegram-photo-uploader
    ```

2. Install the required Python library:

    ```bash
    pip3 install requests
    ```

## Usage

1. Set your Telegram bot token and the chat ID in the script:

    ```python
    token = "YOUR_BOT_TOKEN"
    receiver = "CHAT_ID"
    ```

2. Run the script with the path to the photo you want to send:

    ```bash
    ./telegram-jpg.py /path/to/photo.jpg
    ```

    Example:

    ```bash
    ./telegram-jpg.py myphoto.jpg
    ```

## Contributing
1. Fork the repository.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a pull request.

## License

Distributed under the MIT License.
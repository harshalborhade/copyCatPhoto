# CopyCat: Your Purr-fect Clipboard Companion 

CopyCat is a simple Python application that fetches a random cat picture from the internet and automatically copies it to your clipboard.  This allows you to quickly paste a delightful feline image into your chats, documents, or anywhere else you need a dose of kitty cuteness!

## Features

*   **One-Click Cat Pictures:**  Fetches a random cat image with a single run.
*   **Clipboard Integration:** Seamlessly copies the image to your clipboard for easy pasting.
*   **Powered by the Cat API:** Uses the The Cat API to source a wide variety of cat pictures.

## Prerequisites

*   Python 3
*   `PIL` (Pillow) library: `pip install Pillow`
*   `pywin32` library: `pip install pywin32` (only required on Windows)

## Installation

1.  Clone the repository:

    ```bash
    git clone [your_repo_url]
    cd [your_repo_directory]
    ```

2.  Install the necessary dependencies:

    ```bash
    pip install Pillow pywin32
    ```

## Usage

1.  Run the script:

    ```bash
    python copy_cat_to_clipboard.py
    ```

2.  A random cat picture is now in your clipboard! Paste it wherever you like (e.g., Ctrl+V in Windows).

## API Key

The application uses an API key from The Cat API.  The current key is included in the script.  If you encounter issues or want to increase your usage limits, you can obtain your own free API key from [The Cat API](https://thecatapi.com/) and replace the `api_key` variable in the `copy_cat_to_clipboard.py` file.

## Troubleshooting

*   **Windows-Specific:** This application is primarily designed for Windows due to its use of the `win32clipboard` library.
*   **Dependencies:** Ensure that you have correctly installed the required dependencies (`Pillow` and `pywin32`).
*   **API Key:**  If you're having issues fetching images, double-check that your API key is valid.
*   **Clipboard Issues:**  Some applications might not support pasting images directly from the clipboard.

## Contributing

Contributions are welcome!  Feel free to submit issues or pull requests for improvements or bug fixes.

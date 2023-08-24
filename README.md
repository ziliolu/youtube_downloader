# YouTube Downloader

<p align="center">
  <img src="https://img.shields.io/github/languages/top/ziliolu/youtube_downloader?color=#FFFFFF&style=flat-square" />
  <img src="https://img.shields.io/badge/status-completed-blue?color=#FFFFFF&style=flat-square" />
  <img src="https://img.shields.io/github/last-commit/ziliolu/youtube_downloader?color=#FFFFFF&style=flat-square" />
</p>

## About
This is a Python script that allows you to download YouTube videos by providing a valid YouTube link. It uses the `pytube` library to fetch the video and download it in the highest resolution available.

## Prerequisites

- Python 3.x
- `pytube` library (`pip install pytube`)

## Usage

1. Run the script (`python3 downloader.py`).
2. Enter a valid YouTube link when prompted.
3. The script will fetch the video details, download the video, and save it in the `downloaded_videos` directory.

## Script Explanation

The script performs the following steps:

1. **Imports required modules:**

   - `pytube.YouTube`: Allows fetching video details and streams.
   - `pytube.exceptions.RegexMatchError`: Catches invalid YouTube link exceptions.
   - `pytube.exceptions.AgeRestrictedError`: Catches age-restricted video exceptions.

2. **Prompts for YouTube link:**

   - Takes user input for a valid YouTube link.

3. **Downloads the video:**

   - Tries to fetch the video using `pytube.YouTube`.
   - Prints the video title and number of views.
   - Fetches the highest resolution video stream using `.streams.get_highest_resolution()`.
   - Downloads the video and saves it in the `downloaded_videos` directory.

4. **Exception Handling:**

   - Catches `RegexMatchError` if the provided link format is invalid.
   - Catches `AgeRestrictedError` if the video is age-restricted.

## Notes

- The script uses the `pytube` library to interact with YouTube's servers and fetch video data.
- Be cautious when downloading copyrighted content; make sure to follow YouTube's terms of use.

Feel free to customize the script, add more features, or improve the user experience to suit your needs.


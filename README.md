# Smart Calendar — APC

## Overview

A smart desktop calendar assistant that combines Google Calendar integration, real-time weather data, voice-controlled input, and desktop notifications into a single application. Built in January 2022 during postgraduate studies at Vrije Universiteit Brussel.

---

## Features

### Google Calendar Integration
- Reads upcoming events from your primary Google Calendar (next 50 events)
- Creates new calendar events with email and popup reminders
- Full OAuth2 authentication flow — authorizes once, stores token for subsequent runs
- Read-only calendar scope by default (`calendar.readonly`)

### Weather Data
- Fetches real-time temperature and weather conditions via OpenWeatherMap API
- Returns temperature, feels-like, humidity, pressure, wind speed, and weather description
- Configurable city in `weather.py`

### Voice Input
- Microphone-based speech recognition via Google Speech Recognition API
- Listens for voice commands to control calendar actions
- Graceful handling of unrecognised audio and service interruptions

### Desktop Notifications
- System-level push notifications via `plyer`
- Configurable title, message, and display duration
- Works cross-platform (Windows, macOS, Linux)

---

## Setup

### 1. Google Calendar Credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project
3. Enable the **Google Calendar API**
4. Create **OAuth 2.0 Client Credentials** (Desktop application type)
5. Download the credentials JSON file
6. Rename it to `credentials.json` and place it in `api/creds/`

Use `api/creds/credentials.json.example` as a reference for the expected format.

> `token.json` is generated automatically after the first successful OAuth login. Do not commit it to version control.

### 2. OpenWeatherMap API Key
1. Register at [openweathermap.org](https://openweathermap.org/api)
2. Copy your API key
3. Open `api/weather.py` and replace `your_openweathermap_api_key_here` with your key
4. Update the `CITY` variable to your location

### 3. Install Dependencies

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
pip install requests
pip install SpeechRecognition pyaudio
pip install plyer
```

> **PyAudio on Windows:** Install via pre-compiled wheel from [Christoph Gohlke's repository](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) if `pip install pyaudio` fails.

---

## Project Structure

```
Smat_calendar_APC/
├── api/
│   ├── creds/
│   │   ├── credentials.json.example   # Template — copy and fill with your credentials
│   │   └── token.json                 # Auto-generated after first OAuth login (git-ignored)
│   ├── gcal.py                        # Google Calendar API integration
│   └── weather.py                     # OpenWeatherMap API integration
├── main.py                            # Main application entry point
├── notification.py                    # Desktop notification handler
├── speech.py                          # Voice input / speech recognition
└── events                             # Local event data
```

---

## Security Notes

**Never commit real credentials to version control.**

- `credentials.json` — add to `.gitignore`
- `token.json` — add to `.gitignore`
- API keys — use environment variables or a `.env` file

This repo uses a `.gitignore` to exclude real credential files and provides `.example` templates instead.

---

## Tech Stack

- **Language:** Python
- **Calendar:** Google Calendar API v3 · OAuth2
- **Weather:** OpenWeatherMap REST API
- **Voice:** SpeechRecognition · Google Speech Recognition
- **Notifications:** plyer
- **Environment:** PyCharm / local Python

---

## Author

**Tanjil Hasan**
github.com/tanjilh136 · linkedin.com/in/tanjil-hasan-650246169

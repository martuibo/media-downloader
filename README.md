# Media Downloader 🎵🎬

A simple, powerful Python CLI tool to download audio and video from SoundCloud, YouTube, and hundreds of other platforms.

## Features

- 🎵 Download audio from URLs (SoundCloud, YouTube, etc.) as MP3, M4A, WAV, and more
- 🎬 Download videos in best quality with automatic format merging
- 📋 Get media information without downloading
- 🎯 Simple command-line interface
- 🌐 Supports 1000+ websites via yt-dlp
- 📁 Organized output with customizable directories

## Supported Platforms

This tool supports any platform that yt-dlp supports, including:
- SoundCloud
- YouTube
- Vimeo
- Twitter/X
- Instagram
- TikTok
- Facebook
- And [hundreds more](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

## Prerequisites

- Python 3.7 or higher
- FFmpeg (for audio conversion)

### Installing FFmpeg

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) or use:
```bash
winget install FFmpeg
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/media-downloader.git
cd media-downloader
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Download Audio (MP3)
```bash
python src/downloader.py -a "https://soundcloud.com/artist/track"
```

### Download Video
```bash
python src/downloader.py -v "https://youtube.com/watch?v=dQw4w9WgXcQ"
```

### Specify Output Directory
```bash
python src/downloader.py -a "https://..." -o ./my_music
```

### Different Audio Format
```bash
python src/downloader.py -a "https://..." -f m4a
```

### Get Media Information
```bash
python src/downloader.py -i "https://..."
```

## Command Line Options
```
positional arguments:
  url                   URL to download from

options:
  -h, --help            Show help message
  -a, --audio           Download audio only (default: MP3)
  -v, --video           Download video
  -f, --format FORMAT   Audio format (mp3, m4a, wav, etc.) - default: mp3
  -q, --quality QUALITY Video quality (best, worst) - default: best
  -o, --output OUTPUT   Output directory - default: downloads
  -i, --info            Get info about URL without downloading
```

## Examples

### Download SoundCloud track as MP3
```bash
python src/downloader.py -a "https://soundcloud.com/artist/amazing-track"
```

### Download YouTube video
```bash
python src/downloader.py -v "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### Download to specific folder
```bash
python src/downloader.py -a "https://soundcloud.com/..." -o ~/Music/SoundCloud
```

### Download audio as WAV (high quality)
```bash
python src/downloader.py -a "https://..." -f wav
```

### Check video info before downloading
```bash
python src/downloader.py -i "https://youtube.com/watch?v=..."
```

## Project Structure
```
media-downloader/
├── src/
│   └── downloader.py      # Main CLI application
├── tests/                 # Unit tests (optional)
├── downloads/             # Default download directory (created automatically)
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore           # Git ignore rules
```

## How It Works

This tool uses [yt-dlp](https://github.com/yt-dlp/yt-dlp), a powerful fork of youtube-dl, to:
1. Extract media URLs from various platforms
2. Download the best available quality
3. Convert audio to your preferred format using FFmpeg
4. Save files with clean, organized names

## Troubleshooting

### "FFmpeg not found"
Install FFmpeg using the instructions in the Prerequisites section.

### "ERROR: Unsupported URL"
Check if the platform is supported by visiting the [yt-dlp supported sites list](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

### Downloads are slow
This depends on your internet connection and the source platform. yt-dlp optimizes download speeds automatically.

## Legal Notice

This tool is for personal use only. Please respect copyright laws and terms of service of the platforms you download from. Only download content you have the right to download.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this tool for personal projects.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The amazing downloader engine
- [FFmpeg](https://ffmpeg.org/) - For media conversion

## Support

If you encounter any issues, please open an issue on GitHub.
#!/usr/bin/env python3
"""
Media Downloader - Download audio and video from various platforms
Supports SoundCloud, YouTube, and hundreds of other sites via yt-dlp
"""

import argparse
import sys
from pathlib import Path
import yt_dlp


class MediaDownloader:
    """Handler for downloading media from URLs"""
    
    def __init__(self, output_dir: str = "downloads"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def download_audio(self, url: str, format: str = "mp3", allow_playlist: bool = False) -> bool:
        """
        Download audio from URL and convert to specified format
        
        Args:
            url: The URL to download from
            format: Audio format (mp3, m4a, wav, etc.)
            allow_playlist: If True, download entire playlist; if False, only single video
        
        Returns:
            bool: True if successful, False otherwise
        """
        output_template = str(self.output_dir / "%(title)s.%(ext)s")
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': not allow_playlist,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': format,
                'preferredquality': '192',
            }],
            'outtmpl': output_template,
            'quiet': False,
            'no_warnings': False,
            'extractor_args': {
                'youtube': {
                    'player_client': ['android', 'web'],
                    'skip': ['dash', 'hls']
                }
            },
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"\n🎵 Downloading audio from: {url}")
                ydl.download([url])
                print(f"✅ Successfully downloaded audio to: {self.output_dir}")
                return True
        except Exception as e:
            print(f"❌ Error downloading audio: {e}", file=sys.stderr)
            return False
    
    def download_video(self, url: str, quality: str = "best", allow_playlist: bool = False) -> bool:
        """
        Download video from URL
        
        Args:
            url: The URL to download from
            quality: Video quality (best, worst, or specific format)
            allow_playlist: If True, download entire playlist; if False, only single video
        
        Returns:
            bool: True if successful, False otherwise
        """
        output_template = str(self.output_dir / "%(title)s.%(ext)s")
        
        ydl_opts = {
            'format': f'{quality}video+bestaudio/best' if quality == 'best' else quality,
            'noplaylist': not allow_playlist,
            'outtmpl': output_template,
            'quiet': False,
            'no_warnings': False,
            'merge_output_format': 'mp4',
            'extractor_args': {
                'youtube': {
                    'player_client': ['android', 'web'],
                    'skip': ['dash', 'hls']
                }
            },
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"\n🎬 Downloading video from: {url}")
                ydl.download([url])
                print(f"✅ Successfully downloaded video to: {self.output_dir}")
                return True
        except Exception as e:
            print(f"❌ Error downloading video: {e}", file=sys.stderr)
            return False
    
    def get_info(self, url: str) -> dict:
        """
        Get information about a URL without downloading
        
        Args:
            url: The URL to get info from
        
        Returns:
            dict: Video/audio information
        """
        ydl_opts = {'quiet': True}
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(url, download=False)
        except Exception as e:
            print(f"❌ Error getting info: {e}", file=sys.stderr)
            return {}


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Download audio and video from various platforms",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Download audio as MP3
  python downloader.py -a "https://soundcloud.com/artist/track"
  
  # Download video
  python downloader.py -v "https://youtube.com/watch?v=..."
  
  # Specify output directory
  python downloader.py -a "https://..." -o ./my_music
  
  # Get info without downloading
  python downloader.py -i "https://..."
        """
    )
    
    parser.add_argument("url", nargs="?", help="URL to download from")
    parser.add_argument("-a", "--audio", action="store_true", 
                       help="Download audio only (default: MP3)")
    parser.add_argument("-v", "--video", action="store_true",
                       help="Download video")
    parser.add_argument("-f", "--format", default="mp3",
                       help="Audio format (mp3, m4a, wav, etc.) - default: mp3")
    parser.add_argument("-q", "--quality", default="best",
                       help="Video quality (best, worst) - default: best")
    parser.add_argument("-o", "--output", default="downloads",
                       help="Output directory - default: downloads")
    parser.add_argument("-i", "--info", action="store_true",
                       help="Get info about URL without downloading")
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.url:
        parser.print_help()
        sys.exit(1)
    
    if not (args.audio or args.video or args.info):
        print("❌ Error: Please specify -a (audio), -v (video), or -i (info)")
        parser.print_help()
        sys.exit(1)
    
    # Create downloader instance
    downloader = MediaDownloader(output_dir=args.output)
    
    # Execute requested action
    if args.info:
        print(f"📋 Getting info for: {args.url}")
        info = downloader.get_info(args.url)
        if info:
            print(f"\nTitle: {info.get('title', 'N/A')}")
            print(f"Uploader: {info.get('uploader', 'N/A')}")
            print(f"Duration: {info.get('duration', 'N/A')} seconds")
            print(f"Description: {info.get('description', 'N/A')[:200]}...")
    elif args.audio:
        success = downloader.download_audio(args.url, format=args.format)
        sys.exit(0 if success else 1)
    elif args.video:
        success = downloader.download_video(args.url, quality=args.quality)
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
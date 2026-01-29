"""
Build script to create executable file using PyInstaller
Run this file to generate the .exe
"""

import PyInstaller.__main__
import sys
from pathlib import Path

def build_exe():
    """Build the executable"""
    
    print("=" * 60)
    print("Building Media Downloader executable...")
    print("=" * 60)
    
    # PyInstaller arguments
    args = [
        'src/gui.py',                          # Your main script
        '--name=MediaDownloader',              # Name of the exe
        '--onefile',                           # Create a single exe file
        '--windowed',                          # No console window (GUI only)
        '--add-data=src/downloader.py;src',    # Include the downloader module (Windows)
        '--clean',                             # Clean PyInstaller cache
        '--noconfirm',                         # Overwrite output directory without asking
        # You can add an icon later with: '--icon=icon.ico',
    ]
    
    print("\nStarting build process...")
    print("This may take a few minutes...\n")
    
    PyInstaller.__main__.run(args)
    
    print("\n" + "=" * 60)
    print("✅ Build complete!")
    print("=" * 60)
    print(f"\nYour executable is located in: {Path('dist').absolute()}")
    print("File name: MediaDownloader.exe")
    print("\nYou can now distribute this file to users!")
    print("=" * 60)

if __name__ == "__main__":
    build_exe()
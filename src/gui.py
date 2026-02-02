#!/usr/bin/env python3
"""
Media Downloader GUI - Graphical interface for downloading audio and video
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
from pathlib import Path
import sys
from downloader import MediaDownloader


class MediaDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Meedia tööriist 🎵🎬")
        self.root.geometry("600x550")
        self.root.resizable(False, False)
        
        # Set a neutral background color
        self.root.configure(bg="#f5f5f5")
        
        # Set icon if available (optional)
        try:
            self.root.iconbitmap('icon.ico')
        except:
            pass
        
        # Variables
        self.url_var = tk.StringVar()
        self.output_var = tk.StringVar(value="")
        self.format_var = tk.StringVar(value="mp3")
        self.download_type = tk.StringVar(value="audio")
        self.playlist_var = tk.BooleanVar(value=False)
        self.status_var = tk.StringVar(value="Valmis")
        
        self.setup_ui()
        
    def create_context_menu(self, widget):
        """Create a right-click context menu for an Entry widget"""
        context_menu = tk.Menu(widget, tearoff=0)
        
        context_menu.add_command(
            label="Lõika",
            command=lambda: self.cut_text(widget),
            accelerator="Ctrl+X"
        )
        context_menu.add_command(
            label="Kopeeri",
            command=lambda: self.copy_text(widget),
            accelerator="Ctrl+C"
        )
        context_menu.add_command(
            label="Kleebi",
            command=lambda: self.paste_text(widget),
            accelerator="Ctrl+V"
        )
        context_menu.add_separator()
        context_menu.add_command(
            label="Vali kõik",
            command=lambda: self.select_all(widget),
            accelerator="Ctrl+A"
        )
        
        def show_context_menu(event):
            """Show context menu on right-click"""
            try:
                context_menu.tk_popup(event.x_root, event.y_root)
            finally:
                context_menu.grab_release()
        
        # Bind right-click to show menu
        widget.bind("<Button-3>", show_context_menu)
        
        # Also bind keyboard shortcuts
        widget.bind("<Control-x>", lambda e: self.cut_text(widget))
        widget.bind("<Control-c>", lambda e: self.copy_text(widget))
        widget.bind("<Control-v>", lambda e: self.paste_text(widget))
        widget.bind("<Control-a>", lambda e: self.select_all(widget))
        
        return context_menu
    
    def cut_text(self, widget):
        """Cut selected text from widget"""
        try:
            if widget.selection_present():
                widget.event_generate("<<Cut>>")
        except tk.TclError:
            pass
    
    def copy_text(self, widget):
        """Copy selected text from widget"""
        try:
            if widget.selection_present():
                widget.event_generate("<<Copy>>")
        except tk.TclError:
            pass
    
    def paste_text(self, widget):
        """Paste text into widget"""
        try:
            widget.event_generate("<<Paste>>")
        except tk.TclError:
            pass
    
    def select_all(self, widget):
        """Select all text in widget"""
        try:
            widget.select_range(0, tk.END)
            widget.icursor(tk.END)
        except tk.TclError:
            pass
        
    def setup_ui(self):
        """Setup the user interface"""
        
        # Title
        title_frame = tk.Frame(self.root, bg="#4a4a4a", height=70)
        title_frame.pack(fill=tk.X)
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame, 
            text="Meedia tööriist",
            font=("Segoe UI", 20, "bold"),
            bg="#4a4a4a",
            fg="#ffffff"
        )
        title_label.pack(pady=12)
        
        subtitle_label = tk.Label(
            title_frame,
            text="Tööriist heli ja video allalaadimiseks",
            font=("Segoe UI", 9),
            bg="#4a4a4a",
            fg="#d0d0d0"
        )
        subtitle_label.pack()
        
        # Main container
        main_frame = tk.Frame(self.root, padx=30, pady=20, bg="#f5f5f5")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # URL Input
        url_label = tk.Label(
            main_frame, 
            text="Sisesta URL:", 
            font=("Segoe UI", 10, "bold"),
            bg="#f5f5f5",
            fg="#2c2c2c"
        )
        url_label.pack(anchor=tk.W, pady=(0, 5))
        
        url_entry = tk.Entry(
            main_frame, 
            textvariable=self.url_var, 
            font=("Segoe UI", 10), 
            width=50,
            bg="#ffffff",
            fg="#2c2c2c",
            relief=tk.SOLID,
            borderwidth=1
        )
        url_entry.pack(fill=tk.X, pady=(0, 15))
        url_entry.focus()
        
        # Add context menu to URL entry
        self.create_context_menu(url_entry)
        
        # Download Type Selection
        type_label = tk.Label(
            main_frame, 
            text="Allalaadimise tüüp:", 
            font=("Segoe UI", 10, "bold"),
            bg="#f5f5f5",
            fg="#2c2c2c"
        )
        type_label.pack(anchor=tk.W, pady=(0, 5))
        
        type_frame = tk.Frame(main_frame, bg="#f5f5f5")
        type_frame.pack(anchor=tk.W, pady=(0, 10))
        
        audio_radio = tk.Radiobutton(
            type_frame,
            text="Ainult heli 🎵",
            variable=self.download_type,
            value="audio",
            font=("Segoe UI", 9),
            command=self.on_type_change,
            bg="#f5f5f5",
            fg="#2c2c2c",
            selectcolor="#e0e0e0",
            activebackground="#f5f5f5"
        )
        audio_radio.pack(side=tk.LEFT, padx=(0, 20))
        
        video_radio = tk.Radiobutton(
            type_frame,
            text="Video 🎬",
            variable=self.download_type,
            value="video",
            font=("Segoe UI", 9),
            command=self.on_type_change,
            bg="#f5f5f5",
            fg="#2c2c2c",
            selectcolor="#e0e0e0",
            activebackground="#f5f5f5"
        )
        video_radio.pack(side=tk.LEFT)
        
        # Playlist checkbox
        playlist_check = tk.Checkbutton(
            type_frame,
            text="📀 Terve playlist/album",
            variable=self.playlist_var,
            font=("Segoe UI", 9),
            bg="#f5f5f5",
            fg="#2c2c2c",
            selectcolor="#e0e0e0",
            activebackground="#f5f5f5"
        )
        playlist_check.pack(side=tk.LEFT, padx=(20, 0))
        
        # Format Selection (for audio)
        self.format_frame = tk.Frame(main_frame, bg="#f5f5f5")
        self.format_frame.pack(anchor=tk.W, pady=(0, 15))
        
        format_label = tk.Label(
            self.format_frame, 
            text="Audio formaat:", 
            font=("Segoe UI", 10, "bold"),
            bg="#f5f5f5",
            fg="#2c2c2c"
        )
        format_label.pack(anchor=tk.W, pady=(0, 5))
        
        format_combo = ttk.Combobox(
            self.format_frame,
            textvariable=self.format_var,
            values=["mp3", "m4a", "wav", "flac", "aac"],
            state="readonly",
            width=15,
            font=("Segoe UI", 9)
        )
        format_combo.pack(anchor=tk.W)
        
        # Output Directory
        output_label = tk.Label(
            main_frame, 
            text="Salvesta kausta:", 
            font=("Segoe UI", 10, "bold"),
            bg="#f5f5f5",
            fg="#2c2c2c"
        )
        output_label.pack(anchor=tk.W, pady=(0, 5))
        
        output_frame = tk.Frame(main_frame, bg="#f5f5f5")
        output_frame.pack(fill=tk.X, pady=(0, 20))
        
        output_entry = tk.Entry(
            output_frame, 
            textvariable=self.output_var, 
            font=("Segoe UI", 9), 
            state="normal",  # Changed from readonly to allow copy
            bg="#ffffff",
            fg="#2c2c2c",
            relief=tk.SOLID,
            borderwidth=1
        )
        output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        # Add context menu to output entry (even though it's readonly, copy is still useful)
        self.create_context_menu(output_entry)
        
        browse_btn = tk.Button(
            output_frame,
            text="Sirvi",
            command=self.browse_directory,
            font=("Segoe UI", 9),
            bg="#6c6c6c",
            fg="#ffffff",
            activebackground="#5a5a5a",
            activeforeground="#ffffff",
            relief=tk.FLAT,
            cursor="hand2",
            padx=15,
            pady=5
        )
        browse_btn.pack(side=tk.LEFT)
        
        # Download Button
        self.download_btn = tk.Button(
            main_frame,
            text="Lae alla",
            command=self.start_download,
            font=("Segoe UI", 11, "bold"),
            bg="#5a5a5a",
            fg="#ffffff",
            activebackground="#4a4a4a",
            activeforeground="#ffffff",
            relief=tk.FLAT,
            cursor="hand2",
            height=2
        )
        self.download_btn.pack(fill=tk.X, pady=(10, 15))
        
        # Progress Bar
        style = ttk.Style()
        style.theme_use('default')
        style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor='#e0e0e0',
            background='#6c6c6c',
            thickness=20
        )
        
        self.progress = ttk.Progressbar(
            main_frame, 
            mode='indeterminate',
            style="Custom.Horizontal.TProgressbar"
        )
        self.progress.pack(fill=tk.X, pady=(0, 10))
        
        # Status Label
        status_label = tk.Label(
            main_frame,
            textvariable=self.status_var,
            font=("Segoe UI", 9),
            fg="#6c6c6c",
            bg="#f5f5f5"
        )
        status_label.pack()
        
    def on_type_change(self):
        """Handle download type change"""
        if self.download_type.get() == "audio":
            # Always pack format frame when audio is selected
            self.format_frame.pack_forget()  # Remove first
            # Find the position before output_label
            pack_position = None
            for widget in self.format_frame.master.winfo_children():
                if isinstance(widget, tk.Label):
                    text = widget.cget("text")
                    if text == "Salvesta kausta:":
                        pack_position = widget
                        break
        
            if pack_position:
                self.format_frame.pack(anchor=tk.W, pady=(0, 15), before=pack_position)
            else:
                self.format_frame.pack(anchor=tk.W, pady=(0, 15))
        else:
            # Hide format frame for video
            self.format_frame.pack_forget()
    
    def browse_directory(self):
        """Open directory browser"""
        directory = filedialog.askdirectory(
            title="Vali allalaadimise asukoht",
            initialdir=self.output_var.get() if self.output_var.get() else None
        )
        if directory:
            self.output_var.set(directory)
    
    def validate_inputs(self):
        """Validate user inputs"""
        url = self.url_var.get().strip()
        output = self.output_var.get().strip()
        
        if not output: 
            messagebox.showerror("Viga", "Palun vali salvestamise kaust")
            return False
        
        if not url:
            messagebox.showerror("Viga", "Palun lisa korrektne veebilehe link")
            return False
        
        if not url.startswith(('http://', 'https://')):
            messagebox.showerror("Viga", "Palun sisesta korrektne URL (peab algama http:// või https://)")
            return False
        
        return True
    
    def start_download(self):
        """Start the download process"""
        if not self.validate_inputs():
            return
        
        # Disable button and start progress
        self.download_btn.config(state=tk.DISABLED, bg="#808080")
        self.progress.start(10)
        self.status_var.set("Allalaadimine käib... Palun oota")
        
        # Run download in separate thread
        thread = threading.Thread(target=self.download_worker, daemon=True)
        thread.start()
    
    def download_worker(self):
        """Worker thread for downloading"""
        try:
            url = self.url_var.get().strip()
            output_dir = self.output_var.get()
            download_type = self.download_type.get()
            allow_playlist = self.playlist_var.get()
            
            downloader = MediaDownloader(output_dir=output_dir)
            
            if download_type == "audio":
                format_type = self.format_var.get()
                success = downloader.download_audio(url, format=format_type, allow_playlist=allow_playlist)
            else:
                success = downloader.download_video(url, allow_playlist=allow_playlist)
            
            # Update UI on main thread
            self.root.after(0, self.download_complete, success)
            
        except Exception as e:
            self.root.after(0, self.download_error, str(e))
    
    def download_complete(self, success):
        """Handle download completion"""
        self.progress.stop()
        self.download_btn.config(state=tk.NORMAL, bg="#5a5a5a")
        
        if success:
            self.status_var.set("✅ Allalaadimine õnnestus!")
            messagebox.showinfo(
                "Õnnestus",
                f"Allalaadimine õnnestus!\n\nSalvestatud asukohta: {self.output_var.get()}"
            )
            self.url_var.set("")  # Clear URL
        else:
            self.status_var.set("❌ Allalaadimine ebaõnnestus")
            messagebox.showerror(
                "Viga",
                "Allalaadimine ebaõnnestus. Palun kontrolli URL-i ja proovi uuesti."
            )
    
    def download_error(self, error_msg):
        """Handle download error"""
        self.progress.stop()
        self.download_btn.config(state=tk.NORMAL, bg="#5a5a5a")
        self.status_var.set("❌ Viga")
        messagebox.showerror("Viga", f"Tekkis viga:\n\n{error_msg}")


def main():
    """Main entry point for GUI"""
    root = tk.Tk()
    app = MediaDownloaderGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
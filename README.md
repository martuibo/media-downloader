**Media allalaadimise tööriist** 🎵🎬

Lihtne, võimas Pythonil põhinev CLI-tööriist heli ja video allalaadimiseks SoundCloudist, YouTube’ist ja sadadelt teistelt platvormidelt.

**Funktsioonid**

🎵 Laadi URL-idest heli (SoundCloud, YouTube jne) MP3, M4A, WAV ja teistes formaatides

🎬 Laadi videod parima kvaliteediga koos automaatse formaatide liitmisega

📋 Vaata meedia infot ilma allalaadimata

🎯 Lihtne käsurea liides

🌐 Toetab 1000+ veebisaiti läbi yt-dlp

📁 Korrastatud väljund koos kohandatavate kaustadega

**Toetatud platvormid**
See tööriist toetab kõiki platvorme, mida yt-dlp toetab, sh:

SoundCloud
YouTube
Vimeo
Twitter/X
Instagram
TikTok
Facebook
Ja sajad teised

**Eeldused**

Python 3.7 või uuem
FFmpeg (helikonverteerimiseks)
FFmpeg paigaldamine
macOS:
brew install ffmpeg

Ubuntu/Debian:
  sudo apt update
  sudo apt install ffmpeg


Windows:
Laadi alla saidilt ffmpeg.org
 või kasuta:
              winget install FFmpeg

**Paigaldamine**

Klooni see repo:
git clone https://github.com/yourusername/media-downloader.git
cd media-downloader


Paigalda sõltuvused:
pip install -r requirements.txt

Kasutamine
Laadi heli (MP3)
python src/downloader.py -a "https://soundcloud.com/artist/track"

Laadi video
python src/downloader.py -v "https://youtube.com/watch?v=dQw4w9WgXcQ"

Määra väljundkaust
python src/downloader.py -a "https://..." -o ./my_music

Teine heliformaat
python src/downloader.py -a "https://..." -f m4a

Vaata meedia infot
python src/downloader.py -i "https://..."

Käsurea valikud
positsioonilised argumendid:
  url                   URL, kust alla laadida

valikud:
  -h, --help            Näita abi
  -a, --audio           Laadi ainult heli (vaikimisi: MP3)
  -v, --video           Laadi video
  -f, --format FORMAT   Heliformaat (mp3, m4a, wav jne) - vaikimisi: mp3
  -q, --quality QUALITY Video kvaliteet (best, worst) - vaikimisi: best
  -o, --output OUTPUT   Väljundkaust - vaikimisi: downloads
  -i, --info            Näita URL-i infot ilma allalaadimata

Näited
Laadi SoundCloudi lugu MP3-na
python src/downloader.py -a "https://soundcloud.com/artist/amazing-track"

Laadi YouTube’i video
python src/downloader.py -v "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

Laadi kindlasse kausta
python src/downloader.py -a "https://soundcloud.com/..." -o ~/Music/SoundCloud

Laadi heli WAV-formaadis (kõrge kvaliteet)
python src/downloader.py -a "https://..." -f wav

Kontrolli video infot enne allalaadimist
python src/downloader.py -i "https://youtube.com/watch?v=..."

Projekti struktuur
media-downloader/
├── src/
│   └── downloader.py      # Peamine CLI rakendus
├── tests/                 # Unit-testid (valikuline)
├── downloads/             # Vaikimisi allalaadimiste kaust (luuakse automaatselt)
├── requirements.txt       # Python sõltuvused
├── README.md              # See fail
└── .gitignore             # Git ignore reeglid

**Kuidas see töötab**

See tööriist kasutab yt-dlp, mis:
                                  Ekstraheerib meedia URL-id erinevatelt platvormidelt
                                  Laadib alla parima saadaoleva kvaliteediga
                                  Konverteerib heli sinu eelistatud formaati FFmpegi abil
                                  Salvestab failid puhaste ja korrastatud nimedega

**Tõrkeotsing**
“FFmpeg not found”

Paigalda FFmpeg vastavalt juhistele jaotises Eeldused.

“ERROR: Unsupported URL”

Kontrolli, kas platvorm on toetatud, vaadates yt-dlp toetatud saitide nimekirja
.

Allalaadimised on aeglased

See sõltub sinu internetiühendusest ja allikaplatvormist. yt-dlp optimeerib allalaadimiskiirust automaatselt.

Juriidiline märkus

See tööriist on mõeldud ainult isiklikuks kasutuseks. Palun austa autoriõigusi ja platvormide kasutustingimusi. Laadi alla ainult sisu, mille allalaadimiseks sul on õigus.

Panustamine

Panused on teretulnud! Esita julgelt Pull Request.

Litsents

MIT-litsents — kasuta vabalt oma projektides.

Tänusõnad

yt-dlp
 — suurepärane allalaadimismootor

FFmpeg
 — meediakonverteerimiseks

Tugi

Kui tekib probleeme, palun ava GitHubis issue.

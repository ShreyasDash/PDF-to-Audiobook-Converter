# Free PDF audiobook script

`pdf_audiobook.py` reads selectable text from a PDF and converts it to numbered WAV audio files using an installed system voice. Speech generation runs locally; no PDF text is uploaded to a service.

## Install

Use Python 3.9 or newer, then install the two Python packages:

```powershell
python -m pip install pypdf pyttsx3
```

The script relies on voices provided by your operating system. Windows uses its installed SAPI voices. If there are no usable system voices, add a voice in your operating system's speech settings.

## Use

```powershell
python pdf_audiobook.py "C:\path\to\book.pdf"
```

By default, audio goes into a sibling folder named `<pdf-name>_audiobook`. Each part is a WAV file; play them in numeric order.

```powershell
python pdf_audiobook.py "book.pdf" --output "book_audio" --rate 165
python pdf_audiobook.py "book.pdf" --voice "Zira"
python pdf_audiobook.py --list-voices
```

Use `--chunk-chars` to make shorter or longer audio parts (default: 12,000 characters). `--rate` is in words per minute. `--voice` matches part of an installed voice's name or ID.

## PDF requirements

The PDF needs selectable text. Image-only scans have no text for the script to extract; run OCR on a scan first, then convert the OCR-processed PDF. Page text is read in order. Complex page layouts, columns, headers, and footnotes may not extract in ideal reading order.

This creates local WAV files rather than a single MP3. If you want a single file, combine the parts afterward with an audio editor or a free tool such as FFmpeg.

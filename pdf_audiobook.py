"""Convert the text in a PDF into one WAV file per page.

Install dependencies with: python -m pip install pypdf pyttsx3
"""

import argparse
from pathlib import Path

import pyttsx3
from pypdf import PdfReader


def main():
    parser = argparse.ArgumentParser(description="Make a simple audiobook from a text-based PDF.")
    parser.add_argument("pdf", type=Path, help="PDF file to read")
    parser.add_argument("-o", "--output", type=Path, help="Folder for audio files")
    args = parser.parse_args()

    if not args.pdf.is_file():
        parser.error(f"File not found: {args.pdf}")

    output = args.output or args.pdf.with_name(args.pdf.stem + "_audio")
    output.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(args.pdf)
    engine = pyttsx3.init()

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if not text.strip():
            print(f"Skipping page {page_number}: no text found")
            continue

        audio_file = output / f"page_{page_number:04}.wav"
        print(f"Reading page {page_number} of {len(reader.pages)}")
        engine.save_to_file(text, str(audio_file))
        engine.runAndWait()

    engine.stop()
    print(f"Audio saved in {output.resolve()}")


if __name__ == "__main__":
    main()

"""Download PHREEQC databases from the official USGS distribution archive.

Downloads phreeqc-3.8.6-17100.zip (Windows) or phreeqc-3.8.6-17100.tar.gz
(Linux/macOS) and extracts the database directory to src/phreeqc/databases.
"""

from __future__ import annotations

import io
import sys
import tarfile
import urllib.request
import zipfile
from pathlib import Path

VERSION = "3.8.6-17100"
BASE_URL = "https://water.usgs.gov/water-resources/software/PHREEQC"
ARCHIVE_PREFIX = f"phreeqc-{VERSION}/database/"

PROJECT_ROOT = Path(__file__).parent.parent
DEST_DIR = PROJECT_ROOT / "src" / "phreeqc" / "databases"


def download(url: str) -> bytes:
    print(f"Downloading {url} ...", flush=True)
    with urllib.request.urlopen(url) as response:  # noqa: S310
        total = int(response.headers.get("Content-Length", 0))
        data = bytearray()
        chunk = 1 << 16  # 64 KiB
        while True:
            block = response.read(chunk)
            if not block:
                break
            data += block
            if total:
                pct = len(data) * 100 // total
                print(f"\r  {len(data):,} / {total:,} bytes ({pct}%)", end="", flush=True)
        print()
    return bytes(data)


def extract_zip(data: bytes, dest: Path) -> None:
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        for member in zf.infolist():
            if not member.filename.startswith(ARCHIVE_PREFIX):
                continue
            filename = member.filename[len(ARCHIVE_PREFIX):]
            if not filename or member.is_dir() or not filename.endswith(".dat"):
                continue
            out = dest / filename
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(zf.read(member))
            print(f"  extracted {filename}")


def extract_tar(data: bytes, dest: Path) -> None:
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tf:
        for member in tf.getmembers():
            if not member.name.startswith(ARCHIVE_PREFIX):
                continue
            filename = member.name[len(ARCHIVE_PREFIX):]
            if not filename or member.isdir() or not filename.endswith(".dat"):
                continue
            out = dest / filename
            out.parent.mkdir(parents=True, exist_ok=True)
            f = tf.extractfile(member)
            if f is not None:
                out.write_bytes(f.read())
            print(f"  extracted {filename}")


def main() -> None:
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    if sys.platform == "win32":
        url = f"{BASE_URL}/phreeqc-{VERSION}.zip"
        data = download(url)
        print("Extracting databases from zip archive ...")
        extract_zip(data, DEST_DIR)
    else:
        url = f"{BASE_URL}/phreeqc-{VERSION}.tar.gz"
        data = download(url)
        print("Extracting databases from tar.gz archive ...")
        extract_tar(data, DEST_DIR)

    files = sorted(DEST_DIR.glob("*.dat"))
    print(f"\nDone. {len(files)} database files written to {DEST_DIR}")


if __name__ == "__main__":
    main()

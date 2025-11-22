import hashlib
import os
from datetime import datetime
from .models import FileInfo


def calculate_file_hash(file_path: str) -> str:
    """محاسبه‌ی هش (MD5) برای تشخیص تغییر واقعی محتوا"""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def scan_directory(base_path: str) -> list[FileInfo]:
    """
    اسکن کامل فولدر و خروجی دادن لیستی از FileInfo
    مسیرها به صورت نسبی نسبت به base_path ذخیره می‌شوند.
    """
    file_infos = []

    for root, _, files in os.walk(base_path):
        for filename in files:
            full_path = os.path.join(root, filename)

            #  مسیر نسبی برای مقایسه
            rel_path = os.path.relpath(full_path, base_path)

            # اطلاعات فایل
            stats = os.stat(full_path)
            size = stats.st_size
            modified_at = datetime.fromtimestamp(stats.st_mtime)

            # محاسبه هش
            file_hash = calculate_file_hash(full_path)

            # ساخت مدل
            file_infos.append(
                FileInfo(
                    path=rel_path.replace("\\", "/"),
                    size=size,
                    modified_at=modified_at,
                    hash=file_hash,
                )
            )

    return file_infos
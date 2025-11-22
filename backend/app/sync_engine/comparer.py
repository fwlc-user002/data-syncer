from .models import FileInfo, DiffResult


def compare_directories(
    source_files: list[FileInfo], target_files: list[FileInfo]
) -> DiffResult:
    """
    مقایسه فایل‌های source با target و تشخیص تغییرات
    """

    # تبدیل لیست‌ها به دیکشنری برای دسترسی O(1)
    source_map = {f.path: f for f in source_files}
    target_map = {f.path: f for f in target_files}

    new_files = []
    modified_files = []
    deleted_files = []
    unchanged_files = []

    # بررسی فایل‌های موجود در source
    for path, src_file in source_map.items():
        if path not in target_map:
            new_files.append(src_file)
        else:
            tgt_file = target_map[path]
            if src_file.hash != tgt_file.hash:
                modified_files.append(src_file)
            else:
                unchanged_files.append(src_file)

    # بررسی فایل‌های حذف‌شده
    for path in target_map:
        if path not in source_map:
            deleted_files.append(path)

    return DiffResult(
        new_files=new_files,
        modified_files=modified_files,
        deleted_files=deleted_files,
        unchanged_files=unchanged_files,
    )

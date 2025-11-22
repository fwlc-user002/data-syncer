from pydantic import BaseModel
from datetime import datetime


class FileInfo(BaseModel):
    """
    اطلاعات یک فایل در سیستم (source یا target)
    """

    path: str
    size: int
    modified_at: datetime
    hash: str

class DiffResult(BaseModel):
    """
    نتیجه مقایسه دو فولدر (source و target)
    """
    new_files: list[FileInfo]
    modified_files: list[FileInfo]
    deleted_files: list[str]
    unchanged_files: list[FileInfo]
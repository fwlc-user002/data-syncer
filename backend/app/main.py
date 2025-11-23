# from fastapi import FastAPI
# from pydantic import BaseModel
# from datetime import datetime

# # from fastapi.middleware.cors import CORSMiddleware
# import os

# from .sync_engine.scanner import scan_directory
# from .sync_engine.comparer import compare_directories
# from .sync_engine.models import DiffResult

# app = FastAPI(
#     title="Data Syncer API",
#     description="Backend API for the Python + Next data synchronization tool",
#     version="0.1.0",
# )

# app = FastAPI(
#     title="Data Syncer API",
#     description="Backend API for the Python + Next data synchronization tool",
#     version="0.1.0",
# )

# # ---- اضافه کردن CORS ----
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # در آینده محدود می‌کنیم
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # مسیرهای پایه‌ی تستی (بعداً config.json می‌شود)
# SOURCE_DIR = "/home/user002/projects/data-syncer/test_source"
# TARGET_DIR = "/home/user002/projects/data-syncer/test_target"


# @app.get("/health")
# def health_check():
#     return {"ok": True, "message": "Data Syncer API is running"}


# @app.get("/status", response_model=DiffResult)
# def get_status():

#     # اگر مسیر وجود نداشته باشد، هیچ چیز برنمی‌گردانیم
#     if not os.path.exists(SOURCE_DIR) or not os.path.exists(TARGET_DIR):
#         return DiffResult(
#             new_files=[], modified_files=[], deleted_files=[], unchanged_files=[]
#         )

#     #  اسکن فولدرها
#     source_files = scan_directory(SOURCE_DIR)
#     target_files = scan_directory(TARGET_DIR)

#     # مقایسه و تولید diff
#     diff = compare_directories(source_files, target_files)

#     return diff

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os

from .sync_engine.scanner import scan_directory
from .sync_engine.comparer import compare_directories
from .sync_engine.models import DiffResult

# ------------------------------
#   ساخت اپلیکیشن FastAPI
# ------------------------------
app = FastAPI(
    title="Data Syncer API",
    description="Backend API for the Python + Next data synchronization tool",
    version="0.1.0",
)

# ------------------------------
#   فعال‌سازی CORS
# ------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # در آینده فقط localhost:3000 می‌ذاریم
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------
#   مسیرهای تست (بعداً config.json می‌شود)
# ------------------------------
SOURCE_DIR = "/home/user002/projects/data-syncer/test_source"
TARGET_DIR = "/home/user002/projects/data-syncer/test_target"


# ------------------------------
#   Health Check
# ------------------------------
@app.get("/health")
def health_check():
    return {"ok": True, "message": "Data Syncer API is running"}


# ------------------------------
#   Status API (Diff Result)
# ------------------------------
@app.get("/status", response_model=DiffResult)
def get_status():

    # اگر مسیر وجود نداشته باشد
    if not os.path.exists(SOURCE_DIR) or not os.path.exists(TARGET_DIR):
        return DiffResult(
            new_files=[], modified_files=[], deleted_files=[], unchanged_files=[]
        )

    # اسکن فولدرها
    source_files = scan_directory(SOURCE_DIR)
    target_files = scan_directory(TARGET_DIR)

    # مقایسه فولدرها
    diff = compare_directories(source_files, target_files)

    return diff

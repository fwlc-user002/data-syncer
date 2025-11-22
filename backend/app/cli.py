# import argparse
# from .sync_engine.scanner import scan_directory
# from .sync_engine.comparer import compare_directories


# def main():
#     parser = argparse.ArgumentParser(description="Data Syncer CLI")

#     parser.add_argument(
#         "--source", "-s", type=str, required=True, help="Target directory path"
#     )

#     args = parser.parse_args()

#     print(f"🔍 Scanning source: {args.source}")
#     print(f"📂 Scanning target: {args.target}")

#     source_files = scan_directory(args.source)
#     target_files = scan_directory(args.target)

#     diff = compare_directories(source_files, target_files)

#     print("\n===== SYNC REPORT =====")
#     print(f"🆕  New files: {len(diff.new_files)}")
#     print(f"✏️  Modified files: {len(diff.modified_files)}")
#     print(f"🗑️  Deleted files: {len(diff.deleted_files)}")
#     print(f"✔️  Unchanged files: {len(diff.unchanged_files)}")

#     print("\n---- DETAILS ----")

#     if diff.new_files:
#         print("\n🆕 New:")
#         for f in diff.new_files:
#             print(f"  + {f.path}")

#     if diff.modified_files:
#         print("\n✏️ Modified:")
#         for f in diff.modified_files:
#             print(f" ~ {f.path}")

#     if diff.deleted_files:
#         print("\n🗑️ Deleted:")
#         for f in diff.deleted_files:
#             print(f"  - {f}")

#     print("\nDone. ✔")


# if __name__ == "__main__":
#     main()

import argparse
from .sync_engine.scanner import scan_directory
from .sync_engine.comparer import compare_directories


def main():
    parser = argparse.ArgumentParser(description="Data Syncer CLI")

    parser.add_argument(
        "--source",
        "-s",
        type=str,
        required=True,
        help="Source directory path",
    )

    parser.add_argument(
        "--target",
        "-t",
        type=str,
        required=True,
        help="Target directory path",
    )

    args = parser.parse_args()

    print(f"🔍 Scanning source: {args.source}")
    print(f"📂 Scanning target: {args.target}")

    source_files = scan_directory(args.source)
    target_files = scan_directory(args.target)

    diff = compare_directories(source_files, target_files)

    print("\n===== SYNC REPORT =====")
    print(f"🆕  New files: {len(diff.new_files)}")
    print(f"✏️  Modified files: {len(diff.modified_files)}")
    print(f"🗑️  Deleted files: {len(diff.deleted_files)}")
    print(f"✔️  Unchanged files: {len(diff.unchanged_files)}")

    print("\n---- DETAILS ----")

    if diff.new_files:
        print("\n🆕 New:")
        for f in diff.new_files:
            print(f"  + {f.path}")

    if diff.modified_files:
        print("\n✏️ Modified:")
        for f in diff.modified_files:
            print(f"  ~ {f.path}")

    if diff.deleted_files:
        print("\n🗑️ Deleted:")
        for f in diff.deleted_files:
            print(f"  - {f}")

    print("\nDone. ✔")


if __name__ == "__main__":
    main()

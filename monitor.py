
import os
import shutil
import psutil
from pathlib import Path
from datetime import datetime


# 1. Automatically select the folder to scan
SCAN_FOLDER = Path.home()


# 2. Check disk space
def check_disk_space(folder_path):
    disk = shutil.disk_usage(folder_path)

    total = disk.total / (1024 ** 3)
    used = disk.used / (1024 ** 3)
    free = disk.free / (1024 ** 3)

    result = (
        "\n--- DISK SPACE ---\n"
        f"Total Disk Space: {total:.2f} GB\n"
        f"Used Disk Space: {used:.2f} GB\n"
        f"Free Disk Space: {free:.2f} GB"
    )

    return result


# 3. Calculate folder size
def get_folder_size(folder_path):
    total_size = 0

    for root, dirs, files in os.walk(
        folder_path,
        onerror=lambda error: None
    ):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                total_size += os.path.getsize(file_path)
            except OSError:
                continue

    size_mb = total_size / (1024 ** 2)

    result = (
        "\n--- FOLDER SIZE ---\n"
        f"Scanned Folder: {folder_path}\n"
        f"Total Folder Size: {size_mb:.2f} MB"
    )

    return result


# 4. Find five largest files
def find_largest_files(folder_path):
    largest_files = []

    for root, dirs, files in os.walk(
        folder_path,
        onerror=lambda error: None
    ):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                file_size = os.path.getsize(file_path)

                largest_files.append(
                    (file_path, file_size)
                )

            except OSError:
                continue

    largest_files.sort(
        key=lambda item: item[1],
        reverse=True
    )

    result = "\n--- FIVE LARGEST FILES ---"

    if not largest_files:
        result += "\nNo files found."

    for file_path, file_size in largest_files[:5]:
        size_mb = file_size / (1024 ** 2)

        result += (
            f"\nFile: {file_path}"
            f"\nSize: {size_mb:.2f} MB\n"
        )

    return result


# 5. Check CPU usage
def check_cpu_usage():
    cpu = psutil.cpu_percent(interval=1)

    result = (
        "\n--- CPU USAGE ---\n"
        f"CPU Usage: {cpu}%"
    )

    return result


# 6. Check RAM usage
def check_ram_usage():
    memory = psutil.virtual_memory()

    total_ram = memory.total / (1024 ** 3)
    used_ram = memory.used / (1024 ** 3)
    available_ram = memory.available / (1024 ** 3)

    result = (
        "\n--- RAM USAGE ---\n"
        f"Total RAM: {total_ram:.2f} GB\n"
        f"Used RAM: {used_ram:.2f} GB\n"
        f"Available RAM: {available_ram:.2f} GB\n"
        f"RAM Usage: {memory.percent}%"
    )

    return result


# 7. Get current date and time
def get_date_time():
    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return (
        "\n--- DATE AND TIME ---\n"
        f"Report Generated: {current_time}"
    )


# 8. Save report
def save_report(report):

    file_name = "health_log.txt"

    save_locations = [
        Path(__file__).resolve().parent,
        Path.home() / "Documents",
        Path.home()
    ]

    for location in save_locations:

        try:
            location.mkdir(parents=True, exist_ok=True)

            file_path = location / file_name

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write("\n".join(report))

            print("\nReport saved successfully!")
            print(f"Saved location: {file_path}")

            return

        except OSError:
            continue

    print("\nError: Could not save the health report.")
    print("Please check your folder permissions.")


# 9. Main program
def main():

    print("=" * 40)
    print("       SYSTEM HEALTH MONITOR")
    print("=" * 40)

    folder_path = SCAN_FOLDER

    print(f"\nAutomatically scanning: {folder_path}")
    print("\nPlease wait while the system is checked...")

    report = []

    report.append("SYSTEM HEALTH MONITOR REPORT")
    report.append("=" * 40)

    report.append(check_disk_space(folder_path))

    report.append(get_folder_size(folder_path))

    report.append(find_largest_files(folder_path))

    report.append(check_cpu_usage())

    report.append(check_ram_usage())

    report.append(get_date_time())

    # Display results
    print("\n".join(report))

    # Save results
    save_report(report)

    print("\n" + "=" * 40)
    print("       MONITOR COMPLETED")
    print("=" * 40)


# 10. Run program
if __name__ == "__main__":
    main()
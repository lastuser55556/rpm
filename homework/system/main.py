import argparse
import os
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument("--timeout", type=float, default=5)
    args = parser.parse_args()
    if not args.timeout > 0 or args.timeout == float("inf"):
        parser.error("Таймаут должен быть конечным положительным числом")
    if not args.file.is_file():
        print("Файл не найден", file=sys.stderr)
        return 2
    worker = "import sys; from pathlib import Path; print(Path(sys.argv[1]).stat().st_size)"
    try:
        result = subprocess.run(
            [sys.executable, "-c", worker, os.fspath(args.file.resolve())],
            timeout=args.timeout,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.TimeoutExpired:
        print("Дочерний процесс не успел завершиться", file=sys.stderr)
        return 3
    except (OSError, subprocess.CalledProcessError):
        print("Не удалось получить размер файла", file=sys.stderr)
        return 4
    print(f"Размер: {int(result.stdout)} байт")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

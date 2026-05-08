"""
LeetCode Hot 100 统一运行入口
"""

import subprocess
import sys
from pathlib import Path


def main():
    root = Path(__file__).parent
    problems = sorted(root.glob("h*_*.py"))

    if not problems:
        print("未找到题目文件")
        return

    passed = 0
    failed = []

    for f in problems:
        print(f"--- {f.stem} ---")
        result = subprocess.run([sys.executable, str(f)], capture_output=True, text=True)
        print(result.stdout.rstrip())
        if result.returncode == 0:
            passed += 1
        else:
            failed.append(f.stem)
            if result.stderr:
                print(result.stderr.rstrip())
        print()

    print(f"通过: {passed}/{len(problems)}")
    if failed:
        print(f"失败: {', '.join(failed)}")


if __name__ == "__main__":
    main()

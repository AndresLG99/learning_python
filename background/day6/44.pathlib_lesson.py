from pathlib import Path, PureWindowsPath

directory = Path("D:/Documents Local/Portfolio/learning_python/background/day6/class_material/directory_test/test_file.txt")
print(directory.read_text())
print(directory.name)
print(directory.suffix)
print(directory.stem)

if not directory.exists():
    print("Doesn't exist")
else:
    print("Exists")

windows_path = PureWindowsPath(directory)
print(windows_path)
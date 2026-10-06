#! /usr/bin/env python3
from importlib.metadata import version, PackageNotFoundError
from importlib import import_module
import sys
#import requests

packages: dict[str, str] = {
    "numpy": "Numerical computation ready",
    "pandas": "Data manipulation ready",
    "matplotlib": "Visualization ready",
}

def check_dependency(package_name: str) -> tuple[bool, str]:
    try:
        ver: str = version(package_name)
        return (True, ver)
    except PackageNotFoundError:
        return (False, "Not installed")

def verify_environment() -> bool:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    all_ok: bool = True
    for package, purpose in packages.items():
        installed, ver = check_dependency(package)
        if installed:
            print(f"[OK] {package} ({ver}) - {purpose}")
        else:
            print(f"[MISSING] {package} - {purpose}")
            all_ok = False

    if not all_ok:
        print("\nERROR: Missing required dependencies!")
        print("\nTo install via pip, run:")
        print("  pip install -r requirements.txt")
        print("\nTo install via Poetry, run:")
        print("  poetry install")
        return False

    return True

def analysis() -> None:
    np = import_module("numpy")
    pd = import_module("pandas")
    plt = import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    x = np.linspace(0, 10, 1000)
    y = np.sin(x) + np.random.normal(-0.15, 0.15, 1000)

    df = pd.DataFrame({"signal": y, "time": x})

    print("Generating visualization...")
    plt.figure(figsize=(8, 4))
    plt.plot(df["time"], 
             df["signal"], 
             label="Matrix Signal", 
             color="#00FF00",
             linewidth=1)
    plt.title("Matrix Data Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal Amplitude")
    plt.grid(True)
    plt.savefig("matrix_analysis.png")
    plt.show()
    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")

def main() -> None:
    if not verify_environment():
        sys.exit(1)
    analysis()


if __name__ == "__main__":
    main()

import subprocess
import sys

print("Starting YouTube Sentiment Analysis Pipeline...\n")

scripts = [
    "src/get_comments.py",
    "src/data_cleaning.py",
    "src/sentiment_analysis.py",
    "src/visualization.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"\nPipeline stopped because of an error in {script}")
        sys.exit(1)

print("\nPipeline completed successfully! 🎉")
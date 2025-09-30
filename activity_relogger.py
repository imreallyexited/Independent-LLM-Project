import os
import random
import subprocess
from datetime import datetime, timedelta

START_DATE = datetime(2025, 9, 30)  
END_DATE = datetime(2026, 2, 11)   
MIN_COMMITS_PER_DAY = 0            
MAX_COMMITS_PER_DAY = 4            
WORK_PROBABILITY = 0.7             

FILES = [
    "models/transformer.py",
    "models/cnn_layer.py",
    "data/loader.py",
    "data/preprocessing.py",
    "training/train_loop.py",
    "training/optimizer.py",
    "utils/metrics.py",
    "utils/visualization.py",
    "config.py",
    "main.py"
]

COMMIT_MESSAGES = [
    "Fix gradient vanishing problem",
    "Update learning rate scheduler",
    "Refactor data augmentation pipeline",
    "Optimize tensor calculations",
    "Add dropout layer to prevent overfitting",
    "Fix dimension mismatch in forward pass",
    "Update loss function logic",
    "Clean up unused variables",
    "Improve validation metrics logging",
    "Adjust batch size for memory optimization",
    "Fix bug in backpropagation",
    "Implement early stopping",
    "Update dependencies",
    "Refactor model architecture"
]

CODE_SNIPPETS = [
    "\n# Optimized calculation for matrix multiplication",
    "\n# TODO: Refactor this loop for better performance",
    "\n# Changed activation function to ReLU",
    "\ndef temp_calculation(x):\n    return x * 0.01 + 0.9  # Normalization step",
    "\n# Logging output shape for debugging",
    "\n# Added support for CUDA acceleration",
    "\n# Fixed index out of bounds error handled",
]

def create_structure():
    """Dosya ve klasörleri oluşturur."""
    print("Creating project structure...")
    for file_path in FILES:
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(f"# AI Project Module: {os.path.basename(file_path)}\n")
                f.write("import numpy as np\nimport torch\n\n")

def git_commit(date, message):
    """Belirtilen tarihte commit atar."""
    date_str = date.strftime('%Y-%m-%d %H:%M:%S')
    env = os.environ.copy()
    env['GIT_COMMITTER_DATE'] = date_str
    env['GIT_AUTHOR_DATE'] = date_str
    
    
    subprocess.run(['git', 'add', '.'], check=True, env=env)
    
    
    subprocess.run(['git', 'commit', '-m', message, '--date', date_str], env=env, stdout=subprocess.DEVNULL)
    print(f"Committed: {date_str} -> {message}")

def modify_random_file():
    """Rastgele bir python dosyasına rastgele kod ekler."""
    file_to_edit = random.choice(FILES)
    snippet = random.choice(CODE_SNIPPETS)
    
    with open(file_to_edit, "a") as f:
        f.write(snippet + "\n")

def main():
    create_structure()
    
    current_date = START_DATE
    total_commits = 0
    
    while current_date <= END_DATE:
        
        is_weekend = current_date.weekday() >= 5
        daily_prob = WORK_PROBABILITY * 0.5 if is_weekend else WORK_PROBABILITY
        
        if random.random() < daily_prob:
            num_commits = random.randint(MIN_COMMITS_PER_DAY, MAX_COMMITS_PER_DAY)
            
            for _ in range(num_commits):
                hour = random.randint(9, 23)
                minute = random.randint(0, 59)
                commit_date = current_date.replace(hour=hour, minute=minute)
                
                modify_random_file()
                msg = random.choice(COMMIT_MESSAGES)
                git_commit(commit_date, msg)
                total_commits += 1
        
        current_date += timedelta(days=1)
    
    print(f"\nSUCCESS! Total {total_commits} fake commits created.")
    print("Now creating a cleaner 'final' state...")
    
    if os.path.exists("activity_booster.py"):
        os.remove("activity_booster.py")
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', 'Final cleanup and release', '--date', END_DATE.strftime('%Y-%m-%d %H:%M:%S')])

if __name__ == "__main__":
    main()
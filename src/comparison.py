import os
import json

def scan_experiments(experiment_dir="experiments"):
    
    
    all_items = os.listdir(experiment_dir)
    
    run_folders = [item for item in all_items if item.startswith("run")]
    
    
    return run_folders


def load_experiment_data(run_dir):
    metrics_path = os.path.join(run_dir,"metrics.json")
    
    with open(metrics_path,"r") as f:
        data = json.load(f)
        
    return data


def compare_experiments(experiment_dir="experiments"):
    folder_names = scan_experiments(experiment_dir)
    
    
    all_data = []
    
    for folder_name in folder_names:
        
        full_path = os.path.join(experiment_dir,folder_name)
        
        
        try:
            data = load_experiment_data(full_path)
            
            all_data.append(data)
        except FileNotFoundError:
            print(f"Skipping {folder_name}: metrics.json not found.")
            
    return all_data


def get_best_run(experiment_list, metric="accuracy"):
    
    # 1. Initialize based on what we are looking for
    if metric == "loss":
        best_score = float('inf')
    else:
        best_score = float('-inf')
        
    best_run = None
    
    for experiment in experiment_list:
        # Get the final value recorded in the list
        current_score = experiment[metric][-1]
        
        # Define winning conditions
        is_accuracy_better = (metric == "accuracy" and current_score > best_score)
        is_loss_better     = (metric == "loss" and current_score < best_score)
        
        # Update if we found a winner
        if is_accuracy_better or is_loss_better:
            best_score = current_score
            best_run = experiment
            
    return best_run


if __name__ == "__main__":
    # 1. Scan and Load
    print("Scanning experiments...")
    all_runs = compare_experiments("./experiments")
    print(f"Found {len(all_runs)} runs.")
    
    # 2. Find the Winner
    winner = get_best_run(all_runs, metric="accuracy")
    
    # 3. Print Results
    if winner:
        print("\n Winning Run:")
        print(f"Final Accuracy: {winner['accuracy'][-1]}")
        print(f"Final Loss: {winner['loss'][-1]}")
      
    else:
        print("No valid runs found.")
        
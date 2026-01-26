from src.comparison import load_experiment_data,scan_experiments,compare_experiments
import os
import json



all_data = compare_experiments("./experiments")
summary_list = []
for data in all_data:
    
    metrics_path = os.path.join("experiments",data["run_id"],"config.json")
    
    with open(metrics_path,"r") as f:
        config = json.load(f)
        
    data["learning_rate"] = config["lr"]

    summary = {
        "Run ID": data["run_id"],
        "LR":data["learning_rate"],
        "Epochs":len(data["loss"]),
        "Final Loss":data["loss"][-1],
        "Best Loss":min(data["loss"])
    }
    
    summary_list.append(summary)
    
    

summary_path = os.path.join("experiments", "summary.md")

with open(summary_path, "w") as f:
    # 1. Title
    f.write("# Experiment Summary\n\n")
    
    # 2. Table Header
    f.write("| Run ID | Learning Rate | Epochs | Final Loss | Best Loss |\n")
    
    # 3. The Separator Line (Critical for Markdown tables)
    f.write("|---|---|---|---|---|\n")
    
    # 4. Data Rows
    for summary in summary_list:
        f.write(f"| {summary['Run ID']} | {summary['LR']} | {summary['Epochs']} | {summary['Final Loss']} | {summary['Best Loss']} |\n")

print(f"Summary report generated at: {summary_path}")
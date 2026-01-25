from datetime import datetime
import os 
import json
import matplotlib.pyplot as plt

class Experiment:
    def __init__(self,config,experiment_dir="experiments",tags=None):
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        
        self.history = {}
        
        self.run_name = f"run{self.timestamp}"
        
        self.run_dir = os.path.join(experiment_dir,self.run_name)
        
        
        #define subdirectories
        self.plots_dir = os.path.join(self.run_dir,"plots")
        self.checkpoints_dir = os.path.join(self.run_dir, "checkpoints")
        
        
        #3. Create all directories
        os.makedirs(self.run_dir,exist_ok=True)
        os.makedirs(self.plots_dir,exist_ok=True)
        os.makedirs(self.checkpoints_dir, exist_ok=True)
        
        #4. Store and save Metadata
        self.config = config
        self.tags = tags if tags else []
        self._save__initial_metadata()
        
        
        os.makedirs(self.run_dir,exist_ok=True)
        
        print(f"Initiated experiment: {self.run_name}")
        print(f"   📂 Location: {self.run_dir}")
        
    def _save__initial_metadata(self):
        
        config_path = os.path.join(self.run_dir, "config.json")
        with open(config_path, "w") as f:
            json.dump(self.config,f,indent=4)
        
        
        #save metadata (timestamps,tags)
        metadata = {
            "run_name": self.run_name,
            "start_time":self.timestamp,
            "tags": self.tags
        }
        
        metadata_path = os.path.join(self.run_dir, "metadata.json")
        with open(metadata_path,"w") as f:
            json.dump(metadata, f,indent=4)
            
            
    def log_metric(self, name, value):
        
        if name not in self.history:
            self.history[name] = [value]
        else:
            self.history[name].append(value)
            
    def save_metrics(self):
        
        metrics_path = os.path.join(self.run_dir, "metrics.json")
        
        
        with open(metrics_path,"w") as f:
            json.dump(self.history,f,indent=4)
            
            
    def save_plot(self, figure, filename):
        #saves a matplotlib figure to the plots directly
        
        plot_path = os.path.join(self.plots_dir,filename)
        
        figure.savefig(plot_path)
        
            
            
    
if __name__ == "__main__":
    # Quick test to see if it creates the folder
    exp = Experiment(config={"lr": 0.01}, tags=["day2_test"]) 
    
    
    print("Simulating training...")
    exp.log_metric("loss", 0.5)
    exp.log_metric("loss", 0.4)
    exp.log_metric("accuracy", 0.8)
    
    # exp.log_metric("loss", 0.5)
    exp.log_metric("loss", 0.2)
    exp.log_metric("accuracy", 0.9)
    
    exp.save_metrics()
    print("Metrics saved.")
    
    fig, ax = plt.subplots()
    ax.plot([0.5, 0.4, 0.3], label="Loss")
    ax.legend()
    
    exp.save_plot(fig, "loss_curve.png")
    print("Plot saved.")
    
          
    
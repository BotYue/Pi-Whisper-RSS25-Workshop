import os
import pandas as pd

# Root directory where extracted data lives
data_dir = "../"

# Results
common_results = []
ap_results = []

# Walk and process
for root, dirs, files in os.walk(data_dir):
    for file in files:
        if "latency" in file.lower() and file.endswith(".txt"):
            file_path = os.path.join(root, file)
            try:
                df = pd.read_csv(file_path, header=None, names=["filename", "latency"])
                avg_latency = df["latency"].mean()

                # Normalize and split the path
                path_parts = os.path.normpath(file_path).split(os.path.sep)
                board = path_parts[-3]  # e.g., Rasp5 8GB
                category = path_parts[-2]  # e.g., AP or Common
                model = file.replace("latency_", "").replace(".txt", "")

                result_entry = {
                    "File": file,
                    "Board": board,
                    "Model": model,
                    "Average Latency": avg_latency
                }

                if "common" in category.lower():
                    common_results.append(result_entry)
                elif "ap" in category.lower():
                    ap_results.append(result_entry)

            except Exception as e:
                print(f"Failed to process {file_path}: {e}")

# Save to CSV
df_common = pd.DataFrame(common_results)
df_ap = pd.DataFrame(ap_results)
df_common.to_csv("latency_averages_Common.csv", index=False)
df_ap.to_csv("latency_averages_AP.csv", index=False)


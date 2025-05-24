import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the updated CSV file
df = pd.read_csv("latency_averages_AP.csv")

# Manual model order and display labels
model_order = [
    "openai_tiny_en",
    "tiny_en_fp32",
    "tiny_en",
    "openai_base_en",
    "base_en_fp32",
    "base_en",
    "distil-small_en_fp32",
    "distil-small_en"
]

model_labels = {
    "openai_tiny_en": "OpenAI Whisper\ntiny.en (fp32)",
    "openai_base_en": "OpenAI Whisper\nbase.en (fp32)",
    "tiny_en_fp32": "Faster-Whisper\ntiny.en (fp32)",
    "base_en_fp32": "Faster-Whisper\nbase.en (fp32)",
    "distil-small_en_fp32": "Faster-Whisper\ndistill-small.en (fp32)",
    "tiny_en": "Faster-Whisper\ntiny.en (int8)",
    "base_en": "Faster-Whisper\nbase.en (int8)",
    "distil-small_en": "Faster-Whisper\ndistill-small.en (int8)"
}

board_order = ["Rasp4 4GB", "Rasp5 4GB", "Rasp5 8GB", "Rasp5 16GB"]
board_labels = {
    "Rasp4 4GB": "Pi 4 (4GB)",
    "Rasp5 4GB": "Pi 5 (4GB)",
    "Rasp5 8GB": "Pi 5 (8GB)",
    "Rasp5 16GB": "Pi 5 (16GB)"
}

# Map and categorize board and model columns
df["Raspberry Pi Model"] = df["Board"].map(board_labels)
df = df[df["Model"].isin(model_order)]
df["Model"] = pd.Categorical(df["Model"], categories=model_order, ordered=True)
df["Raspberry Pi Model"] = pd.Categorical(
    df["Raspberry Pi Model"],
    categories=[board_labels[b] for b in board_order],
    ordered=True
)
df["Model Label"] = df["Model"].map(model_labels)

# Plot
sns.set(style="whitegrid")
plt.figure(figsize=(14, 6))
sns.barplot(
    data=df,
    x="Model Label",
    y="Average Latency",
    hue="Raspberry Pi Model",
    errorbar=None,
    palette="tab10"
)
plt.xlabel("", fontsize=14)
plt.title("Average Latency — AP News Test Set")
plt.xticks(rotation=45, fontsize=13)
plt.tight_layout()
plt.savefig("latency_plot_AP.png", dpi=600)
plt.show()

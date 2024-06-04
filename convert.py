import json
import csv
import os
from datetime import datetime
import pandas as pd

def convert_channel_to_csv(input_dir, output_dir, channel_name):
    messages = []

    channel_dir = os.path.join(input_dir, channel_name)
    if not os.path.exists(channel_dir) or not os.path.isdir(channel_dir):
        print(f"Skipping {channel_dir} as it is not a directory.")
        return

    for filename in os.listdir(channel_dir):
        if filename.endswith('.json'):
            with open(os.path.join(channel_dir, filename), 'r', encoding='utf-8') as f:
                messages.extend(json.load(f))
    
    cleaned_messages = []
    for msg in messages:
        cleaned_msg = {
            "timestamp": datetime.fromtimestamp(float(msg.get("ts", 0))).strftime('%Y-%m-%d %H:%M:%S') if msg.get("ts") else None,
            "user": msg.get("user_profile", {}).get("display_name"),
            "text": msg.get("text")
        }
        cleaned_messages.append(cleaned_msg)

    # Create a DataFrame
    df = pd.DataFrame(cleaned_messages)

    # Sort by timestamp
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by='timestamp')

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Save to CSV
    output_file = os.path.join(output_dir, f"{channel_name}.csv")
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f'CSV file has been created for channel {channel_name}: {output_file}')

def convert_all_channels_to_csv(input_dir, output_dir):
    for channel_name in os.listdir(input_dir):
        channel_path = os.path.join(input_dir, channel_name)
        if os.path.isdir(channel_path):
            convert_channel_to_csv(input_dir, output_dir, channel_name)

if __name__ == "__main__":
    input_directory = 'slack_export'
    output_directory = 'output'
    convert_all_channels_to_csv(input_directory, output_directory)

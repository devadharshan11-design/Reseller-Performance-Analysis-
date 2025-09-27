import os
import subprocess
import sys

def setup_and_download_dataset():
    """
    Checks for Kaggle API credentials, then downloads and unzips the Olist dataset
    into a specific project path.
    """
    # --- MODIFIED PART ---
    # Define the absolute path for your data directory
    project_path = r'D:\SQL PROJECT'
    data_directory = os.path.join(project_path, 'olist_data')
    # --- END OF MODIFIED PART ---

    # Check for kaggle.json
    kaggle_config_dir = os.path.join(os.path.expanduser('~'), '.kaggle')
    if not os.path.exists(os.path.join(kaggle_config_dir, 'kaggle.json')):
        print("🚨 Error: 'kaggle.json' not found.")
        print(f"Please make sure your Kaggle API token is in this directory: {kaggle_config_dir}")
        sys.exit()

    # Create a directory for the data if it doesn't exist
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
        print(f"✅ Created directory: '{data_directory}'")

    # Construct the Kaggle CLI command
    command = [
        'kaggle', 'datasets', 'download',
        '-d', 'olistbr/brazilian-ecommerce',
        '-p', data_directory,
        '--unzip'
    ]

    # Execute the command
    print("\nDownloading and unzipping dataset... please wait.")
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"✅ Success! Dataset files are ready in the '{data_directory}' folder.")
    except subprocess.CalledProcessError as e:
        print(f"🚨 An error occurred during download: {e.stderr}")
    except FileNotFoundError:
        print("🚨 Error: 'kaggle' command not found. Is the 'kaggle' package installed correctly?")

# Run the function
if __name__ == "__main__":
    setup_and_download_dataset()
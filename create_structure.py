
import os

def create_structure():
    # Define the project structure
    dirs = [
        # Data directories
        os.path.join('data', 'train', 'images'),
        os.path.join('data', 'train', 'labels'),
        os.path.join('data', 'test', 'images'),
        os.path.join('data', 'test', 'labels'),
        os.path.join('data', 'val', 'images'),
        os.path.join('data', 'val', 'labels'),
        os.path.join('data', 'labels'),  # Generic labels folder
        
        # Augmented data directories
        os.path.join('aug_data', 'train', 'images'),
        os.path.join('aug_data', 'train', 'labels'),
        os.path.join('aug_data', 'test', 'images'),
        os.path.join('aug_data', 'test', 'labels'),
        os.path.join('aug_data', 'val', 'images'),
        os.path.join('aug_data', 'val', 'labels'),
        
        # Logs or Models if needed (common practice)
        'logs',
        'models'
    ]

    for d in dirs:
        try:
            os.makedirs(d, exist_ok=True)
            print(f"Created/Verified directory: {d}")
        except Exception as e:
            print(f"Error creating {d}: {e}")

    # Create a placeholder for .gitkeep in data if it's empty, 
    # just to ensure git tracks the folder structure if initialized.
    # (Optional, but good for "creating files" request)
    
if __name__ == "__main__":
    create_structure()

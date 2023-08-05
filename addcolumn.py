import os
import pandas as pd

def add_filename_column(file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)
    
    # Extract the filename from the file path
    filename = os.path.basename(file_path)
    
    # Add a new column with the filename
    df['Filename'] = filename
    
    # Save the DataFrame back to the same Excel file
    df.to_excel(file_path, index=False)
    
directory = r'C:\Users\Idea\Desktop\Companies Charge Index'

for filename in os.listdir(directory):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        file_path = os.path.join(directory, filename)
        add_filename_column(file_path)


import pandas as pd
import os

# Set the folder path where your Excel files are located
folder_path = r'C:\Users\Idea\Desktop\Companies Charge Index'  # Make sure to enclose the path in quotes

# Create an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):  # Consider only Excel files
        file_path = os.path.join(folder_path, filename)
        df = pd.read_excel(file_path)  # Read the Excel file into a DataFrame
        combined_data = combined_data.append(df, ignore_index=True)  # Append the data to the combined DataFrame

# Save the combined data to a new Excel file
combined_data.to_excel('combined_data_with_columns.xlsx', index=False)  # Enclose the filename in quotes



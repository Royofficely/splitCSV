import pandas as pd
import math
import os

def split_csv(input_file, num_splits):
    try:
        df = pd.read_csv(input_file)
        
      
        total_rows = len(df)
        rows_per_file = math.ceil(total_rows / num_splits)
        
        base_name = os.path.splitext(input_file)[0]
        
        created_files = []
        
        for i in range(num_splits):
            start_idx = i * rows_per_file
            end_idx = min((i + 1) * rows_per_file, total_rows)
            
            if start_idx >= total_rows:
                break
                
            split_df = df.iloc[start_idx:end_idx]
            
            output_file = f"{base_name}_part_{i + 1}.csv"
            
            split_df.to_csv(output_file, index=False)
            created_files.append(output_file)
            
        return created_files
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

if __name__ == "__main__":
    input_csv = "your_file.csv"
    number_of_splits = 3
    
    result_files = split_csv(input_csv, number_of_splits)
    
    if result_files:
        print(f"Successfully split into {len(result_files)} files:")
        for file in result_files:
            print(f"- {file}")

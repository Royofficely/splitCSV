# CSV Processing Tools

This repository contains two Python utilities for processing CSV files:
1. CSV to TXT Converter
2. CSV File Splitter

## Prerequisites

- Python 3.x
- pandas library (`pip install pandas`)

## CSV to TXT Converter

### Description
Converts a CSV file containing content and URLs into a formatted text file. Each entry in the output file is separated by a line of underscores.

### Usage
```python
from csv_to_txt import convert_csv_to_txt

input_csv = "path/to/your/input.csv"
output_txt = "path/to/your/output.txt"

convert_csv_to_txt(input_csv, output_txt)
```

### CSV File Format
Your input CSV should have the following columns:
- `URL`: Contains the webpage URL
- `Content`: Contains the main content
- `Chunk Number`: (Optional) Numbering of chunks

### Output Format
```
________
[Content]
Link: [URL]

```

## CSV File Splitter

### Description
Splits a large CSV file into multiple smaller files while preserving the header in each file.

### Usage
```python
from csv_splitter import split_csv

input_file = "path/to/your/large.csv"
number_of_splits = 3  # or any number you want

result_files = split_csv(input_file, number_of_splits)
```

### Features
- Preserves header in each split file
- Evenly distributes rows across files
- Creates sequentially numbered output files (e.g., original_part_1.csv, original_part_2.csv)
- Handles errors gracefully

### Output
The splitter will create files named:
- `[original_name]_part_1.csv`
- `[original_name]_part_2.csv`
- etc.

## Error Handling

Both tools include error handling for common issues:
- File not found errors
- Invalid file format errors
- General exceptions

## Example Code

### CSV to TXT Conversion
```python
import pandas as pd

def convert_csv_to_txt(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        with open(output_file, 'w', encoding='utf-8') as txt_file:
            for index, row in df.iterrows():
                txt_file.write("________\n")
                txt_file.write(f"{row['Content']}\n")
                txt_file.write(f"Link: {row['URL']}\n\n")
    except Exception as e:
        print(f"Error: {str(e)}")
```

### CSV Splitting
```python
import pandas as pd
import math

def split_csv(input_file, num_splits):
    try:
        df = pd.read_csv(input_file)
        rows_per_file = math.ceil(len(df) / num_splits)
        
        for i in range(num_splits):
            start_idx = i * rows_per_file
            end_idx = min((i + 1) * rows_per_file, len(df))
            split_df = df.iloc[start_idx:end_idx]
            split_df.to_csv(f"{input_file.rsplit('.', 1)[0]}_part_{i+1}.csv", index=False)
    except Exception as e:
        print(f"Error: {str(e)}")
```

## Troubleshooting

Common issues and solutions:

1. **FileNotFoundError**
   - Verify the input file path is correct
   - Check file permissions

2. **Encoding Issues**
   - Try specifying the encoding when reading the CSV: `pd.read_csv(file, encoding='utf-8')`

3. **Memory Issues**
   - For large files, consider processing in chunks
   - Reduce the number of splits

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open-source and available under the MIT License.

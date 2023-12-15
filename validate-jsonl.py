import json
import sys

def process_jsonl_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    json_object = json.loads(line)
                    print(f"Line {line_number}: JSON object successfully parsed.")
                except json.JSONDecodeError as e:
                    print(f"Line {line_number}: JSON decoding error - {e}")
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
    else:
        file_path = sys.argv[1]
        process_jsonl_file(file_path)

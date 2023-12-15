import argparse
import json

def validate_message_structure(messages):
    expected_roles = {"system", "user", "assistant"}
    if len(messages) != 3:
        return False
    for msg in messages:
        if not isinstance(msg, dict) or 'role' not in msg or 'content' not in msg:
            return False
        if msg['role'] not in expected_roles:
            return False
    return True

def process_jsonl_file(file_path, openai_mode):
    error_count = 0
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    json_object = json.loads(line)
                    if openai_mode:
                        if 'messages' in json_object and isinstance(json_object['messages'], list):
                            if not validate_message_structure(json_object['messages']):
                                print(f"Line {line_number}: Error - Invalid structure in 'messages' array.")
                                error_count += 1
                        else:
                            print(f"Line {line_number}: Error - JSON object does not contain a valid 'messages' attribute.")
                            error_count += 1
                except json.JSONDecodeError as e:
                    print(f"Line {line_number}: JSON decoding error - {e}")
                    error_count += 1

        if error_count == 0:
            print("Success: No errors found.")
        else:
            print(f"Total errors found: {error_count}")

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="JSONL Validator")
    parser.add_argument("file_path", help="Path to the JSONL file")
    parser.add_argument("--openai", action="store_true", help="Enable OpenAI mode")

    args = parser.parse_args()

    process_jsonl_file(args.file_path, args.openai)

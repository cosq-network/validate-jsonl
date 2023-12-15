# JSONL Validator

## Overview

This Python script is designed to validate JSONL (JSON Lines) files. JSONL files consist of multiple JSON objects, each on a separate line. The script checks the structure of each JSON object and performs specific validations.

## Features

- Validates the structure of JSON objects in a JSONL file.
- Checks for the presence of a "messages" attribute in each JSON object.
- Verifies that the "messages" attribute is an array.
- Validates the structure of the "messages" array, ensuring it contains exactly three objects.
- Each object in the "messages" array should have a "role" and "content," and the "role" should be one of "system," "user," or "assistant."

## Usage

```bash
python script.py <file_path> [--openai]
```

- `<file_path>`: Path to the JSONL file to be validated.
- `--openai`: (Optional) Enable OpenAI mode. This flag can be used to enable specific behavior related to OpenAI.

## Example

Validate a JSONL file:

```bash
python script.py path/to/your/file.jsonl
```

Enable OpenAI mode:

```bash
python script.py path/to/your/file.jsonl --openai
```

## Output

The script will print error messages for any validation issues encountered, including JSON decoding errors, missing "messages" attributes, and invalid "messages" array structures. If no errors are found, it will print a success message. In case of errors, it will also indicate the total number of errors found.

## Requirements

- Python 3.x
- argparse (standard library)
- json (standard library)

## License

This script is released under the [MIT License](LICENSE).

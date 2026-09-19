# Trivia Gen

Trivia Gen is a small Python script that retrieves computer science trivia questions from the [Open Trivia Database](https://opentdb.com/) and saves them to a CSV file.

## Requirements

- Python 3
- The `requests` package

Install the dependency with:

```bash
pip install requests
```

## Usage

Run the script from the project directory:

```bash
python triviagen.py
```

When prompted, enter:

1. The number of questions to generate.
2. A difficulty level: `easy`, `medium`, or `hard`.

The script creates a file named `tech trivia.csv` in the current directory. The file contains each question and its correct answer in two columns: `Question` and `Answer`.


# Wordlist Text Block Generator

This Python script allows you to generate blocks of text based on a list of words from an input file. These blocks of text have each line populated with randomly shuffled words, and their length is constrained to a specified target. At the end of the text block, a seed number is appended, which can be provided by the user or generated randomly.

## Features

- Load words from a specified file.
- Filter and shuffle words.
- Generate lines of text with controlled length.
- Embed a seed value to reproduce the same block in future runs.
- Option for the user to input a seed value or use a randomly generated one.
- Save the generated text block to a file with the seed value as its name.

## Usage

To use this script, simply run it with Python:

```bash
python passphraseoffline.py
```

Upon execution, you'll be prompted to enter a seed number. You can provide one, or press Enter to let the script generate a random seed. The generated text block will then be saved to a file with the seed value as its name.

### Output

The generated file will contain lines of text populated with shuffled words. The last line of the file will be the seed value used for generation.

## Functions

### 1. `load_words_from_file(wordlist)`

Loads words from the specified file and returns them as a list.

### 2. `create_string_of_words(words, target_length=35)`

Creates a string of words with a specified target length. Filters out words containing numbers or dots and ensures the output string's length is within one character of the target length.

### 3. `generate_text_block(seed_value=None)`

Generates a block of text based on the loaded wordlist. This function allows you to provide a seed value to reproduce a previously generated block, or leave it empty to generate a random seed.

### 4. `prompt_for_seed_and_generate_file()`

Prompts the user for a seed value and generates the text block. This function saves the block to a file and returns the filename.

## Note

Ensure that the `output.txt` file (or your desired wordlist file) is in the same directory as the script. The default wordlist file is `output.txt`.

## License

This script is provided as-is without any warranty. Use at your own discretion.d
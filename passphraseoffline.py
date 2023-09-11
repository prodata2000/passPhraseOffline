import random

def load_words_from_file(wordlist):
    """Load words from a file and return them as a list."""
    with open(wordlist, 'r') as f:
        return [word.strip() for word in f.read().split(',')]

def create_string_of_words(words, target_length=35):
    filtered_words = [word for word in words if not (any(char.isdigit() for char in word) or '.' in word)]
    random.shuffle(filtered_words)

    line = ""
    for word in filtered_words:
        if len(line) + len(word) + 1 <= target_length:
            line += (word.upper() + " ")
            if len(line) >= target_length:
                break
    return line.strip()

def replace_spaces_with_symbols(text):
    """Replace spaces in the text with a random special symbol."""
    symbols = "!@#$%^&*()[]{}<>"
    return ''.join(random.choice(symbols) if char == ' ' else char for char in text)

def generate_text_block(seed_value=None, replace_spaces=False):
    if seed_value is None:
        seed_value = random.randint(0, 99999999999)

    random.seed(seed_value)

    words = load_words_from_file('output.txt')
    lines = []

    for i in range(10):
        line = create_string_of_words(words)
        while not (34 <= len(line) <= 35):
            line = create_string_of_words(words)
        if replace_spaces:
            line = replace_spaces_with_symbols(line)
        lines.append(f"{i} {line}")

    seed_line = f"{seed_value}"
    lines.append(seed_line)

    return '\n'.join(lines), seed_value

def prompt_for_seed_and_generate_file():
    # Prompt the user for a seed value
    seed_value = input("Please enter a seed number (or press Enter to generate a random seed): ")

    # Prompt the user to replace spaces with special characters
    replace_spaces = input("Do you want to replace spaces with special characters? (yes/no): ").strip().lower() == 'yes'

    try:
        seed_value = int(seed_value)
    except ValueError:
        seed_value = None  # This will trigger the function to generate a random seed

    # Generate and save the text block
    text_block, seed = generate_text_block(seed_value, replace_spaces)
    wordlist = f"{seed}.txt"
    with open(wordlist, 'w') as f:
        f.write(text_block)

    return wordlist

if __name__ == "__main__":
    filename = prompt_for_seed_and_generate_file()
    print(f"Text block saved to {filename}")

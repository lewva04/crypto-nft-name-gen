import random

def load_words(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def generate_name(adjectives, nouns):
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

def main():
    adjectives = load_words("data/adjectives.txt")
    nouns = load_words("data/nouns.txt")
    name = generate_name(adjectives, nouns)
    print("🎨 Your random NFT name:\n")
    print(name)

if __name__ == "__main__":
    main()

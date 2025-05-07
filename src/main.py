import sys
from word import Word

def main():
    num_words = 1
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) == 2:
        num_words = int(sys.argv[1])
    else:
        print("Usage: python main.py [num_words]")
        sys.exit(1)
    used = set()
    words = [Word() for _ in range(num_words)]
    num_guesses = num_words + 5
    while num_words > 0 and num_guesses > 0:
        print(f"Guesses left: {num_guesses}")
        print(f"Words left: {num_words}")
        print(f"Used letters: {', '.join(sorted(used))}")
        guess = input("Guess a word: ")
        if guess == "exit":
            break
        if len(guess) != 5:
            print("Please enter a 5 letter word.")
            continue
        num_guesses -= 1
        for word in words:
            if word.word == guess:
                num_words -= 1
                word.guessed = True
            else:
                word.guesses.append(guess)
                guess_map = ""
                for i in range(len(word.word)):
                    used.add(guess[i])
                    if word.word[i] == guess[i]:
                        guess_map += "O "
                    elif guess[i] in word.word:
                        guess_map += "/ "
                    else:
                        guess_map += "X "
                word.guesses_map.append(guess_map)
            for i in range(len(word.guesses)):
                print(f"{i+1}: {word.guesses_map[i]}        {word.guesses[i]}")
            if word.guessed:
                print(word.word)
            print("____________________________")
    if num_words == 0:
        print(f"You guessed all {len(words)} words!")
    else:
        print(f"You ran out of guesses! You guessed {len(words) - num_words} words.")
    

if __name__ == "__main__":
    main()
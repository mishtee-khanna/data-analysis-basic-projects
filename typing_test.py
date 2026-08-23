import time
import random

sentences = [
    "The sun rose quietly over the distant mountains.",
    "She forgot her umbrella before leaving the house.",
    "The little dog chased a butterfly across the garden.",
    "We watched an interesting movie after dinner.",
    "My brother enjoys playing cricket every weekend.",
    "The teacher explained the concept with a simple example.",
    "A bright rainbow appeared after the heavy rain.",
    "He bought a new notebook from the bookstore.",
    "The children were laughing near the playground.",
    "I usually drink coffee while studying in the morning.",
    "The old library has thousands of fascinating books.",
    "She completed her assignment before the deadline.",
    "Our team won the competition yesterday.",
    "The train arrived at the station exactly on time.",
    "He loves listening to music while working.",
    "The flowers in the garden smell wonderful.",
    "We visited a beautiful museum during our trip.",
    "My laptop suddenly stopped working during the presentation.",
    "The chef prepared a delicious meal for everyone.",
    "She learned Python through online tutorials.",
    "The stars looked incredibly bright tonight.",
    "I found an interesting article about artificial intelligence.",
    "The students discussed their project during lunch.",
    "He practices coding problems every evening.",
    "A gentle breeze moved the curtains near the window."
]

def measure_accuracy(user_input, test_sentence):
    correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b)
    accuracy = (correct_chars / len(test_sentence)) * 100 if test_sentence else 0
    return accuracy 

def typing_test():
    test_sentence = random.choice(sentences)
    print("Type the following sentence as fast as possible")
    print(test_sentence)
    input("Press ENTER when you are ready...")
    start_time = time.time() # Measure the start time
    user_input = input("\nStart Typing : \n")
    end_time = time.time() # Measure the end time
    time_taken = end_time - start_time
    word_count = len(test_sentence.split(" "))

    print("RESULT")
    print(f"Time Taken : {time_taken} seconds")
    print(f"Word Count : {word_count}")
    print(f"Typing speed: {word_count / (time_taken / 60):.2f} words per minute")
    accuracy = measure_accuracy(user_input, test_sentence)
    print(f"Accuracy : {accuracy:.2f}")


typing_test()

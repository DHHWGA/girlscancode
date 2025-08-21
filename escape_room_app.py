import time
import threading

# Global timer
time_limit = 300  # 5 minutes
start_time = time.time()

def check_time():
    if time.time() - start_time > time_limit:
        print("\n⏰ Time's up! You couldn't escape in time.")
        exit()

def intro():
    print("🔐 Welcome to the HWGA Escape Room! 🔐")
    time.sleep(1)
    print("\nCreated by the Girls Can Code Club at Handsworth Wood Girls’ Academy. 💻✨")
    time.sleep(2)
    print("\nYou have 5 minutes to escape. Type 'hint' if you need help. Good luck!\n")
    time.sleep(2)

def first_puzzle():
    check_time()
    print("🧩 Puzzle 1: Escape the depths")
    print("Riddle: \"I speak without a mouth and hear without ears. I have no body, but I come alive with wind.\"")
    while True:
        answer = input("Your answer: ").strip().lower()
        check_time()
        if answer == "hint":
            print("💡 Hint: It's something you would hear in an empty room.")
        elif answer == "echo":
            print("✅ Correct! The door clicks open...\n")
            break
        else:
            print("❌ Try again or type 'hint'.")

def second_puzzle():
    check_time()
    print("🧩 Puzzle 2: The LRC maze")
    print("Choose the correct direction at each of the 5 turns: left, right, or forward.\n")
    correct_path = ["left", "forward", "right", "left", "forward"]
    for i, correct_turn in enumerate(correct_path, start=1):
        while True:
            choice = input(f"Turn {i} - Which way? ").strip().lower()
            check_time()
            if choice == "hint":
                print("💡 Hint: Think of alternating directions with a strong finish.")
            elif choice == correct_turn:
                print("✅ You move deeper into the maze...\n")
                break
            else:
                print("❌ Dead end! The maze resets...\n")
                return second_puzzle()
    print("🎉 You’ve made it through the maze!\n")

def final_puzzle():
    check_time()
    print("🧩 Final Puzzle: Open the door")
    print("Clue: 'The code is the year the school was reopened after our being rebuilt'")
    correct_code = "2024"
    while True:
        attempt = input("Enter the 4-digit code: ").strip()
        check_time()
        if attempt.lower() == "hint":
            print("💡 Hint: In human terms the school is just starting to walk and talk.")
        elif attempt == correct_code:
            print("🔓 The lock beeps and clicks open...")
            print("🎉 Congratulations! You've escaped the room!")
            break
        else:
            print("❌ Incorrect. Try again or type 'hint'.")

def start_escape_room():
    intro()
    first_puzzle()
    second_puzzle()
    final_puzzle()

start_escape_room()

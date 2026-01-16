print("Welcome to my Cybersecurity quiz!")

playing = input("Do you want to play? (yes/no): ").strip().lower()
if playing != "yes":
    print("No problem—see you next time!")
    quit()

print("\nOkay! Let's play :)")
score = 0

questions = [
    {
        "question": "1) What does CIA stand for in cybersecurity?",
        "options": {
            "A": "Control, Integrity, Authentication",
            "B": "Confidentiality, Integrity, Availability",
            "C": "Confidentiality, Identification, Access",
            "D": "Compliance, Investigation, Authorization"
        },
        "answer": "B"
    },
    {
        "question": "2) Which of the following is the strongest password?",
        "options": {
            "A": "Password123",
            "B": "qwerty2024",
            "C": "S0ccer!",
            "D": "vT9#kQ2!zL7@pX"
        },
        "answer": "D"
    },
    {
        "question": "3) What is phishing?",
        "options": {
            "A": "Encrypting files to protect them",
            "B": "Tricking people into revealing sensitive information",
            "C": "Blocking malicious traffic on a firewall",
            "D": "Scanning a network for open ports"
        },
        "answer": "B"
    },
    {
        "question": "4) What does MFA stand for?",
        "options": {
            "A": "Multiple File Access",
            "B": "Managed Firewall Appliance",
            "C": "Multi-Factor Authentication",
            "D": "Main Function Authorization"
        },
        "answer": "C"
    },
    {
        "question": "5) Which tool is commonly used for packet capture and network analysis?",
        "options": {
            "A": "Wireshark",
            "B": "Photoshop",
            "C": "Excel",
            "D": "PowerPoint"
        },
        "answer": "A"
    },
    {
        "question": "6) What is ransomware?",
        "options": {
            "A": "A malware that demands payment to restore access to data",
            "B": "A security patch for operating systems",
            "C": "A tool for password management",
            "D": "A type of firewall rule"
        },
        "answer": "A"
    },
    {
        "question": "7) What does HTTPS provide that HTTP does not?",
        "options": {
            "A": "Faster browsing speed",
            "B": "Encryption in transit",
            "C": "Unlimited bandwidth",
            "D": "Automatic virus removal"
        },
        "answer": "B"
    },
    {
        "question": "8) Which of the following is an example of a DDoS attack?",
        "options": {
            "A": "A single hacker guessing your password repeatedly",
            "B": "A system installing updates overnight",
            "C": "Many devices flooding a server with traffic to take it down",
            "D": "Encrypting a file with AES"
        },
        "answer": "C"
    },
    {
        "question": "9) What is the main purpose of a firewall?",
        "options": {
            "A": "To speed up the computer",
            "B": "To monitor employee productivity",
            "C": "To filter and control network traffic based on rules",
            "D": "To recover deleted files"
        },
        "answer": "C"
    },
    {
        "question": "10) What is a vulnerability?",
        "options": {
            "A": "A security weakness that can be exploited",
            "B": "A type of encrypted message",
            "C": "A safe backup copy",
            "D": "A guaranteed protection method"
        },
        "answer": "A"
    }
]


def ask_question(q):
    print("\n" + q["question"])
    for key, value in q["options"].items():
        print(f"   {key}) {value}")

    while True:
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer in ["A", "B", "C", "D"]:
            return user_answer
        print("Please enter only A, B, C, or D.")


for q in questions:
    user_answer = ask_question(q)
    if user_answer == q["answer"]:
        print("Correct! ✅")
        score += 1
    else:
        correct_letter = q["answer"]
        correct_text = q["options"][correct_letter]
        print(f"Incorrect ❌  The correct answer was {correct_letter}) {correct_text}")

percent = (score / len(questions)) * 100
print("\n==============================")
print(f"You got {score} out of {len(questions)} correct.")
print(f"Score: {percent:.0f}%")
print("==============================\n")

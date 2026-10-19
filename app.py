import random
import time

def get_quiz():
  fcards = {}

  with open("quiz.txt", "r") as file:
    for line in file:
      line = line.strip()
      if not line:
        continue

      parts = line.split("|")

      Q = parts[0]
      A = parts[1]

      fcards[Q] = A
  return fcards

def add_quiz():
  Q = input("Whats the question you would like to add? > ")
  A = input("Whats the answer for that question? > ")
  QnA = [Q, A]
  line = "|".join(QnA)

  with open("quiz.txt", "a") as file:
    file.write(line + "\n")

def quiz():
  fcards = get_quiz()
  quiz_running = True
  score = 0


  if not fcards:
    print("No questions found!")
    return
  
  while quiz_running:
    Q = random.choice(list(fcards.keys()))
    A = fcards[Q]

    print(f"Question: {Q}")
    while True:
      uA = input("> ").strip()

      if uA == "exit":
        print(f"\nQuiz ended. Your final score is {score}!")
        quiz_running = False
        break
      elif uA == "answer":
        print(f"Answer: {A}")
        score -= 1
        break
      elif uA == A:
        print("Correct!")
        score += 1
        break
      else:
        print("Incorrect!")
        score -= 1
        break

def main():
  while True:
    print('Type "quiz" to study flashcards, and "add" to add a question to the flashcards.')
    print('Type "exit" to exit.')
    uI = input("> ")

    if uI == "quiz":
      quiz()
    elif uI == "add":
      add_quiz()
    elif uI == "exit":
      print("Thank you for playing. I mean studying... :D")
      time.sleep(5)
      break
    else:
      print("Try Again!")

if __name__ == "__main__":
    main()
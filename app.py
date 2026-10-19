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
      A = parts[1].lower()

      fcards[Q] = A
  return fcards

def add_quiz():

  Q = input("Whats the question you would like to add? > ")
  Q = "".join(["\n", Q])
  A = input("Whats the answer for that question? > ")
  QnA = [Q, A]
  line = "|".join(QnA)

  with open("quiz.txt", "a") as file:
    file.write(line)

def save_score(timestamp, score):
  lines = []
  current_hs = 0
  try:
    with open("score.score", 'r') as file:
      lines = file.readlines()
      if lines:
        first_line = lines[0].strip()
        parts = first_line.split("|")
        current_hs = int(parts[1])
      pass
  except FileNotFoundError:
    pass

  is_new_record = score > current_hs

  new_entry = f"{timestamp}|{score}"
  if is_new_record:
    new_entry += "|h"

  if not lines:
    lines.append(new_entry + "\n")
    lines.append(new_entry + "\n")
  elif is_new_record:
    lines[0] = new_entry + "\n"
    lines.append(new_entry + "\n")
  else:
    lines.append(new_entry + "\n")

  with open("score.score", "w") as file:
    file.writelines(lines)

def fetch_hs():
  try:
    with open("score.score", "r") as file:
      first_line = file.readline().strip()
      if not first_line:
        return 0
      hs_list = first_line.split("|")
      high_score = hs_list[1]
      high_score = int(high_score)
      return high_score
  except FileNotFoundError:
    return 0

def quiz():
  fcards = get_quiz()
  quiz_running = True
  score = 0
  timestamp = time.strftime("%Y-%m-%d %H:%M:%S")


  if not fcards:
    print("No questions found!")
    return


  print(f"Your current high score is {fetch_hs()}")

  while quiz_running:
    Q = random.choice(list(fcards.keys()))
    A = fcards[Q]

    print(f"Question: {Q}")
    while True:
      uA = input("> ").strip().lower()

      if uA == "exit":
        print(f"\nQuiz ended. Your final score is {score}!")
        quiz_running = False
        save_score(timestamp, score)
        break
      elif uA == "answer":
        print(f"(+0) Answer: {A}")
        break
      elif uA == "score":
        print(score)
        break
      elif uA == "hs":
        print(fetch_hs())
        break
      elif uA == A:
        print("(+1) Correct!")
        score += 1
        break
      else:
        print(f"(-1) Incorrect! Correct answer was: {A}")
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
    elif uI == "hs":
      print(fetch_hs())
    elif uI == "exit":
      print("Thank you for playing. I mean studying... :D")
      time.sleep(5)
      break
    else:
      print("Try Again!")

if __name__ == "__main__":
    main()
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
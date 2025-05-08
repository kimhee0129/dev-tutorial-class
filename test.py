import random
from typing import List, Dict


class Student:
    def __init__(self, name: str, scores: Dict[str, int]):
        self.name = name
        self.scores = scores

    def average(self) -> float:
        return sum(self.scores.values()) / len(self.scores)

    def __str__(self):
        return f"{self.name}: {self.average():.2f}"


def generate_students(n: int) -> List[Student]:
    subjects = ['Math', 'English', 'Science']
    students = []
    for i in range(n):
        name = f"Student{i+1}"
        scores = {subject: random.randint(50, 100) for subject in subjects}
        students.append(Student(name, scores))
    return students


def save_to_file(students: List[Student], filename: str):
    try:
        with open(filename, 'w') as f:
            for student in students:
                f.write(str(student) + '\n')
    except IOError as e:
        print(f"파일 저장 중 오류 발생: {e}")


def load_names(filename: str) -> List[str]:
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


def main():
    print("학생 성적 생성 중...")
    students = generate_students(5)
    for s in students:
        print(s)

    print("\n파일 저장 중...")
    save_to_file(students, 'students.txt')

    print("\n저장된 내용:")
    names = load_names('students.txt')
    for name in names:
        print(name)


if __name__ == "__main__":
    main()
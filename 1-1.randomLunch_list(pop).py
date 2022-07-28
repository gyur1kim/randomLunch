# 세 번째. 배열과 random 모듈을 이용함 -> random.shuffle을 이용해 학생들을 무작위로 섞고, pop 메서드를 이용해 배열의 맨 뒤에만 접근하면 된다.


# 1. 배열이랑 random 모듈 이용
import random

students = ['기*석', '김*림', '김*리', '김*수', '김*식',
            '김*준', '김*늬', '류*규', '박*현', '박*하',
            '서*준', '신*호', '안*나', '양*진', '오*원',
            '유*훈', '이*진', '이*민', '이*준', '이*빈',
            '정*진', '정*정', '정*상', '조*주', '최*현']

########## 이름 예쁘게 출력하기 위한 코드 ###########
studentsName = ''
for i, name in enumerate(students, 1):
    if i%5 == 1:
        studentsName += '| '
    studentsName += f'{name} | '
    if i % 5 == 0:
        studentsName += '\n'
print('===========<< 밥 짝궁을 찾아서 >>==========')
print()
print(studentsName)
print('=========================================')
print()
##################################################


# 1. 못오신 분들 제외하기
atHome = input('못오신 분들 이름 적기(스페이스로 구분, 다 오셨으면 그냥 엔터) : ').split()

# 1-1. 이름을 적다가 오타가 난 경우를 대비하자.
while True:
    try:
        for home in atHome:
            students.remove(home)
    except ValueError:
        print()
        print(f"'{home}'에서 오타가 났습니다\n")
        atHome = input('오타 난 이름부터 다시 입력(스페이스로 구분) : ').split()
    else:
        break


# 2. 남은 인원을 3명,4명으로 나누면 총 몇 조가 나오는지 구하기 -> Greedy 사용
partition_dict = {}
studentsLength = len(students)
while True:
    if studentsLength < 0:
        break

    if studentsLength % 4 == 0:
        partition_dict.update({'4': studentsLength // 4})
        break
    else:
        partition_dict.update({'3': partition_dict.get('3', 0) + 1})
        studentsLength -= 3

# 2-1. 현재 인원 수로 4명/3명인 조를 만들 수 없다면?
if studentsLength < 0:
    print('사람을 4~3명인 조로 만들 수가 없어요...! 그냥 알아서 드세요')
    exit()


# 3. 위의 결과를 이용해 사람 나누기
# 인원별 조의 수를 활용해 사람을 뽑는다(random.choice 이용함) ex) 위의 딕셔너리 결과가 {'3':2, '4':3} -> 3명인 조 2개, 4명인 조 3개
# 3중 for문은... 최악이지만.... -> 3중 for문인줄 알았으나, 교수님께서 항상 for문이 3개라고 해서 O(n^3)이라고 하시지는 않았다.
random.shuffle(students)                # 학생들을 무작위로 섞기
partition_output = []                   # 결과를 담아낼 리스트
for k, v in partition_dict.items():     # 딕셔너리의 key와 value를 뽑아낸다.
    for _ in range(v):                  # value는 조를 몇 개 만들어야 하는지 나타낸다
        part = []                       # 한 조를 담기 위한 리스트
        for _ in range(int(k)):         # key는 한 조에서 몇 명을 뽑을지를 나타낸다, 문자열을 정수로 바꿔줘야 한다.
            student = students.pop()    # 무작위로 섞인 학생 리스트에서 맨 마지막 학생을 뽑는다
            part.append(student)        # 그 학생을 part 리스트에 담는다.
        partition_output.append(part)   # 한 조가 완성되면, partition_output에 담는다.


# 4. 결과를 예쁘게 출력하자..... FE지망생으로서 보여지는 화면에도 어느 정도 신경써주자
print()
output = ''
for i, part in enumerate(partition_output, 1):
    output += f'<<{i}조>>  |'
    for student in part:
        output += f' {student} |'
    output += '\n'
print(output)

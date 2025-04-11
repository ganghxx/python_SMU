def read_single_digit(n):
    nums_in_kor = "영일이삼사오육칠팔구"
    print(nums_in_kor[n], end=" ")

def read_number(n):
    for i in str(n):
        read_single_digit(int(i))

read_number(int(input("세 자리 정수 입력: ")))

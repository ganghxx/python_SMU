import os
import pickle

def input_scores():
    scores = []
    cnt = 1
    while True:
        score = int(input(f'#{cnt}? '))
        if score >= 0:
            scores.append(score)
            cnt += 1
        else:
            print()
            return scores
        
def get_average(scores):
    total = sum(scores)
    avg = total/len(scores)
    return avg

def show_scores(scores):
    print('개인점수: ', end='')
    for i in scores:
        print(i,'', end='')
    print()


file_path = 'score.bin'

if os.path.exists(file_path):
    print('[파일 읽기]')
    print()
    with open(file_path, 'rb') as f:
        scores = pickle.load(f)
else:
    print('[점수 입력]')
    scores = input_scores()
    with open(file_path, 'wb') as f:
        pickle.dump(scores, f)

print('[점수 출력]')
show_scores(scores)
print(f'평균: {get_average(scores):.1f}')
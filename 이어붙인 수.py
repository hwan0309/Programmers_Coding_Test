# 정수가 담긴 리스트 num_list가 주어집니다.
# num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    answer_1 = ''
    answer_2 = ''
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            answer_1 += str(num_list[i])
        else:
            answer_2 += str(num_list[i])
    answer = int(answer_1) + int(answer_2)
    return answer
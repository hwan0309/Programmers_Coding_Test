# 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면
# 1을 크면 0을 return하도록 solution 함수를 완성해주세요.


def solution(num_list):
    answer = 0
    multiply = 1
    add = 0

    for i in num_list:
        multiply *= i
        add += i

    answer = 1 if multiply < add * add else 0

    return answer
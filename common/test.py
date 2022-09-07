import copy


def check_solution(solution, test_case_list):
    for test_case in test_case_list:
        temp = copy.deepcopy(test_case)
        if solution(temp["input"]) != temp["output"]:
            print('test is not passed :(')
            return False
    print('test is passed!')
    return True

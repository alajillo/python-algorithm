def check_solution(solution, test_case_list):
    for test_case in test_case_list:
        if solution(test_case["input"]) != test_case["output"]:
            return False
    return True



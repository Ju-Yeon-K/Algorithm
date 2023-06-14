
from collections import Counter
from datetime import datetime
import os
import re


def problem_source_code():
    py_problem_solve_code_list = []
    java_problem_solve_code_list = []

    directory_list = [directory for directory in os.listdir("./백준") if ". " in directory]

    for directory in directory_list:
        py_code_list = [file for file in os.listdir(f"./백준/{directory}") if file.endswith(".py")]
        java_code_list = [file for file in os.listdir(f"./백준/{directory}") if file.endswith(".java")]
        if py_code_list:
            py_problem_solve_code_list.append(py_code_list[0][:-3])
        if java_code_list:
            java_problem_solve_code_list.append(java_code_list[0][:-5])

    # py_name_list = [re.findall(r'\[[^)]*\]', code_name) for code_name in py_problem_solve_code_list]
    # py_name_list = [name[0].replace("[", "").replace("]", "") for name in py_name_list if len(name) > 0]
    

    return py_problem_solve_code_list, java_problem_solve_code_list


def make_count_info(total_code_num, code_cnt_info):
    count_info = f"#### 현재까지 풀어본 총 문제 수 : {total_code_num}개\n"

    for name in code_cnt_info:
        temp = f"- {name[0]} - {name[1]}개\n"
        count_info += temp

    return count_info


def make_read_me(py_name_list, java_name_list):
    return f"""# Baekjoon
<img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/-JAVA-007396?style=flat&logo=OpenJDK&logoColor=white"> 

- Python 문제 리스트업
{py_name_list}

- Java 문제 리스트업
{java_name_list}
"""


def update_readme_md():
    py_name_list, java_name_list = problem_source_code()

    readme = make_read_me(py_name_list=py_name_list, java_name_list=java_name_list)

    return readme


if __name__ == "__main__":
    readme = update_readme_md()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)

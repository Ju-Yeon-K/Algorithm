
import os

def problem_source_code():
    py_problem_list = []
    java_problem_list = []

    for (path, dir, files) in os.walk("./백준/"):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            problem_name = path.split('/')[-1]
            
            if ext == '.py':
                py_problem_list.append(f'[{problem_name}](https://www.acmicpc.net/problem/{problem_name.split(".")[0]}) [Code]({path[1:]}/{problem_name.split(".")[1].lstrip()}.py)')
            if ext == '.java':
                java_problem_list.append(f'[{problem_name}](https://www.acmicpc.net/problem/{problem_name.split(".")[0]}) [Code]({path[1:]}/{problem_name.split(".")[1].lstrip()}.java)')

    return py_problem_list, java_problem_list


def make_read_me(py_name_list, java_name_list):
    return f"""# Baekjoon
<img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/-JAVA-007396?style=flat&logo=OpenJDK&logoColor=white">   
(푼 문제 자동으로 README.md 업데이트됨.)   
   

--- 
 🐥 이 README.md 는 매크로에 의해 자동 업데이트됩니다.     
 🐣 문제 풀이 코드는 백준/Gold,Silver,Bronze/... 에 있으니 참고해주세요.   
 
 --- 
  ✔️ Python 문제 리스트업   
    - {'<br>    - '.join(py_name_list)}   
    
--- 
    
 ✔️ Java 문제 리스트업   
    - {'<br>    - '.join(java_name_list)}

"""


def update_readme_md():
    py_name_list, java_name_list = problem_source_code()
    readme = make_read_me(py_name_list=py_name_list, java_name_list=java_name_list)

    return readme


if __name__ == "__main__":
    readme = update_readme_md()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)

## Template Setup Guide

Use this template to learn python and complete [practice projects](https://github.com/panaversity/learn-cloud-native-modern-python/tree/main/09_python_crash_course/projects) in Cloud Native Style Development Environment.

### PreRequisite:

1. Installed Docker
2. Add DevContianer Extension to VS Code
3. Knows the purpose of `docker compose up --build -d` and `docker compose down` commands

## Setup

1. Clone the repp and open folder `cnai_python_starter_template` or it's code in VS code

2. Ensure that in VS code terminal if you type `dir` or `ls` the output is:

```bash
D:\Ali Files\PIAIC Course\Quartar 3\Python Assignments\Assignment 03> dir
Volume in drive D is New Volume
 Volume Serial Number is 1C21-8DF0

 Directory of D:\Ali Files\PIAIC Course\Quartar 3\Python Assignments\Assignment 03

08/07/2024  08:38 PM    <DIR>          .
08/07/2024  08:37 PM    <DIR>          ..
08/07/2024  08:38 PM               249 compose.yml
08/07/2024  08:38 PM               448 Dockerfile
08/07/2024  08:51 PM                48 main.py
08/07/2024  08:52 PM             1,085 README.md
               4 File(s)          1,830 bytes
               2 Dir(s)  32,267,882,496 bytes free
```

3. Start Template

In Terminal run `docker compose up --build -d`

4. Open the Container in VSCode - now using the DevContainer Remote Explorer open the Container in VS Code

5. Do all your coding challenges - make python files and run them in vs code.

6. After practice close dev container and in terminal run `docker compose down`


from flask import Flask
app = Flask(name)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if name == 'main':
    app.run(debug=True


Last login: Fri Sep  6 17:05:15 on ttys008
zion@miniMac-9 ~ % ls
11.mp4				Parallels
2023-11-14 21-34-47.mp4		Pictures
Applications			Public
Atomic				RedTiger-Tools
Beast_Bomber			Skia-macOS-Release-x64.zip
Darkus				SocialSploit
Deanon				Windows 10 (1).pvm
Desktop				explosion.dsc
Discord-All-Tools-In-One	installer
Documents			noblack-mail
Downloads			satoshi
Library				sherlock
Lightumin			skia-m102
LittleBrother			Безіменний 2.AAE
Mine-imator			Безіменний 2.mp4
Movies				Безіменний.mp4
Music
zion@miniMac-9 ~ % ls
11.mp4				Parallels
2023-11-14 21-34-47.mp4		Pictures
Applications			Public
Atomic				RedTiger-Tools
Beast_Bomber			Skia-macOS-Release-x64.zip
Darkus				SocialSploit
Deanon				Windows 10 (1).pvm
Desktop				explosion.dsc
Discord-All-Tools-In-One	installer
Documents			noblack-mail
Downloads			satoshi
Library				sherlock
Lightumin			skia-m102
LittleBrother			Безіменний 2.AAE
Mine-imator			Безіменний 2.mp4
Movies				Безіменний.mp4
Music
zion@miniMac-9 ~ % cd Desktop
zion@miniMac-9 Desktop % ;s
zsh: command not found: s
zion@miniMac-9 Desktop % ls
Codepad.app		Computer Science	Новая папка
zion@miniMac-9 Desktop % cd 'Computer Science
quote> cd Desktop
quote> 
quote> cd Desktop
quote> 
quote> 
quote> 
zion@miniMac-9 Desktop % ls
Codepad.app		Computer Science	Новая папка
zion@miniMac-9 Desktop % cd 'Computer Science'
zion@miniMac-9 Computer Science % ls
Python
zion@miniMac-9 Computer Science % mkdir python_work
zion@miniMac-9 Computer Science % ls
Python		python_work
zion@miniMac-9 Computer Science % cd python_work
zion@miniMac-9 python_work % ls
zion@miniMac-9 python_work % touch test1.py
zion@miniMac-9 python_work % ls
test1.py
zion@miniMac-9 python_work % python3 test1.py
Hello, world!
zion@miniMac-9 python_work % cd ..            
zion@miniMac-9 Computer Science % ls
Python		python_work
zion@miniMac-9 Computer Science % cd Python
zion@miniMac-9 Python % cd stepik
zion@miniMac-9 stepik % ls
test1.py	test2.py
zion@miniMac-9 stepik % cd test2.py
cd: not a directory: test2.py
zion@miniMac-9 stepik % python3 test2.py
  File "/Users/zion/Desktop/Computer Science/Python/Stepik/test2.py", line 3
    d3 = num 5 100
             ^
SyntaxError: invalid syntax
zion@miniMac-9 stepik % python3 test2.py
  File "/Users/zion/Desktop/Computer Science/Python/Stepik/test2.py", line 3
    d3 = num 5 100
             ^
SyntaxError: invalid syntax
zion@miniMac-9 stepik % python3 test2.py
123
Traceback (most recent call last):
  File "/Users/zion/Desktop/Computer Science/Python/Stepik/test2.py", line 3, in <module>
    d3 = num % 100
         ~~~~^~~~~
TypeError: not all arguments converted during string formatting
zion@miniMac-9 stepik % python3 test2.py
123
23
zion@miniMac-9 stepik % 
  [Восстановлен 6 сент. 2024 г., 19:33:57]
Last login: Fri Sep  6 19:33:52 on console
Restored session: Fri Sep  6 19:32:58 EEST 2024
zion@miniMac-9 stepik % 
  [Восстановлен 6 сент. 2024 г., 20:13:13]
Last login: Fri Sep  6 20:13:05 on console
/bin/date: option requires an argument -- r
usage: date [-jnRu] [-I[date|hours|minutes|seconds]] [-f input_fmt]
            [-r filename|seconds] [-v[+|-]val[y|m|w|d|H|M|S]]
            [[[[mm]dd]HH]MM[[cc]yy][.SS] | new_date] [+output_fmt]
/Users/zion/.zsh_sessions/5675A469-F52F-473F-A97A-FC8D702DC2AA.session:2: command not found: Saving
zion@miniMac-9 stepik % 
  [Восстановлен 6 сент. 2024 г., 20:16:45]
Last login: Fri Sep  6 20:16:36 on console
zion@miniMac-9 stepik % 
  [Восстановлен 7 сент. 2024 г., 10:48:34]
Last login: Sat Sep  7 10:48:28 on console
zion@miniMac-9 stepik % ls
test1.py	test2.py
zion@miniMac-9 stepik % ls
test1.py	test2.py
zion@miniMac-9 stepik % cd ..
zion@miniMac-9 Python % ls
Stepik
zion@miniMac-9 Python % ls
python_work	stepik
zion@miniMac-9 Python % cd python_work
zion@miniMac-9 python_work % ls\
> ls
zsh: command not found: lsls
zion@miniMac-9 python_work % ls
test1.py
zion@miniMac-9 python_work % dir
zsh: command not found: dir
zion@miniMac-9 python_work % ls 
name.py		test1.py
zion@miniMac-9 python_work % python3 name.py
Ada Lovelace
zion@miniMac-9 python_work % python3 full_name.py
ada lovelace
zion@miniMac-9 python_work % python3 format.py   
Hello, <built-in method title of str object at 0x102525970>!
zion@miniMac-9 python_work % python3 format.py
Hello, Ada Lovalace!
zion@miniMac-9 python_work % python3 full_name.py
ada lovelace
zion@miniMac-9 python_work % ls                  
  [Восстановлен 8 сент. 2024 г., 09:25:53]
Last login: Sun Sep  8 09:25:45 on console
zion@miniMac-9 python_work % pip install flask

Collecting flask
  Downloading flask-3.0.3-py3-none-any.whl.metadata (3.2 kB)
Collecting Werkzeug>=3.0.0 (from flask)
  Downloading werkzeug-3.0.4-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from flask)
  Downloading jinja2-3.1.4-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.1.2 (from flask)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from flask)
  Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Collecting blinker>=1.6.2 (from flask)
  Downloading blinker-1.8.2-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->flask)
  Downloading MarkupSafe-2.1.5-cp312-cp312-macosx_10_9_universal2.whl.metadata (3.0 kB)
Downloading flask-3.0.3-py3-none-any.whl (101 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.7/101.7 kB 50.6 kB/s eta 0:00:00
Downloading blinker-1.8.2-py3-none-any.whl (9.5 kB)
Downloading click-8.1.7-py3-none-any.whl (97 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 38.1 kB/s eta 0:00:00
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.4-py3-none-any.whl (133 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.3/133.3 kB 24.7 kB/s eta 0:00:00
Downloading werkzeug-3.0.4-py3-none-any.whl (227 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 227.6/227.6 kB 25.1 kB/s eta 0:00:00
Downloading MarkupSafe-2.1.5-cp312-cp312-macosx_10_9_universal2.whl (18 kB)
Installing collected packages: MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, flask
Successfully installed Jinja2-3.1.4 MarkupSafe-2.1.5 Werkzeug-3.0.4 blinker-1.8.2 click-8.1.7 flask-3.0.3 itsdangerous-2.2.0

[notice] A new release of pip is available: 24.1.2 -> 24.2
[notice] To update, run: pip install --upgrade pip
zion@miniMac-9 python_work % 
zion@miniMac-9 python_work % ls
format_title.py	full_name.py	hello_world.py	name.py
zion@miniMac-9 python_work % cd mkdir flask
cd: string not in pwd: mkdir
zion@miniMac-9 python_work % mkdir flask
zion@miniMac-9 python_work % ls
flask		full_name.py	name.py
format_title.py	hello_world.py
zion@miniMac-9 python_work % cd flask
zion@miniMac-9 flask % touch app1.py
zion@miniMac-9 flask % ls
app1.py
zion@miniMac-9 flask % ls
app1.py
zion@miniMac-9 flask % nano app1.py
zion@miniMac-9 flask % nano app1.py

  UW PICO 5.09                                File: app1.py                                Modified  

from flask import Flask 
app = Flask(name)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if name == 'main':
    app.run(debug=True)















^G Get Help     ^O WriteOut     ^R Read File    ^Y Prev Pg      ^K Cut Text     ^C Cur Pos      
^X Exit         ^J Justify      ^W Where is     ^V Next Pg      ^U UnCut Text   ^T To Spell     
Last login: Fri Sep  6 17:05:15 on ttys008
zion@miniMac-9 ~ % ls
11.mp4				Parallels
2023-11-14 21-34-47.mp4		Pictures
Applications			Public
Atomic				RedTiger-Tools
Beast_Bomber			Skia-macOS-Release-x64.zip
Darkus				SocialSploit
Deanon				Windows 10 (1).pvm
Desktop				explosion.dsc
Discord-All-Tools-In-One	installer
Documents			noblack-mail
Downloads			satoshi
Library				sherlock
Lightumin			skia-m102
LittleBrother			Безіменний 2.AAE
Mine-imator			Безіменний 2.mp4
Movies				Безіменний.mp4
Music
zion@miniMac-9 ~ % ls
11.mp4				Parallels
2023-11-14 21-34-47.mp4		Pictures
Applications			Public
Atomic				RedTiger-Tools
Beast_Bomber			Skia-macOS-Release-x64.zip
Darkus				SocialSploit
Deanon				Windows 10 (1).pvm
Desktop				explosion.dsc
Discord-All-Tools-In-One	installer
Documents			noblack-mail
Downloads			satoshi
Library				sherlock
Lightumin			skia-m102
LittleBrother			Безіменний 2.AAE
Mine-imator			Безіменний 2.mp4
Movies				Безіменний.mp4
Music
zion@miniMac-9 ~ % cd Desktop
zion@miniMac-9 Desktop % ;s
zsh: command not found: s
zion@miniMac-9 Desktop % ls
Codepad.app		Computer Science	Новая папка
zion@miniMac-9 Desktop % cd 'Computer Science
quote> cd Desktop
quote> 
quote> cd Desktop
quote> 
quote> 
quote> 
zion@miniMac-9 Desktop % ls
Codepad.app		Computer Science	Новая папка
zion@miniMac-9 Desktop % cd 'Computer Science'
zion@miniMac-9 Computer Science % ls
Python
zion@miniMac-9 Computer Science % mkdir python_work
zion@miniMac-9 Computer Science % ls
Python		python_work
zion@miniMac-9 Computer Science % cd python_work
zion@miniMac-9 python_work % ls
zion@miniMac-9 python_work % touch test1.py
zion@miniMac-9 python_work % ls
test1.py
zion@miniMac-9 python_work % python3 test1.py
Hello, world!
zion@miniMac-9 python_work % cd ..            
zion@miniMac-9 Computer Science % ls
Python		python_work
zion@miniMac-9 Computer Science % cd Python
zion@miniMac-9 Python % cd stepik
zion@miniMac-9 stepik % ls
test1.py	test2.py
zion@miniMac-9 stepik % cd test2.py
cd: not a directory: test2.py
zion@miniMac-9 stepik % python3 test2.py
  File "/Users/zion/Desktop/Computer Science/Python/Stepik/test2.py", line 3
    d3 = num 5 100
             ^
SyntaxError: invalid syntax
zion@miniMac-9 stepik % python3 test2.py
  File "/Users/zion/Desktop/Computer Science/Python/Stepik/test2.py", line 3
    d3 = num 5 100
             ^
SyntaxError: invalid syntax
zion@miniMac-9 stepik % python3 test2.py
123
Traceback (most recent call last):
  File "/Users/zion/Desktop/Computer Science/Python/Stepik/test2.py", line 3, in <module>
    d3 = num % 100
         ~~~~^~~~~
TypeError: not all arguments converted during string formatting
zion@miniMac-9 stepik % python3 test2.py
123
23
zion@miniMac-9 stepik % 
  [Восстановлен 6 сент. 2024 г., 19:33:57]
Last login: Fri Sep  6 19:33:52 on console
Restored session: Fri Sep  6 19:32:58 EEST 2024
zion@miniMac-9 stepik % 
  [Восстановлен 6 сент. 2024 г., 20:13:13]
Last login: Fri Sep  6 20:13:05 on console
/bin/date: option requires an argument -- r
usage: date [-jnRu] [-I[date|hours|minutes|seconds]] [-f input_fmt]
            [-r filename|seconds] [-v[+|-]val[y|m|w|d|H|M|S]]
            [[[[mm]dd]HH]MM[[cc]yy][.SS] | new_date] [+output_fmt]
/Users/zion/.zsh_sessions/5675A469-F52F-473F-A97A-FC8D702DC2AA.session:2: command not found: Saving
zion@miniMac-9 stepik % 
  [Восстановлен 6 сент. 2024 г., 20:16:45]
Last login: Fri Sep  6 20:16:36 on console
zion@miniMac-9 stepik % 
  [Восстановлен 7 сент. 2024 г., 10:48:34]
Last login: Sat Sep  7 10:48:28 on console
zion@miniMac-9 stepik % ls
test1.py	test2.py
zion@miniMac-9 stepik % ls
test1.py	test2.py
zion@miniMac-9 stepik % cd ..
zion@miniMac-9 Python % ls
Stepik
zion@miniMac-9 Python % ls
python_work	stepik
zion@miniMac-9 Python % cd python_work
zion@miniMac-9 python_work % ls\
> ls
zsh: command not found: lsls
zion@miniMac-9 python_work % ls
test1.py
zion@miniMac-9 python_work % dir
zsh: command not found: dir
zion@miniMac-9 python_work % ls 
name.py		test1.py
zion@miniMac-9 python_work % python3 name.py
Ada Lovelace
zion@miniMac-9 python_work % python3 full_name.py
ada lovelace
zion@miniMac-9 python_work % python3 format.py   
Hello, <built-in method title of str object at 0x102525970>!
zion@miniMac-9 python_work % python3 format.py
Hello, Ada Lovalace!
zion@miniMac-9 python_work % python3 full_name.py
ada lovelace
zion@miniMac-9 python_work % ls                  
  [Восстановлен 8 сент. 2024 г., 09:25:53]
Last login: Sun Sep  8 09:25:45 on console
zion@miniMac-9 python_work % pip install flask

Collecting flask
  Downloading flask-3.0.3-py3-none-any.whl.metadata (3.2 kB)
Collecting Werkzeug>=3.0.0 (from flask)
  Downloading werkzeug-3.0.4-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from flask)
  Downloading jinja2-3.1.4-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.1.2 (from flask)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from flask)
  Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Collecting blinker>=1.6.2 (from flask)
  Downloading blinker-1.8.2-py3-none-any.whl.metadata (1.6 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->flask)
  Downloading MarkupSafe-2.1.5-cp312-cp312-macosx_10_9_universal2.whl.metadata (3.0 kB)
Downloading flask-3.0.3-py3-none-any.whl (101 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.7/101.7 kB 50.6 kB/s eta 0:00:00
Downloading blinker-1.8.2-py3-none-any.whl (9.5 kB)
Downloading click-8.1.7-py3-none-any.whl (97 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 38.1 kB/s eta 0:00:00
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.4-py3-none-any.whl (133 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.3/133.3 kB 24.7 kB/s eta 0:00:00
Downloading werkzeug-3.0.4-py3-none-any.whl (227 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 227.6/227.6 kB 25.1 kB/s eta 0:00:00
Downloading MarkupSafe-2.1.5-cp312-cp312-macosx_10_9_universal2.whl (18 kB)
Installing collected packages: MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, flask
Successfully installed Jinja2-3.1.4 MarkupSafe-2.1.5 Werkzeug-3.0.4 blinker-1.8.2 click-8.1.7 flask-3.0.3 itsdangerous-2.2.0

[notice] A new release of pip is available: 24.1.2 -> 24.2
[notice] To update, run: pip install --upgrade pip
zion@miniMac-9 python_work % 
zion@miniMac-9 python_work % ls
format_title.py	full_name.py	hello_world.py	name.py
zion@miniMac-9 python_work % cd mkdir flask
cd: string not in pwd: mkdir
zion@miniMac-9 python_work % mkdir flask
zion@miniMac-9 python_work % ls
flask		full_name.py	name.py
format_title.py	hello_world.py
zion@miniMac-9 python_work % cd flask
zion@miniMac-9 flask % touch app1.py
zion@miniMac-9 flask % ls
app1.py
zion@miniMac-9 flask % ls
app1.py
zion@miniMac-9 flask % nano app1.py
zion@miniMac-9 flask % nano app1.py

  UW PICO 5.09                                File: app1.py                                Modified  

from flask import Flask 
app = Flask(name)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if name == 'main':
    app.run(debug=True)















^G Get Help     ^O WriteOut     ^R Read File    ^Y Prev Pg      ^K Cut Text     ^C Cur Pos      
^X Exit         ^J Justify      ^W Where is     ^V Next Pg      ^U UnCut Text   ^T To Spell     






≈

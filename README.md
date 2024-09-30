# six_in_a_row
pygame 라이브러리를 사용한 6목 게임

## File tree
📦six_in_a_row
<br>
 ┣ 📂src
 <br>
 ┃ ┣ 📂img
 <br>
 ┃ ┃ ┣ 📜Blank_Go_board.png
 <br>
 ┃ ┃ ┣ 📜Go_b_no_bg.png
 <br>
 ┃ ┃ ┗ 📜Go_w_no_bg.png
 <br>
 ┃ ┣ 📂sound
 <br>
 ┃ ┃ ┣ 📜pop-39222.mp3
 <br>
 ┃ ┃ ┗ 📜yeah~.mp3
 <br>
 ┣ 📜README.md
 <br>
 ┣ 📜main.py
 <br>
 ┣ 📜position.py
 <br>
 ┗ 📜rule.py

<img width="400" alt="스크린샷 2024-08-23 오후 10 34 40" src="https://github.com/user-attachments/assets/dd875371-363c-4d08-8f54-065395e54747">
<img width="500" src="https://github.com/user-attachments/assets/b6251e04-a73d-46cc-8ace-e6a917daa785">

## Rule
1. 흑이 선공으로 돌 하나를 둔다.
2. 이후 다음 턴부터는 돌을 서로 2개씩 둔다. (첫 수를 제외한)
3. 먼저 6목을 만드는 사람이 win!

## Install pygame for Mac
```
python3 -m venv myvenv
source myvenv/bin/activate
python -m pip install --upgrade pip
pip install pygame
```

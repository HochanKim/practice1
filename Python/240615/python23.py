# pyautogui 키보드 마우스 자동화
# pip install pyautogui

import pyautogui    # pyautogui 기능 가져오기
import time         # time 기능 가져오기
import pyperclip    # pyperclip 기능 가져오기

# 화면 사이즈 출력
screen_width, screen_height = pyautogui.size()
print(f"screen_width : {screen_width}, screen_height : {screen_height}")

# 마우스 위치 출력
time.sleep(2)
print(pyautogui.position)

# 마우스 좌표 이동
pyautogui.moveTo(600, 400, 2)

# 마우스 클릭
pyautogui.click()   # 현 위치에서 클릭
pyautogui.click(button = 'right')   # 오른쪽마우스 클릭

pyautogui.doubleClick()   # 더블클릭
pyautogui.click(clicks=3, interval=2)   # 2초 인터벌, 클릭 3번
pyautogui.click(600, 400)   # 설정 좌표에서 클릭

# 마우스 드래그
pyautogui.dragTo(400, 200, 2)   # 2초뒤 설정한 좌표로 드래그

# 마우스 드래그를 이용해서 탭위치 변경
# pyautogui.moveTo(336, 45, 3)
# pyautogui.dragTo(984, 44, 3)

# 키보드 제어
pyautogui.write('# Hello, world!', interval=0.25)     # 각 문자를 0.25초 간격으로 입력

# 한글처리 방법
pyperclip.copy("# 만나서 반갑습니다.")
pyautogui.hotkey('ctrl', 'v')

# 이 예제는 메모장을 열고 "안녕하세요"라는 한글 문자열을 입력하는 방법
pyautogui.hotkey('win', 'r')    # 실행창 열기
time.sleep(1)
pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(1)

# 한글 문자열을 클립보드에 복사
pyperclip.copy('안녕하세요')

# 클립보드 내용을 붙여넣기
pyautogui.hotkey('ctrl', 'v')

# 특수 문자 입력방법
pyautogui.press('enter')    # enter
pyautogui.press('up')       # up

# 스크린샷
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')   # 스크린샷을 파일로 저장
import pyautogui
import time

def main():
    #获取鼠标位置
    input('移动至小人位置后回车')
    loca1 = pyautogui.position()
    input('移动至目标位置后回车')
    loca2 = pyautogui.position()
    #input('回车以继续')

    #计算距离
    a = loca1.x - loca2.x
    b = loca1.y - loca2.y
    len2 = a*a + b*b
    length = len2**0.5
    print( '距离为  ' and length)

    #进行长按松开操作 并回到python窗口
    pyautogui.mouseDown()
    time.sleep(length/547.5)
    pyautogui.mouseUp()
    pyautogui.hotkey('Alt','Shift','Tab')

while True:
    main()

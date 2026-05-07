import os
import sys

if getattr(sys, 'frozen', False):
    # PyInstaller onefile：配置文件应在 exe 同目录，而非 _MEI 临时解压目录
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.realpath(__file__))

import time
from pynput import mouse, keyboard
from pynput.keyboard import Key, KeyCode
import configparser
import psutil

# 全局变量
target_key = Key.shift
delay_press_ms = 10
key_pressed = False
listener = None
keyboard_controller = keyboard.Controller()
program_name = ""
exit_flag = False 

def is_program_running(program_name):
    """检查程序是否运行（不区分大小写）"""
    program_name_lower = program_name.lower()
    for proc in psutil.process_iter(['name']):
        proc_name = proc.info['name']
        if proc_name and proc_name.lower() == program_name_lower:
            return True
    return False

def read_config():
    """读取配置文件（显式指定UTF-8编码）"""
    config_dir = os.path.join(current_dir, "config.ini")
    config = configparser.ConfigParser()
    config.read(config_dir, encoding='utf-8')
    return {
        'key': config.get('config', 'key'),
        'delay_press': config.getint('config', 'delay_press'),
        'program_running': config.get('config', 'program_running')
    }

def get_key(key_name: str):
    """解析按键名称"""
    try:
        return getattr(Key, key_name)
    except AttributeError:
        if len(key_name) == 1:
            return KeyCode(char=key_name.lower())
        else:
            raise ValueError(f"无效按键名称: {key_name}")

def on_click(x, y, button, pressed):
    """鼠标点击回调"""
    global key_pressed
    if button == mouse.Button.right:
        if pressed:
            time.sleep(delay_press_ms / 1000)
            keyboard_controller.press(target_key)
            key_pressed = True
        else:
            if key_pressed:
                keyboard_controller.release(target_key)
                key_pressed = False

def init_listener():
    """初始化监听器"""
    global listener
    listener = mouse.Listener(on_click=on_click)
    listener.start()

def cleanup():
    """资源清理函数"""
    global listener, key_pressed
    if key_pressed:
        keyboard_controller.release(target_key)
        key_pressed = False
    if listener and listener.is_alive():
        listener.stop()
        listener.join()

def wait_for_program():
    """等待程序启动"""
    global exit_flag
    print(f"\n等待程序 '{program_name}' 启动... (Ctrl+C 永久退出)")
    try:
        while not exit_flag and not is_program_running(program_name):
            print(".", end="", flush=True)
            time.sleep(2)
    except KeyboardInterrupt:
        exit_flag = True
        print("\n收到退出指令")

def main_loop():
    """主监控循环"""
    global exit_flag
    while not exit_flag:
        if is_program_running(program_name):
            print("\n程序已运行，开始监听！")
            init_listener()
            
            try:
                # 保持监听状态
                while not exit_flag and is_program_running(program_name):
                    time.sleep(1)
            except KeyboardInterrupt:
                exit_flag = True
                print("\n收到退出指令")
            finally:
                cleanup()
                if not exit_flag:
                    print("检测到程序关闭，停止监听...")
            
            # 等待程序重新启动
            if not exit_flag:
                wait_for_program()

def main():
    global target_key, delay_press_ms, program_name
    args = read_config()
    program_name = args['program_running']

    try:
        target_key = get_key(args['key'])
    except ValueError as e:
        print(f"错误: {e}")
        return

    delay_press_ms = args['delay_press']

    key_type = "特殊键" if isinstance(target_key, Key) else "字符键"
    print(f"\n当前配置：")
    print(f"  模拟按键: {target_key} ({key_type})")
    print(f"  按下延迟: {delay_press_ms}ms")
    print(f"  当前监控程序: {program_name}")
    # print("持续运行模式已启用，程序关闭后会自动等待重启")
    print("-" * 40)
    
    wait_for_program()
    main_loop()

if __name__ == "__main__":
    try:
        main()
    finally:
        cleanup()
        print("\n资源已释放，脚本完全退出")
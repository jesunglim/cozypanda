import subprocess

from tkinter import *


h_list = ["box","camera"]

# 버튼 테스트
def scene_run():
    proc = subprocess.Popen(['python', 'scene.py'])

def show():
    # 임시 함수
    def domenu():
        print("OK")
        
        
    root = Tk()
    root.iconbitmap(r'icon/icon.ico')
    root.title('CozyPanda')
    root.geometry("300x600")

    def menu_bar():
        menubar = Menu(root)                                # 윈도우에 메뉴바 추가
        filemenu = Menu(menubar, tearoff=0)                 # 상위 메뉴 탭 항목 추가
        menubar.add_cascade(label="File", menu=filemenu)    # 상위 메뉴 탭 설정
        filemenu.add_command(label="New", command=domenu)   # 항목 추가
        filemenu.add_command(label="Open", command=domenu)
        filemenu.add_command(label="Save", command=domenu)
        filemenu.add_command(label="Save as...", command=domenu)
        filemenu.add_separator()                            # 분리선 추가
        filemenu.add_command(label="Exit", command=root.quit)

        editmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Copy", command=domenu)
        editmenu.add_command(label="Paste", command=domenu)
        editmenu.add_separator()
        editmenu.add_command(label="Delete", command=domenu)

        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=domenu)

        root.config(menu=menubar)             # 생성된 객체를 위에서 생성된 메뉴바에 연결    

    def main_window():
        # main window
        def t_label():
            top_label = Label(root, text="Box 1", bg="#4C4C4C")           # top layout
            top_label.pack(ipadx=10, ipady=1, fill='both')

            btn1 = Button(top_label, text = "Run", command=scene_run)
            btn1.pack()
        t_label()

        def m_label():
            mid_label = Label(root, text="Box 2", bg="gray")            # mid layout
            hierarchy_label = Label(mid_label, bg="gray") # heirachy
            hierarchy_title = Label(hierarchy_label, text="Hierarchy", bg="#B7B6B6")
            hierarchy_menu_label = Label(hierarchy_label, bg="gray")

            
            obj_frame = Label(hierarchy_label)
            scrollbar = Scrollbar(obj_frame)
            list = Listbox(obj_frame, yscrollcommand=scrollbar.set)

            def refresh():
                h_list.append("box")
                list.delete(0, END)
                for item in h_list:
                    list.insert(END, item)

            add_btn = Button(hierarchy_menu_label, text=' Add ', command=refresh)
            del_btn = Button(hierarchy_menu_label, text=' Del ', command=refresh)

            mid_label.pack(ipadx=10, ipady=10, fill='both', expand=True)
            hierarchy_label.pack(ipadx=10, ipady=10, expand=True, fill='both', side='left')
            hierarchy_title.pack(side='top', fill='x')
            hierarchy_menu_label.pack(side='top', fill='x')
            add_btn.pack(padx=5, pady=5, side='left')
            del_btn.pack(padx=5, pady=5, side='left')
            obj_frame.pack(expand=True, fill='both')
            scrollbar.pack(side='right', fill='both')
            list.pack(expand=True, fill='both')
            for item in h_list:
                list.insert(END, item)

            inspector_label = Label(mid_label, text="Inspector", bg="red") # inspector
            inspector_label.pack(ipadx=10, ipady=10, expand=True, fill='both', side='left')
        m_label()

        def b_label():
            btm_label = Label(root, text="Project", bg="#4C4C4C")          # bottom layout
            btm_label.pack(ipadx=10, ipady=10, fill='both', expand=True)
        b_label()

    menu_bar()
    main_window()

    root.mainloop()

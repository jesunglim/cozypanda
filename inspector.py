import scene

from tkinter import *
from tkinter import ttk

def show():
    def domenu():
        print("OK")

    root = Tk()
    root.iconbitmap(r'icon/icon.ico')
    root.title('CozyPanda')
    root.geometry("300x500")

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
        top_label = Label(root, text="Box 1", bg="#4C4C4C")           # top layout
        top_label.pack(ipadx=10, ipady=1, fill='both')

        # 버튼 테스트
        def scene_run():
            scene.MyApp.run()

        btn1 = Button(top_label, text = "Run", command=scene_run)
        btn1.pack()


        
        mid_label = Label(root, text="Box 2", bg="gray")            # mid layout
        mid_label.pack(ipadx=10, ipady=10, fill='both', expand=True)
        hierarchy_label = Label(mid_label, text="Hierarchy", bg="blue")
        hierarchy_label.pack(ipadx=10, ipady=10, expand=True, fill='both', side='left')
        inspector_label = Label(mid_label, text="Inspector", bg="red")
        inspector_label.pack(ipadx=10, ipady=10, expand=True, fill='both', side='left')


        btm_label = Label(root, text="Project", bg="gray")          # bottom layout
        btm_label.pack(ipadx=10, ipady=10, fill='both', expand=True)

    menu_bar()
    main_window()

    root.mainloop()

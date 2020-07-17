from tkinter import *
from tkinter import ttk
import pymysql

def stockmaintenance():
    root_stock = Tk()
    colour ="light blue"

    product_id1 = IntVar()
    product_id1.set("")
    product1 = StringVar()
    quantity1 = IntVar()
    quantity1.set("")
    cost1 = IntVar()
    cost1.set("")
    search_by = StringVar()
    search_txt = StringVar()

    def add_product_datadase():
        con = pymysql.connect(host="localhost", user="root", password="", database="grocery")
        cur = con.cursor()
        cur.execute("insert into kriyana values(%s,%s,%s,%s)",(product_id1.get(),product1.get(),quantity1.get(),cost1.get()))
        con.commit()
        fetch_data()
        clear()
        con.close()

    def fetch_data():
        con = pymysql.connect(host="localhost", user="root", password="", database="grocery")
        cur = con.cursor()
        cur.execute("select * from kriyana")
        rows=cur.fetchall()
        if(len(rows)!=0):
            main_table1.delete(*main_table1.get_children())
            for row in rows:
                main_table1.insert('',END,values=row)
            con.commit()
        con.close()
        search_txt.set("")

    def get_cursor(event):
        cursor_row=main_table1.focus()
        contents= main_table1.item(cursor_row)
        row = contents['values']
        product_id1.set(row[0])
        product1.set(row[1])
        quantity1.set(row[2])
        cost1.set(row[3])

    def delete_product_database():
        con = pymysql.connect(host="localhost", user="root", password="", database="grocery")
        cur = con.cursor()
        cur.execute("delete from kriyana where id=%s",product_id1.get())
        con.commit()
        con.close()
        fetch_data()
        clear()

    def clear():
        product_id1.set("")
        product1.set("")
        quantity1.set("")
        cost1.set("")

    def update_database():
        con = pymysql.connect(host="localhost", user="root", password="", database="grocery")
        cur = con.cursor()
        cur.execute("update kriyana set product=%s,quantity=%s,price=%s where id=%s",(product1.get(), quantity1.get(), cost1.get(),product_id1.get()))
        con.commit()
        fetch_data()
        clear()
        con.close()

    def search_data():
        con = pymysql.connect(host="localhost", user="root", password="", database="grocery")
        cur = con.cursor()
        cur.execute("select * from kriyana where id Like '%"+str(search_txt.get())+"%'")
        rows = cur.fetchall()
        if (len(rows) != 0):
            main_table1.delete(*main_table1.get_children())
            for row in rows:
                main_table1.insert('', END, values=row)
            con.commit()
        con.close()

    def billing():
        root_stock.destroy()
        import newbilling
        newbilling.newbilling()

    def handle_down(event):
        # handling right arrow key
        event.widget.tk_focusNext().focus()
        return "break"

    def handle_up(event):
        # handling right arrow key
        event.widget.tk_focusPrev().focus()
        return "break"

    #==========Window ===============
    width1 = root_stock.winfo_screenwidth()
    height1 = root_stock.winfo_screenheight()
    root_stock.geometry(f"{width1}x{height1}")

    #========= Heading ==============
    root_stock.title("Stock Maintainance")
    label1 =Label(root_stock,text="Stock Maintenance",font=("luccida 22 bold"),bg=colour ,bd=4,relief=GROOVE)
    label1.pack(side=TOP,fill=X)

    #============= main menu ============
    mainmenu1 = Menu(root_stock)
    mainmenu1.add_command(label="Billing",command=billing)
    mainmenu1.add_command(label="exit",command=exit)
    root_stock.config(menu=mainmenu1)

    #======= Creating manage_frame ===========
    manage_frame = Frame(root_stock,bd=4,relief=GROOVE,bg=colour)
    manage_frame.place(x=20,y=50,width=510,height=700)
    manage_title = Label(manage_frame,text="Manage Products",font=("luccida 22 bold"),bg=colour)
    manage_title.grid(row=0,column=0,columnspan=2,pady=15,padx=20)
    id_lb1 = Label(manage_frame,text="Product Id",font=("luccida 18 bold"),bg=colour )
    id_lb1.grid(sticky="w",row=1,column=0,pady=20,padx=10)
    id_entry = Entry(manage_frame,textvariable=product_id1,bd=4,relief=GROOVE,font=("luccida 17 bold"),width=10)
    id_entry.bind("<Down>", handle_down)
    id_entry.grid(row=1,column=1,columnspan=2,padx=30)
    product_lb1 = Label(manage_frame,text="Product",font=("luccida 18 bold"),bg=colour )
    product_lb1.grid(sticky="w",row=2,column=0,pady=20,padx=10)
    product_entry = Entry(manage_frame,textvariable=product1,bd=4,relief=GROOVE,font=("luccida 17 bold"),width=10)
    product_entry.bind("<Down>", handle_down)
    product_entry.bind("<Up>", handle_up)
    product_entry.grid(row=2,column=1,columnspan=2,padx=30)
    quantity_lb1 = Label(manage_frame,text="Quantity",font=("luccida 18 bold"),bg=colour)
    quantity_lb1.grid(sticky="w",row=3,column=0,pady=20,padx=10)
    quantity_entry = Entry(manage_frame,textvariable=quantity1,bd=4,relief=GROOVE,font=("luccida 17 bold"),width=10)
    quantity_entry.grid(row=3,column=1,columnspan=2,padx=30)
    quantity_entry.bind("<Down>", handle_down)
    quantity_entry.bind("<Up>", handle_up)
    cost_lb1 = Label(manage_frame,text="Price",font=("luccida 18 bold"),bg=colour )
    cost_lb1.grid(sticky="w",row=4,column=0,pady=20,padx=10)
    cost_entry = Entry(manage_frame,textvariable=cost1,bd=4,relief=GROOVE,font=("luccida 17 bold"),width=10)
    cost_entry.grid(row=4,column=1,columnspan=2,padx=30)
    cost_entry.bind("<Up>", handle_up)

    #=========Button frame =========
    btn_frame = Frame(manage_frame,bg=colour ,bd=4,relief=GROOVE)
    btn_frame.place(x=20,y=580,width=470,height=60)
    Button(btn_frame,text="Add",font=("luccida 12"),width=10,command=add_product_datadase).grid(row=0,column=0,padx=8,pady=10)
    Button(btn_frame,text="Delete",font=("luccida 12"),width=10,command=delete_product_database).grid(row=0,column=1,padx=8,pady=10)
    Button(btn_frame,text="Update",font=("luccida 12"),width=10,command=update_database).grid(row=0,column=2,padx=8,pady=10)
    Button(btn_frame,text="Clear",font=("luccida 12"),width=10,command=clear).grid(row=0,column=3,pady=10,padx=8)

    #======== Creating detail frame ============
    detail_frame = Frame(root_stock,bd=4,relief=GROOVE,bg=colour)
    detail_frame.place(x=550,y=50,width=920,height=700)

    search_label1 = Label(detail_frame,text="Search by :",font=("luccida 17 bold"),bg=colour)
    search_label1.grid(row=0,column=0,columnspan=2,pady=5,padx=10)
    search_entry1 = ttk.Combobox(detail_frame,textvariable=search_by,font=("luccida 14 bold"),width=10,state='readonly')
    # search_entry1['values']=("id")
    search_entry1.set("Product Id")
    search_entry1.grid(row=0,column=2,columnspan=2,padx=10)
    productID_entry1 = Entry(detail_frame,textvariable=search_txt,font=("luccida 14 bold"),relief=GROOVE,bd=4,width=12)
    productID_entry1.grid(row=0,column=4,columnspan=2)
    search_btn = Button(detail_frame,text="Search",font=("luccida 12"),bd=4,relief=GROOVE,command=search_data)
    search_btn.grid(row=0,column=6,columnspan=2,padx=15,pady=10)
    show_all_btn = Button(detail_frame,text="Show all",font=("luccida 12"),bd=4,relief=GROOVE,command=fetch_data)
    show_all_btn.grid(row=0,column=8,columnspan=2,padx=15,pady=10)

    table_frame1 = Frame(detail_frame,bd=4,relief=GROOVE,bg="white")
    table_frame1.place(x=20,y=60,width=850,height=600)
    scroll_y= Scrollbar(table_frame1)
    main_table1 = ttk.Treeview(table_frame1,columns=("id","product","quantity","cost"),yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_y.config(command=main_table1.yview)
    main_table1.heading("id",text="ID")
    main_table1.heading("product",text="Product")
    main_table1.heading("quantity",text="Quantity")
    main_table1.heading("cost",text="Cost")
    main_table1['show'] = 'headings'
    main_table1.column("id",width=150)
    main_table1.column("product",width=320)
    main_table1.column("quantity",width=150)
    main_table1.column("cost",width=160)
    main_table1.pack(fill=BOTH,expand=1)
    main_table1.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()

    root_stock.bind("<Escape>",exit)
    root_stock.mainloop()

stockmaintenance()
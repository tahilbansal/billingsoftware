from tkinter import *
import datetime
from tkinter import ttk
import pymysql
import os

def newbilling():

    root =Tk()

    colour ="light blue"

    product_id = StringVar()
    product_id.set("")
    product = StringVar()
    product.set("")
    quantity = DoubleVar()
    quantity.set(1)
    cost = IntVar()


    # =========== Add product in main table ===========
    def add_product(event):
        con = pymysql.connect(host="localhost", user="root", password="", database="grocery")
        cur = con.cursor()
        cur.execute(f"select id,product,price from kriyana where id = {product_id.get()}")
        rows = cur.fetchall()
        for row in rows:
            value = [row[0],row[1],quantity.get(),row[2],quantity.get()*row[2]]
            main_table.insert('',END,values=value)
        con.commit()
        con.close()
        product_id.set("")
        if(product_id !=1):
            productID_entry.focus()
        quantity.set(1)


    # ======== Deleting a selected row if needed=============
    def delete_row():
        selected_items = main_table.selection()
        for selected_item in selected_items:
            main_table.delete(selected_item)

    # ===========  Current date and time ==============
    now = datetime.datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%H:%M")

    bill_no = 0
    # ====== Total the cost of products in mainn table ===========
    def bill(event):
        nonlocal bill_no
        txtarea.delete('1.0', END)
        txtarea.insert(END, f"\n   Lal chand Anil kumar               Bill no.={bill_no}   \n")
        txtarea.insert(END, f"   Mishri Bazaar patiala               {current_date}\n")
        txtarea.insert(END, f"   94178973222                         {current_time}\n\n")
        txtarea.insert(END, "=" * 54 + "\n")
        txtarea.insert(END, "       Products\t\t    QTY\t\t  Price\t\tAmt\n")
        txtarea.insert(END, "=" * 54 + "\n")
        total = 0.0;
        for child in main_table.get_children():
            prod = main_table.item(child)["values"][1]
            quant = float(main_table.item(child)["values"][2])
            item_cost = int(main_table.item(child)["values"][3])
            total += quant*item_cost
            txtarea.insert(END,f"      {prod}\t\t   {quant}\t\t   {item_cost}\t\t{quant*item_cost}\n")
        txtarea.insert(END,"-"*54)
        txtarea.insert(END,f"\n\t\t\t\tTotal Bill : {total}\n")
        total_text = Label(total_frame, text=f"{total}",font=("luccida 22 bold"),bg="white",width=7)
        total_text.grid(row=0, column=2, columnspan=2, pady=5, padx=10)
        txtarea.insert(END, "-" * 54)
        txtarea.insert(END,"\n\n\t   -- Thank you for shopping --")
        bill_no +=1

    # ================ print bill ==============
    def print_bill(event):
        nonlocal bill_no
        bill_data = txtarea.get('1.0',END)
        f1 = open(f"Bill","w")
        f1.write(bill_data)
        f1.close()
        os.startfile("C:/Users/BHARAT/PycharmProjects/GUI/Bill.txt","print")

    def stock():
        root.destroy()
        import StockMaintenance
        StockMaintenance.stockmaintenance()

    def clear(event):
        main_table.delete(*main_table.get_children())
        txtarea.delete('1.0', END)

    def two_discount():
        txtarea.delete('1.0', END)
        txtarea.insert(END, "\tLal chand Anil kumar\n")
        txtarea.insert(END, "\tMishri Bazaar patiala\n")
        txtarea.insert(END, "\t94178973222\n\n")
        txtarea.insert(END, "=" * 54 + "\n")
        txtarea.insert(END, "       Products\t\t    QTY\t\t  Price\t\tAmt\n")
        txtarea.insert(END, "=" * 54 + "\n")
        total = 0.0;
        for child in main_table.get_children():
            prod = main_table.item(child)["values"][1]
            quant = float(main_table.item(child)["values"][2])
            item_cost = 0.98*int(main_table.item(child)["values"][3])
            total += quant * item_cost
            txtarea.insert(END, f"      {prod}\t\t   {quant}\t\t   {item_cost}\t\t{quant * item_cost}\n")
        txtarea.insert(END, "-" * 54)
        txtarea.insert(END, f"\n\t\t\t\tTotal Bill : {total}\n")
        total_text = Label(total_frame, text=f"{total}", font=("luccida 22 bold"), bg="white", width=7)
        total_text.grid(row=0, column=2, columnspan=2, pady=5, padx=10)
        txtarea.insert(END, "-" * 54)
        txtarea.insert(END, "\n\n\t   -- Thank you for shopping --")


    def handle_right(event):
        # handling right arrow key
        quantity.set("")
        quantity_entry.focus()
        return "break"

    def handle_left(event):
        # handling right arrow key
        quantity.set(1)
        productID_entry.focus()
        return "break"

    def SCAN():
        from imutils.video import VideoStream
        from pyzbar import pyzbar
        import argparse
        import datetime
        from datetime import datetime
        import imutils
        import time
        import cv2
        import winsound

        frequency = 2000  # Set Frequency To 2500 Hertz
        duration = 800  # Set Duration To 1000 ms == 1 second

        ap = argparse.ArgumentParser()
        ap.add_argument("-o", "--output", type=str, default="barcodesData.csv",
                        help="path to output CSV file ")
        args = vars(ap.parse_args())

        print("Starting webcam")

        vs = VideoStream(src=0).start()
        time.sleep(2.0)
        csvWrite = open(args["output"], "w")
        found = set()
        while True:
            frameData = vs.read()
            frameData = imutils.resize(frameData, width=600)
            barcodes = pyzbar.decode(frameData)
            for barcode in barcodes:
                (x, y, width, height) = barcode.rect
                cv2.rectangle(frameData, (x, y), (x + width, y + height), (0, 0, 255), 2)
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                textData = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(frameData, textData, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                if barcodeData not in found:
                    csvWrite.write("{},{}\n".format(datetime.today().strftime('%Y-%m-%d'),
                                                    barcodeData))
                    csvWrite.flush()
                    found.add(barcodeData)
                    winsound.Beep(frequency, duration)
            cv2.imshow("Barcode Scanner", frameData)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("e"):
                break

        # close the output CSV file do a bit of cleanup
        print("\nWait while we calculate cost...")
        csvWrite.close()
        cv2.destroyAllWindows()
        vs.stop()

        time.sleep(1.0)
        import numpy as np
        import pandas as pd
        from datetime import datetime
        import re
        import time

        data = pd.read_csv('barcodesData.csv', names=['Date', 'item'])
        col1 = data['Date']
        col2 = data['item'].values
        regex = re.compile(r'(\d+|\s+)')
        total = 0

        with open('saleid.txt', 'r') as f1:

            saleid = f1.read()
            saleID = int(saleid)


            for x in col2:
                # row = str(col1[1]) + '\t \t' + str(regex.split(x)[0]) + '\t \t' + str(regex.split(x)[1])
                con = pymysql.connect(host="localhost", user="root", password="", database="grocery")
                cur = con.cursor()
                bar = x%1000
                cur.execute(f"select id,product,price from kriyana where id = {bar}")
                rows = cur.fetchall()
                for row in rows:
                    value = [row[0], row[1], quantity.get(), row[2], quantity.get() * row[2]]
                    main_table.insert('', END, values=value)
                con.commit()
                con.close()
                product_id.set("")
                if (product_id != 1):
                    productID_entry.focus()
                quantity.set(1)

                # print(row)
            saleID = saleID + 1

        with open('saleid.txt', 'w') as fw:
            fw.write(str(saleID))

        # fw.close()
        # f1.close()

        # f.close()


    # =========== setting GUI window ===========
    root.title("Shopping bill")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f"{width}x{height}")

    # ================= Heading =================
    label =Label(root,text="Billing system",font=("luccida 22 bold"),bg=colour ,bd=4,relief=GROOVE)
    label.pack(side=TOP,fill=X)

    #========= Main Menu ============
    mainmenu = Menu(root)
    mainmenu.add_command(label="Stock maintenance",command=stock)
    mainmenu.add_command(label="exit",command=exit)
    root.config(menu=mainmenu)

    #=================  Creating main frame ========================
    main_frame = Frame(root,bd=4,relief=GROOVE,bg=colour)
    main_frame.place(x=20,y=60,width=850,height=720)

    #============== creating search layer inside main frame ==================
    search_label = Label(main_frame,text="Search by :",font=("luccida 17 bold"),bg=colour)
    search_label.grid(row=0,column=0,columnspan=2,pady=5,padx=10)
    # search_entry = ttk.Combobox(main_frame,font=("luccida 14 bold"),width=10,state='readonly')
    # search_entry['values']=("Product Id")
    # search_entry.set("Product Id")
    # search_entry.grid(row=0,column=2,columnspan=2,padx=10)
    # productID_label = Label(main_frame,text="Product Id :",font=("luccida 17 bold"),bg="light blue")
    # productID_label.grid(row=0,column=4,columnspan=2,pady=5,padx=8)
    productID_entry = Entry(main_frame,textvariable=product_id,font=("luccida 14 bold"),relief=GROOVE,bd=4,width=12)
    productID_entry.grid(row=0,column=2,columnspan=1,padx=10)
    productID_entry.bind("<Right>", handle_right)
    quantity_entry = Entry(main_frame, textvariable=quantity, font=("luccida 14 bold"), relief=GROOVE, bd=4,width=12)
    quantity_entry.grid(row=0, column=3, columnspan=2, padx=10)
    quantity_entry.bind("<Left>",handle_left)
    add_button = Button(main_frame,text="ADD",font=("luccida 10"),relief=GROOVE,bd=4,width=8,command=add_product)
    add_button.grid(row=0,column=6,columnspan=2,padx=15)
    bill_button = Button(main_frame,text="SCAN",font=("luccida 10"),relief=GROOVE,bd=4,width=8,command=SCAN)
    bill_button.grid(row=0,column=8,columnspan=2,padx=15)

    #========== creating table frame inside main frame ============
    table_frame = Frame(main_frame,bd=4,relief=GROOVE,bg="white")
    table_frame.place(x=15,y=50,width=810,height=600)
    scroll_y= Scrollbar(table_frame)
    main_table = ttk.Treeview(table_frame,columns=("id","product","quantity","cost","amt"),yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_y.config(command=main_table.yview)
    main_table.heading("id",text="ID")
    main_table.heading("product",text="Product")
    main_table.heading("quantity",text="Quantity")
    main_table.heading("cost",text="Cost")
    main_table.heading("amt",text="Amount")
    main_table['show'] = 'headings'
    main_table.column("id",width=120)
    main_table.column("product",width=300)
    main_table.column("quantity",width=120)
    main_table.column("cost",width=120)
    main_table.column("amt",width=120)
    main_table.pack(fill=BOTH,expand=1)

    total_frame = Frame(main_frame,bg=colour)
    total_frame.place(x=15,y=655,width=810,height=55)
    total_label = Label(total_frame,text="\t\t\t\t Total Bill :",font=("luccida 17 bold"),bg=colour)
    total_label.grid(row=0,column=0,columnspan=2,pady=5,padx=10)

    delete_button = Button(main_frame,text="DELETE",font=("luccida 10"),relief=GROOVE,bd=4,width=8,command=delete_row)
    delete_button.grid(row=0,column=10,columnspan=2,padx=15)


    #============ Creating bill area =============
    bill_frame= Frame(root,bd=4,relief=GROOVE,bg="white")
    bill_frame.place(x=900,y=60,width=450,height=720)
    bill_title= Label(bill_frame,text="BILL AREA",font=("luccida 15"),relief=GROOVE,bd=4)
    bill_title.pack(fill=X)
    txtarea = Text(bill_frame)
    txtarea.pack(fill=BOTH,expand=1)

    #==========Discount offers==============
    discount_frame = Frame(root,bd=4,relief=GROOVE,bg="white")
    discount_frame.place(x=1370,y=60,width=140,height=720)
    two_button = Button(discount_frame,text="2% Discount",font=("luccida 12"),relief=GROOVE,bd=4,command=two_discount)
    two_button.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

    root.bind("<Return>",add_product)
    root.bind("<Shift_R>",bill)
    root.bind("<p>",print_bill)
    root.bind("<Alt_R>",clear)
    root.bind("<Escape>",exit)
    root.bind("",productID_entry.focus())
    root.mainloop()

newbilling()
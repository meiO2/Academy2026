#Grace L.R Pangaribuan (23502410001), Gloriana Monica (23502410013)

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime

#CONNECT TO DATABASE
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="",
    database="ta_dbs"
)

cursor = db.cursor()

class Sistem(tk.Tk): 

# INTI [v]

    def __init__(self): 
        super().__init__()

        self.title("Sistem Operasional Toko Boga Jaya")
    

        frame = tk.Frame(self, width=800, height=600, bg="#ADDFFF")
        self.frames = "frame"

        heading = tk.Label(frame, text="Sistem Operasi Toko Boga Jaya", font=('Helvetica', 20,'bold'), bg="#ADDFFF")
        heading.pack(pady=20)

        description = tk.Label(frame, text="Silahkan pilih fitur yang ingin digunakan:", font=('Helvetica', 10), bg="#ADDFFF")
        description.pack(padx=20, anchor="w")

        buttonframe = tk.Frame(frame, bg="#ADDFFF", pady=20)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)

        btn1 = tk.Button(buttonframe, text="Penjualan", font=('Helvetica', 15), width=20, relief="groove", bg="white", command= lambda: self.Penjualan(frame))
        btn1.grid(padx=5, pady=5, row=0, column=0, ipadx=30, ipady=30)

        btn2 = tk.Button(buttonframe, text="Stok Barang", font=('Helvetica', 15), width=20, relief="groove", bg="white", command= lambda: self.StokBarang(frame))
        btn2.grid(padx=5,pady=5, row=0, column=1, ipadx=30, ipady=30)

        btn3 = tk.Button(buttonframe, text="Pengeluaran", font=('Helvetica', 15), width=20, relief="groove", bg="white", command= lambda: self.Pengeluaran(frame))
        btn3.grid(padx=5,pady=5, row=0, column=2, ipadx=30, ipady=30)

        btn4 = tk.Button(buttonframe, text="Pengiriman", font=('Helvetica', 15), width=20, relief="groove", bg="white", command= lambda: self.Pengiriman(frame))
        btn4.grid(padx=5,pady=5, row=1, column=0, ipadx=30, ipady=30)

        btn5 = tk.Button(buttonframe, text="Pemasok", font=('Helvetica', 15), width=20, relief="groove", bg="white", command= lambda: self.Pemasok(frame))
        btn5.grid(padx=5,pady=5, row=1, column=1, ipadx=30, ipady=30)

        btn6 = tk.Button(buttonframe, text="Pegawai", font=('Helvetica', 15), width=20, relief="groove", bg="white", command= lambda: self.Pegawai(frame))
        btn6.grid(padx=5,pady=5, row=1, column=2, ipadx=30, ipady=30)

        btn7 = tk.Button(buttonframe, text="Pelanggan \n Grosir", font=('Helvetica', 15), width=20, relief="groove", bg="white", command= lambda: self.pelanggan_grosir(frame))
        btn7.grid(padx=5,pady=5, row=2, column=1, ipadx=30, ipady=18)

        buttonframe.pack(padx=10, pady=10)
        frame.pack_propagate(False)
        frame.pack()

        self.mainloop()

    def clear(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def generate_auto_id(self, entry_widget, table_name, column_name, prefix):
        try:
            query = f"SELECT {column_name} FROM {table_name} ORDER BY {column_name} DESC LIMIT 1"
            cursor.execute(query)
            result = cursor.fetchone()
            new_id_num = int(result[0][len(prefix):]) + 1 if result else 1
            new_id = f"{prefix}{new_id_num:03d}"
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, new_id)
        except Exception as e:
            messagebox.showerror("Error Auto ID", str(e))

#PENJUALAN [v]

    def Penjualan(self, frame):
        self.clear(frame)
        
        headingframe = tk.Frame(frame, bg="#ADDFFF" )
        heading = tk.Label(headingframe, text="Penjualan", font=('Helvetica', 20, 'bold'), bg="#ADDFFF")
        heading.grid(row=0, column=0, pady=10, padx=40, sticky="w")

        backbutton=tk.Button(headingframe, text="Kembali", bg="white", font=('Helvetica', 10), command= lambda: [self.destroy(), Sistem()])
        backbutton.grid(row=0, column=1, pady=10, padx=480, sticky="e")
        headingframe.pack()

        buttonframe = tk.LabelFrame(frame, text="Manage", bg="white")

        btn1 = tk.Button(buttonframe, text="Update", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=self.update_penjualan)
        btn1.grid(padx=25, pady=5, row=0, column=0)

        btn2 = tk.Button(buttonframe, text="Delete", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=self.delete_penjualan)
        btn2.grid(padx=25,pady=5, row=0, column=1)

        btn3 = tk.Button(buttonframe, text="Create", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=self.Create_Penjualan)
        btn3.grid(padx=25,pady=5, row=0, column=2)

        btn4 = tk.Button(buttonframe, text="Find", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=lambda: self.Find_Penjualan(self.ID_Penjualan_entry.get()))
        btn4.grid(padx=25,pady=5, row=0, column=3)

        buttonframe.pack()

        entryframe=tk.Frame(frame, bg="#ADDFFF", padx=40, pady=5)
        entryframe.pack(fill="x")

        entry1label = tk.Label(entryframe, text="ID_PENJUALAN", font=('Helvetica', 10), bg="#ADDFFF")
        entry1label.grid(row=0, column=0, sticky="w")
        self.ID_Penjualan_entry = tk.Entry(entryframe, width=70)
        self.ID_Penjualan_entry.grid(pady=5, row=0, column=1, sticky="w")

        btnID = tk.Button(entryframe, text="Auto ID", font=('Helvetica', 10), width=12, relief="groove", bg="white",
                  command=lambda: self.generate_auto_id(self.ID_Penjualan_entry, "PENJUALAN", "ID_PENJUALAN", "PN"))
        btnID.grid(row=0, column=1, sticky="e", padx=7)

        entry2label = tk.Label(entryframe, text="Jumlah_Terjual", font=('Helvetica', 10), bg="#ADDFFF")
        entry2label.grid(row=1, column=0, sticky="w")
        self.jumlah_terjual_entry= tk.Entry(entryframe, width=92)
        self.jumlah_terjual_entry.grid(pady=5, row=1, column=1, sticky="ew")

        entry4label = tk.Label(entryframe, text="ID_PELANGGAN_GROSIR", font=('Helvetica', 10), bg="#ADDFFF")
        entry4label.grid(row=3, column=0, sticky="w")
        self.id_pelanggan_grosir_entry = tk.Entry(entryframe, width=85)
        self.id_pelanggan_grosir_entry.grid(pady=5, row=3, column=1, sticky="ew")

        entry5label = tk.Label(entryframe, text="ID_BARANG", font=('Helvetica', 10), bg="#ADDFFF")
        entry5label.grid(row=4, column=0, sticky="w")
        self.ID_Barang_entry = tk.Entry(entryframe, width=85)
        self.ID_Barang_entry.grid(pady=5, row=4, column=1, sticky="we")

        entry6label = tk.Label(entryframe, text="Subtotal", font=('Helvetica', 10), bg="#ADDFFF")
        entry6label.grid(row=5, column=0, sticky="w")
        self.subtotal_entry = tk.Entry(entryframe, width=70)
        self.subtotal_entry.grid(pady=5, row=5, column=1, sticky="we") 

        btnsubtotal = tk.Button(entryframe, text="Total", font=('Helvetica', 10), width=12, relief="groove", bg="white", command=self.klik)
        btnsubtotal.grid(row=6, column=1, sticky="e", padx=7)

        entry7label = tk.Label(entryframe, text="Total_Penjualan", font=('Helvetica', 10), bg="#ADDFFF")
        entry7label.grid(row=6, column=0, sticky="w")
        self.total_penjualan_entry = tk.Entry(entryframe, width=70)
        self.total_penjualan_entry.grid(pady=5, row=6, column=1, sticky="w")

        self.viewbarang = ttk.Treeview(frame)
        self.viewbarang["columns"] = ("ID_PENJUALAN", "ID_PELANGGAN_GROSIR", "Total_Penjualan", "Tanggal","ID_BARANG & SubTotal", "Jumlah_Terjual")

        self.viewbarang.column("#0", width=0, stretch=tk.NO)
        for col in self.viewbarang["columns"]:
            if col == "ID_BARANG & SubTotal":
                self.viewbarang.column(col, anchor="w", width=400)
                self.viewbarang.heading(col, text=col)
            else:
                self.viewbarang.column(col, anchor="w", width=150)
                self.viewbarang.heading(col, text=col)             

        scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.viewbarang.yview)
        scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=self.viewbarang.xview)
        self.viewbarang.configure(yscroll=scrollbar_y.set, xscroll=scrollbar_x.set)

        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.viewbarang.pack(expand=True, fill=tk.BOTH)

        self.Find_Penjualan()

        self.viewbarang.bind("<<TreeviewSelect>>", self.pilih_penjualan)

    def Create_Penjualan(self):

        cursor.execute("SELECT ID_PENJUALAN FROM PENJUALAN ORDER BY ID_PENJUALAN DESC LIMIT 1")
        result = cursor.fetchone()
        new_id_num = int(result[0][2:]) + 1 if result else 1
        new_id = f"PN{new_id_num:03d}"
        tanggal_sekarang = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        try:
            id_pelanggan = self.id_pelanggan_grosir_entry.get()
            if id_pelanggan == "":
                id_pelanggan = None
            cursor.execute("""
                INSERT INTO penjualan (ID_PENJUALAN, Total_Penjualan, Tanggal, ID_PELANGGAN_GROSIR)
                VALUES (%s, %s, %s, %s)
            """, (new_id, self.total_penjualan_entry.get(), tanggal_sekarang, id_pelanggan))

            barang_list = [b.strip() for b in self.ID_Barang_entry.get().split(",")]
            jumlah_list = [j.strip() for j in self.jumlah_terjual_entry.get().split(",")]
            subtotal_list = [s.strip() for s in self.subtotal_entry.get().split(",")]

            DETAIL_PENJUALAN = []
            for barang, jumlah, subtotal in zip(barang_list, jumlah_list, subtotal_list):
                DETAIL_PENJUALAN.append({
                    "ID_BARANG": barang,
                    "Jumlah_Terjual": jumlah,
                    "Subtotal": subtotal
                })

            for detail in DETAIL_PENJUALAN:
                cursor.execute("""
                    INSERT INTO detail_penjualan (ID_BARANG, ID_PENJUALAN, Jumlah_Terjual, Subtotal)
                    VALUES (%s, %s, %s, %s)
                """, ( detail["ID_BARANG"],self.ID_Penjualan_entry.get(), detail["Jumlah_Terjual"], detail["Subtotal"]
                ))

            db.commit()

            self.ID_Penjualan_entry.delete(0, tk.END)
            self.ID_Penjualan_entry.insert(0, new_id)
            for entry in [self.jumlah_terjual_entry, self.ID_Barang_entry, self.subtotal_entry, self.total_penjualan_entry]:
                entry.delete(0, tk.END)

            self.Find_Penjualan()

            messagebox.showinfo("Berhasil", "Data Penjualan berhasil dibuat")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def klik(self):
        total = 0
        subtotal_list =[]
        barang_list = [b.strip() for b in self.ID_Barang_entry.get().split(",")]
        jumlah_list = [j.strip() for j in self.jumlah_terjual_entry.get().split(",")]

        DETAIL_PENJUALAN = []

        for barang, jumlah in zip(barang_list, jumlah_list):
            DETAIL_PENJUALAN.append({
                "ID_BARANG": barang,
                "Jumlah_Terjual": int(jumlah),
            })

        for detail in DETAIL_PENJUALAN:
            cursor.execute("SELECT Harga_Jual FROM barang WHERE ID_BARANG = %s", (detail["ID_BARANG"],))
            result = cursor.fetchone()
            if result:
                harga = int(result[0])
                subtotal = float(harga * detail["Jumlah_Terjual"])
                subtotal_list.append(f"{subtotal:.2f}")
                total += subtotal
            else:
                messagebox.showerror("Error", "ID Barang tidak ditemukan")
            
            try:
                jumlah = int(jumlah)
            except ValueError:
                messagebox.showerror("Error", "Jumlah terjual harus berupa angka.")
                return
            
            self.subtotal_entry.delete(0, tk.END)
            self.subtotal_entry.insert(0, ",".join(tuple(subtotal_list)))

            self.total_penjualan_entry.delete(0, tk.END)
            self.total_penjualan_entry.insert(0, str(total))

    def Find_Penjualan(self, id_penjualan=None):
        for row in self.viewbarang.get_children():
            self.viewbarang.delete(row)

        try:
            if id_penjualan:
                cursor.execute("""
                    SELECT p.ID_PENJUALAN, p.ID_PELANGGAN_GROSIR, p.Total_Penjualan, p.Tanggal,
                           GROUP_CONCAT(CONCAT(d.ID_BARANG, ' (', d.Subtotal, ')') SEPARATOR ', ') AS Barang,
                           GROUP_CONCAT(d.Jumlah_Terjual SEPARATOR ', ') AS Jumlah_Terjual
                    FROM penjualan p
                    JOIN detail_penjualan d ON p.ID_PENJUALAN = d.ID_PENJUALAN
                    WHERE p.ID_PENJUALAN = %s
                    GROUP BY p.ID_PENJUALAN
                """, (id_penjualan,))
            else:
                cursor.execute("""
                    SELECT p.ID_PENJUALAN, p.ID_PELANGGAN_GROSIR, p.Total_Penjualan, p.Tanggal,
                           GROUP_CONCAT(CONCAT(d.ID_BARANG, ' (', d.Subtotal, ')') SEPARATOR ', ') AS Barang,
                           GROUP_CONCAT(d.Jumlah_Terjual SEPARATOR ', ') AS Jumlah_Terjual
                    FROM penjualan p
                    JOIN detail_penjualan d ON p.ID_PENJUALAN = d.ID_PENJUALAN
                    GROUP BY p.ID_PENJUALAN;
                """)
            for result in cursor.fetchall():
                self.viewbarang.insert("", tk.END, values=result)
        except Exception as e:
            messagebox.showerror("ERROR", str(e))

    def update_penjualan(self):
        try:
            cursor.execute("""
                UPDATE penjualan SET Total_Penjualan = %s, ID_PELANGGAN_GROSIR = %s WHERE ID_PENJUALAN = %s
            """, (self.total_penjualan_entry.get(), self.id_pelanggan_grosir_entry.get(), self.ID_Penjualan_entry.get()))

            cursor.execute("DELETE FROM detail_penjualan WHERE ID_PENJUALAN = %s", (self.ID_Penjualan_entry.get(),))

            barang_list = [b.strip() for b in self.ID_Barang_entry.get().split(",")]
            jumlah_list = [j.strip() for j in self.jumlah_terjual_entry.get().split(",")]
            subtotal_list = [s.strip() for s in self.subtotal_entry.get().split(",")]

            DETAIL_PENJUALAN = []

            for barang, jumlah, subtotal in zip(barang_list, jumlah_list, subtotal_list):
                DETAIL_PENJUALAN.append({
                    "ID_BARANG": barang,
                    "Jumlah_Terjual": jumlah,
                    "Subtotal": subtotal
                })

            for detail in DETAIL_PENJUALAN:
                cursor.execute("""
                    INSERT INTO detail_penjualan (ID_BARANG, ID_PENJUALAN, Jumlah_Terjual, Subtotal)
                    VALUES (%s, %s, %s, %s)
                    """, (detail["ID_BARANG"], self.ID_Penjualan_entry.get(), detail["Jumlah_Terjual"], detail["Subtotal"]))

            db.commit()
            messagebox.showinfo("Berhasil", "Data penjualan berhasil diupdate.")
        except Exception as e:
            db.rollback()
            messagebox.showerror("ERROR", str(e))
        
        self.Find_Penjualan()

    def delete_penjualan(self):
        id_penjualan = self.ID_Penjualan_entry.get()

        if not id_penjualan:
            messagebox.showerror("ERROR", "ID Penjualan harus diiisi")
            return
        try:
            cursor.execute("DELETE FROM detail_penjualan WHERE ID_PENJUALAN = %s", (id_penjualan,))

            cursor.execute("DELETE FROM pesanan WHERE ID_PENJUALAN = %s", (id_penjualan,))

            cursor.execute("DELETE FROM penjualan WHERE ID_PENJUALAN = %s", (id_penjualan,))
            db.commit()

            messagebox.showinfo("SUKSES", "Data penjualan berhasil dihapus")

            self.ID_Penjualan_entry.delete(0,tk.END)
            self.jumlah_terjual_entry.delete(0,tk.END)
            self.subtotal_entry.delete(0,tk.END)
            self.total_penjualan_entry.delete(0,tk.END)
            self.id_pelanggan_grosir_entry.delete(0,tk.END)
            self.ID_Barang_entry.delete(0,tk.END) 

            self.Find_Penjualan()
        except Exception as e:
         messagebox.showerror("Error", f"Gagal menghapus data: {str(e)}")

    def pilih_penjualan(self,event):
        pilihID = ''
        pilih = self.viewbarang.selection()[0]

        if pilih:
            pilihID = str(self.viewbarang.item(pilih)['values'][0])
            
            cursor.execute("""
                    SELECT p.ID_PENJUALAN, GROUP_CONCAT(d.Jumlah_Terjual SEPARATOR ', ') AS Jumlah_Terjual, p.ID_PELANGGAN_GROSIR,
                           GROUP_CONCAT(d.ID_BARANG SEPARATOR ', ') AS Barang,
                           GROUP_CONCAT(d.Subtotal SEPARATOR ', ') AS Subtotal,
                           p.Total_Penjualan 
                    FROM penjualan p
                    JOIN detail_penjualan d ON p.ID_PENJUALAN = d.ID_PENJUALAN
                    WHERE p.ID_PENJUALAN = %s
                    GROUP BY p.ID_PENJUALAN
                """, (pilihID,))
            
            dataentry = []
            hasil = cursor.fetchall()
            for x in hasil:
                for y in x:
                    dataentry.append(y)

            entry_ = [
                self.ID_Penjualan_entry,
                self.jumlah_terjual_entry,
                self.id_pelanggan_grosir_entry,
                self.ID_Barang_entry,
                self.subtotal_entry,
                self.total_penjualan_entry
            ]

            for entry, dataentry in zip(entry_, dataentry):
                if dataentry is None:
                    continue
                entry.delete(0, tk.END)
                entry.insert(0, dataentry)  

#STOKBARANG [v]
    def StokBarang(self, frame):
        self.clear(frame)

        headingframe = tk.Frame(frame, bg="#ADDFFF" )
        heading = tk.Label(headingframe, text="Stok Barang", font=('Helvetica', 20, 'bold'), bg="#ADDFFF")
        heading.grid(row=0, column=0, pady=10, padx=40, sticky="w")

        backbutton=tk.Button(headingframe, text="Kembali", bg="white", font=('Helvetica', 10), command= lambda: [self.destroy(), Sistem()])
        backbutton.grid(row=0, column=1, pady=10, padx=450, sticky="e")
        headingframe.pack()

        buttonframe = tk.LabelFrame(frame, text="Manage", bg="white")

        btn1 = tk.Button(buttonframe, text="Update", font=('Helvetica', 10), width=15, relief="groove", bg="white", command= self.update_barang)
        btn1.grid(padx=25, pady=5, row=0, column=0)

        btn2 = tk.Button(buttonframe, text="Delete", font=('Helvetica', 10), width=15, relief="groove", bg="white", command= self.delete_Barang)
        btn2.grid(padx=25,pady=5, row=0, column=1)

        btn3 = tk.Button(buttonframe, text="Create", font=('Helvetica', 10), width=15, relief="groove", bg="white", command= self.Create_Barang)
        btn3.grid(padx=25,pady=5, row=0, column=2)

        btn4 = tk.Button(buttonframe, text="Find", font=('Helvetica', 10), width=15, relief="groove", bg="white", command= lambda: self.Find_Barang(self.entry1.get()))
        btn4.grid(padx=25,pady=5, row=0, column=3)

        buttonframe.pack()

        entryframe=tk.Frame(frame, bg="#ADDFFF", padx=40, pady=5)

        entry1label = tk.Label(entryframe, text="ID Barang", font=('Helvetica', 10), bg="#ADDFFF")
        entry1label.grid(row=0, column=0, sticky="w")
        self.entry1 = tk.Entry(entryframe, width=80)
        self.entry1.grid(pady=5, row=0, column=1, sticky="w")

        btnID = tk.Button(entryframe, text="Auto ID", font=('Helvetica', 10), width=12, relief="groove", bg="white", 
                          command= lambda:self.generate_auto_id(self.entry1, "barang", "ID_BARANG", "B0"))
        btnID.grid(row=0, column=1, sticky="e", padx=10)

        entry2label = tk.Label(entryframe, text="Nama Barang", font=('Helvetica', 10), bg="#ADDFFF")
        entry2label.grid(row=1, column=0, sticky="w")
        self.entry2 = tk.Entry(entryframe, width=103)
        self.entry2.grid(pady=5, row=1, column=1, sticky="ew")

        entry3label = tk.Label(entryframe, text="Jumlah Barang", font=('Helvetica', 10), bg="#ADDFFF")
        entry3label.grid(row=2, column=0, sticky="w")
        self.entry3 = tk.Entry(entryframe, width=85)
        self.entry3.grid(pady=5, row=2, column=1, sticky="ew")

        entry4label = tk.Label(entryframe, text="Harga Jual", font=('Helvetica', 10), bg="#ADDFFF")
        entry4label.grid(row=3, column=0, sticky="w")
        self.entry4 = tk.Entry(entryframe, width=85)
        self.entry4.grid(pady=5, row=3, column=1, sticky="ew")

        entry5label = tk.Label(entryframe, text="Harga Beli", font=('Helvetica', 10), bg="#ADDFFF")
        entry5label.grid(row=4, column=0, sticky="w")
        self.entry5 = tk.Entry(entryframe, width=85)
        self.entry5.grid(pady=5, row=4, column=1, sticky="ew")

        entry6label = tk.Label(entryframe, text="ID Pemasok", font=('Helvetica', 10), bg="#ADDFFF")
        entry6label.grid(row=5, column=0, sticky="w")
        self.entry6 = tk.Entry(entryframe, width=85)
        self.entry6.grid(pady=5, row=5, column=1, sticky="ew")

        entry7label = tk.Label(entryframe, text="ID Gudang", font=('Helvetica', 10), bg="#ADDFFF")
        entry7label.grid(row=6, column=0, sticky="w")
        self.entry7 = tk.Entry(entryframe, width=85)
        self.entry7.grid(pady=5, row=6, column=1, sticky="ew")

        entry8label = tk.Label(entryframe, text="Jumlah_disimpan", font=('Helvetica', 10), bg="#ADDFFF")
        entry8label.grid(row=7, column=0, sticky="w")
        self.entry8 = tk.Entry(entryframe, width=85)
        self.entry8.grid(pady=5, row=7, column=1, sticky="ew")

        entryframe.pack(fill="x")

        self.viewbarang = ttk.Treeview(frame)
        self.viewbarang["columns"] =("ID_BARANG", "Nama_Barang", "Jumlah_Barang", "Harga_Jual", "Harga_Beli", "ID_PEMASOK", "ID_GUDANG", "Alamat", "Tanggal", "Jumlah_disimpan")

        self.viewbarang.column("#0", width=0, stretch=tk.NO)

        for col in self.viewbarang["columns"]:
            self.viewbarang.column(col, anchor="w", width=200)
            self.viewbarang.heading(col, text=col)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.viewbarang.yview)
        self.viewbarang.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        scrollbar2 = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=self.viewbarang.xview)
        self.viewbarang.configure(xscroll=scrollbar2.set)
        scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)

        self.viewbarang.pack(expand=True, fill=tk.BOTH)
        self.Find_Barang()

        self.viewbarang.bind("<<TreeviewSelect>>", self.pilih_barang)

    def Create_Barang(self):
 
        cursor.execute("SELECT ID_BARANG FROM barang ORDER BY ID_BARANG DESC LIMIT 1")
        result = cursor.fetchone()
        new_id_num = int(result[0][2:]) + 1 if result else 1
        new_id = f"B{new_id_num:04d}"

        tanggal_sekarang = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        try:
            cursor.execute("""
                INSERT INTO barang (ID_BARANG, Nama_Barang, Jumlah_Barang, Stok_Barang, Harga_Jual)
                VALUES (%s, %s, %s, %s, %s)
            """, (new_id, self.entry2.get(), self.entry3.get(), self.entry3.get(), self.entry4.get()))

            cursor.execute("""INSERT INTO penyimpanan (ID_BARANG, ID_GUDANG, Tanggal_masuk, Jumlah_disimpan) 
                           VALUES(%s, %s, %s, %s)
            """, (new_id, self.entry7.get(), tanggal_sekarang, self.entry8.get()))

            cursor.execute("""INSERT INTO detail_pemasokan (ID_PEMASOK, ID_BARANG, Tanggal, Jumlah, Harga) 
                           VALUES(%s, %s, %s, %s, %s)
            """, (self.entry6.get(), new_id, tanggal_sekarang, self.entry3.get(), self.entry5.get()))

            db.commit()

            for entry in [self.entry1, self.entry2, self.entry3, self.entry4, self.entry5, self.entry6, self.entry7, self.entry8]:
                entry.delete(0, tk.END)

            self.Find_Barang()

            messagebox.showinfo("Berhasil", "Data Penjualan berhasil dibuat") 
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def Find_Barang(self, id_barang=None):
        for row in self.viewbarang.get_children():
            self.viewbarang.delete(row)

        try:
            if id_barang:
                cursor.execute("""
                    SELECT b.ID_BARANG, b.Nama_Barang, b.Jumlah_Barang, b.Harga_Jual, db.Harga, 
                               GROUP_CONCAT(db.ID_PEMASOK SEPARATOR ',') AS ID_PEMASOK, db.ID_GUDANG, db.Alamat, db.Tanggal_masuk, db.Jumlah_disimpan
                    FROM barang b NATURAL LEFT JOIN (SELECT * FROM detail_pemasokan dp NATURAL JOIN pemasok p NATURAL JOIN gudang g NATURAL JOIN penyimpanan pe) AS db 
                    GROUP BY b.ID_BARANG HAVING b.ID_BARANG = %s;
                """, (id_barang,))
            else:
                cursor.execute("""
                    SELECT b.ID_BARANG, b.Nama_Barang, b.Jumlah_Barang, b.Harga_Jual, db.Harga, 
                               GROUP_CONCAT(db.ID_PEMASOK SEPARATOR ',') AS ID_PEMASOK, db.ID_GUDANG, db.Alamat, db.Tanggal_masuk, db.Jumlah_disimpan
                    FROM barang b NATURAL LEFT JOIN (SELECT * FROM detail_pemasokan dp NATURAL JOIN pemasok p NATURAL JOIN gudang g NATURAL JOIN penyimpanan pe) AS db 
                    GROUP BY b.ID_BARANG;
                """)

            for result in cursor.fetchall():
                self.viewbarang.insert("", tk.END, values=result)
        except Exception as e:
            messagebox.showerror("ERROR", str(e))

    def delete_Barang(self):
        id = self.entry1.get()

        if not id:
            messagebox.showerror("ERROR", "ID Barang harus diiisi")
            return
        try:
            check = messagebox.askyesnocancel("Cek", "Yakin data akan dihapus?")

            if check: 
                cursor.execute("DELETE FROM detail_penjualan WHERE ID_BARANG = %s", (id,))

                cursor.execute("DELETE FROM detail_pemasokan WHERE ID_BARANG = %s", (id,))

                cursor.execute("DELETE FROM penyimpanan WHERE ID_BARANG = %s", (id,))

                cursor.execute("DELETE FROM barang WHERE ID_BARANG = %s", (id,))

                db.commit()

                messagebox.showinfo("SUKSES", "Data barang berhasil dihapus")

                for entry in [self.entry1, self.entry2, self.entry3, self.entry4, self.entry5, self.entry6, self.entry7, self.entry8]:
                    entry.delete(0, tk.END)

                self.Find_Barang()
            else:
                return
        except Exception as e:
            db.rollback()
            messagebox.showerror("Error", f"Gagal menghapus data: {str(e)}") 

    def update_barang(self):
        try:
            cursor.execute("""
                UPDATE barang SET ID_BARANG = %s, Nama_Barang = %s, Jumlah_Barang =%s, Stok_Barang = %s, Harga_Jual = %s WHERE ID_BARANG = %s
            """, (self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry3.get(), self.entry4.get(), self.entry1.get()))

            cursor.execute("""UPDATE penyimpanan SET ID_BARANG = %s, ID_GUDANG = %s, Jumlah_disimpan = %s WHERE ID_BARANG = %s
            """, (self.entry1.get(), self.entry7.get(), self.entry8.get(), self.entry1.get()))

            cursor.execute("""UPDATE detail_pemasokan SET ID_PEMASOK = %s, ID_BARANG = %s, Jumlah = %s, Harga =%s WHERE ID_BARANG = %s 
            """, (self.entry6.get(), self.entry1.get(), self.entry3.get(), self.entry5.get(), self.entry1.get()))

            db.commit()

            for entry in [self.entry1, self.entry2, self.entry3, self.entry4, self.entry5, self.entry6, self.entry7, self.entry8]:
                entry.delete(0, tk.END)

            self.Find_Barang()

            db.commit()
            messagebox.showinfo("Berhasil", "Data Barang berhasil diupdate.")
        except Exception as e:
            db.rollback()
            messagebox.showerror("ERROR", str(e))
        
        self.Find_Barang()

    def pilih_barang (self, event):
        pilihID = ''
        pilih = self.viewbarang.selection()[0]

        if pilih:
            pilihID = str(self.viewbarang.item(pilih)['values'][0])
            
            cursor.execute("""
                    SELECT b.ID_BARANG, b.Nama_Barang, b.Jumlah_Barang, b.Harga_Jual, db.Harga, 
                               GROUP_CONCAT(db.ID_PEMASOK SEPARATOR ',') AS ID_PEMASOK, db.ID_GUDANG, b.Stok_Barang
                    FROM barang b NATURAL LEFT JOIN (SELECT * FROM detail_pemasokan dp NATURAL JOIN pemasok p NATURAL JOIN gudang g NATURAL JOIN penyimpanan pe) AS db 
                    GROUP BY b.ID_BARANG HAVING b.ID_BARANG = %s;
                """, (pilihID,))
            
            dataentry = []
            hasil = cursor.fetchall()
            for x in hasil:
                for y in x:
                    dataentry.append(y)

            entry_barang = [self.entry1, self.entry2, self.entry3, self.entry4, self.entry5, self.entry6, self.entry7, self.entry8]

            for entry, dataentry in zip(entry_barang, dataentry):
                if dataentry is None:
                    continue
                entry.delete(0, tk.END)
                entry.insert(0, dataentry)
#Pengeluaran [v]

    def Pengeluaran(self, frame):
        self.clear(frame)

        #GUI
        headingframe = tk.Frame(frame, bg="#ADDFFF" )
        heading = tk.Label(headingframe, text="Pengeluaran", font=('Helvetica', 20, 'bold'), bg="#ADDFFF")
        heading.grid(row=0, column=0, pady=10, padx=40, sticky="w")

        backbutton=tk.Button(headingframe, text="Kembali", bg="white", font=('Helvetica', 10), command= lambda: [self.destroy(), Sistem()])
        backbutton.grid(row=0, column=1, pady=10, padx=450, sticky="e")
        headingframe.pack()

        buttonframe = tk.LabelFrame(frame, text="Manage", bg="white")

        btn1 = tk.Button(buttonframe, text="Update", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=self.update_pengeluaran)
        btn1.grid(padx=25, pady=5, row=0, column=0)

        btn2 = tk.Button(buttonframe, text="Delete", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=self.delete_Pengeluaran)
        btn2.grid(padx=25,pady=5, row=0, column=1)

        btn3 = tk.Button(buttonframe, text="Create", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=self.Create_Pengeluaran)
        btn3.grid(padx=25,pady=5, row=0, column=2)

        btn4 = tk.Button(buttonframe, text="Find", font=('Helvetica', 10), width=15, relief="groove", bg="white", command= lambda: self.Find_Pengeluaran(self.id_pengeluaran_entry.get()))
        btn4.grid(padx=25,pady=5, row=0, column=3)

        buttonframe.pack()

        entryframe=tk.Frame(frame, bg="#ADDFFF", padx=40, pady=5)

        entry1label = tk.Label(entryframe, text="ID_PENGELUARAN", font=('Helvetica', 10), bg="#ADDFFF")
        entry1label.grid(row=0, column=0, sticky="w")
        self.id_pengeluaran_entry = tk.Entry(entryframe, width=75)
        self.id_pengeluaran_entry.grid(pady=5, row=0, column=1, sticky="w")

        btnID = tk.Button(entryframe, text="Auto ID", font=('Helvetica', 10), width=12, relief="groove", bg="white", 
                          command= lambda: self.generate_auto_id(self.id_pengeluaran_entry, "PENGELUARAN", "ID_PENGELUARAN", "PG"))
        btnID.grid(row=0, column=1, sticky="e", padx=7)
        
        entry5label = tk.Label(entryframe, text="ID_PEMASOK", font=('Helvetica', 10), bg="#ADDFFF")
        entry5label.grid(row=1, column=0, sticky="w")
        self.id_pemasok_entry = tk.Entry(entryframe, width=85)
        self.id_pemasok_entry.grid(pady=5, row=1, column=1, sticky="ew")

        entry6label = tk.Label(entryframe, text="ID_Pegawai", font=('Helvetica', 10), bg="#ADDFFF")
        entry6label.grid(row=2, column=0, sticky="w")
        self.id_pegawai_entry = tk.Entry(entryframe, width=85)
        self.id_pegawai_entry.grid(pady=5, row=2, column=1, sticky="ew")

        entry2label = tk.Label(entryframe, text="Nama_Pengeluaran", font=('Helvetica', 10), bg="#ADDFFF")
        entry2label.grid(row=3, column=0, sticky="w")
        self.nama_pengeluaran_entry= tk.Entry(entryframe, width=98)
        self.nama_pengeluaran_entry.grid(pady=5, row=3, column=1, sticky="ew")

        entry3label = tk.Label(entryframe, text="Jumlah_Pengeluaran", font=('Helvetica', 10), bg="#ADDFFF")
        entry3label.grid(row=4, column=0, sticky="w")
        self.jumlah_pengeluaran_entry = tk.Entry(entryframe, width=85)
        self.jumlah_pengeluaran_entry.grid(pady=5, row=4, column=1, sticky="ew")

        entry4label = tk.Label(entryframe, text="Tanggal", font=('Helvetica', 10), bg="#ADDFFF")
        entry4label.grid(row=5, column=0, sticky="w")
        self.tanggal_entry = tk.Entry(entryframe, width=85)
        self.tanggal_entry.grid(pady=5, row=5, column=1, sticky="ew")

        entryframe.pack(fill="x")

        self.viewbarang = ttk.Treeview(frame)
        self.viewbarang["columns"] = ("ID_PENGELUARAN", "ID_PEMASOK", "ID_Pegawai", "Nama_Pengeluaran", "Jumlah_Pengeluaran","Tanggal_Pengeluaran")

        self.viewbarang.column("#0", width=0, stretch=tk.NO)
        for col in self.viewbarang["columns"]:
                self.viewbarang.column(col, anchor="w", width=150)
                self.viewbarang.heading(col, text=col)
               

        scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.viewbarang.yview)
        scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=self.viewbarang.xview)
        self.viewbarang.configure(yscroll=scrollbar_y.set, xscroll=scrollbar_x.set)

        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.viewbarang.pack(expand=True, fill=tk.BOTH)

        self.Find_Pengeluaran()
        self.viewbarang.bind("<<TreeviewSelect>>", self.pilih_pengeluaran)
     
    def Create_Pengeluaran(self):
 
        cursor.execute("SELECT ID_PENGELUARAN FROM pengeluaran ORDER BY ID_PENGELUARAN DESC LIMIT 1")
        result = cursor.fetchone()
        new_id_num = int(result[0][2:]) + 1 if result else 1
        new_id = f"PG{new_id_num:03d}"

        try:
            cursor.execute("""
                INSERT INTO pengeluaran (ID_PENGELUARAN, ID_PEMASOK, ID_PEGAWAI, Nama_Pengeluaran, Jumlah_Pengeluaran, Tanggal_Pengeluaran)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (new_id, self.id_pemasok_entry.get() or None, self.id_pegawai_entry.get() or None, self.nama_pengeluaran_entry.get(), self.jumlah_pengeluaran_entry.get(), self.tanggal_entry.get()))

            db.commit()

            self.id_pengeluaran_entry.delete(0, tk.END)
            self.id_pengeluaran_entry.insert(0, new_id)
            self.id_pemasok_entry.delete(0,tk.END)
            self.id_pegawai_entry.delete(0,tk.END)
            self.nama_pengeluaran_entry.delete(0,tk.END)
            self.jumlah_pengeluaran_entry.delete(0,tk.END)
            self.tanggal_entry.delete(0,tk.END)

            self.Find_Pengeluaran()

            messagebox.showinfo("Berhasil", "Data Pengeluaran berhasil dibuat")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def Find_Pengeluaran(self, id_pengeluaran=None):
        for row in self.viewbarang.get_children():
            self.viewbarang.delete(row)

        try:
            if id_pengeluaran:
                cursor.execute("""SELECT * FROM pengeluaran WHERE ID_PENGELUARAN = %s""", (id_pengeluaran,))
            else:
                cursor.execute("""SELECT * FROM pengeluaran""")

            for result in cursor.fetchall():
                self.viewbarang.insert("", tk.END, values=result)
        except Exception as e:
            messagebox.showerror("ERROR", str(e))

    def delete_Pengeluaran(self):
        id_pengeluaran = self.id_pengeluaran_entry.get()

        if not id_pengeluaran:
            messagebox.showerror("ERROR", "ID Pengeluaran harus diiisi")
            return
        try:
            check = messagebox.askyesnocancel("Cek", "Yakin data akan dihapus?")

            if check: 
                cursor.execute("DELETE FROM pengeluaran WHERE ID_PENGELUARAN = %s", (id_pengeluaran,))

                db.commit()

                messagebox.showinfo("SUKSES", "Data pengeluaran berhasil dihapus")

                for entry in [self.id_pengeluaran_entry, self.id_pemasok_entry, self.id_pegawai_entry, self.nama_pengeluaran_entry, self.jumlah_pengeluaran_entry, self.tanggal_entry]:
                    entry.delete(0, tk.END)

                self.Find_Pengeluaran()
            else:
                return
        except Exception as e:
         messagebox.showerror("Error", f"Gagal menghapus data: {str(e)}") 

    def update_pengeluaran(self):
     try:
        cursor.execute("""UPDATE pengeluaran SET ID_PEMASOK = %s, ID_PEGAWAI = %s, Nama_Pengeluaran = %s, Jumlah_Pengeluaran = %s, Tanggal_Pengeluaran=%s WHERE ID_PENGELUARAN = %s""", 
                       (self.id_pemasok_entry.get() or None, self.id_pegawai_entry.get() or None, self.nama_pengeluaran_entry.get(), self.jumlah_pengeluaran_entry.get(), self.tanggal_entry.get(), self.id_pengeluaran_entry.get()))

        db.commit()
        messagebox.showinfo("Berhasil", "Data pengeluaran berhasil diupdate.")
     except Exception as e:
        db.rollback()
        messagebox.showerror("ERROR", str(e))
        
        self.Find_Pengeluaran()

    def pilih_pengeluaran (self, event):
        pilihID = ''
        pilih = self.viewbarang.selection()[0]

        if pilih:
            pilihID = str(self.viewbarang.item(pilih)['values'][0])
            
            cursor.execute("""SELECT * FROM pengeluaran WHERE ID_PENGELUARAN  = %s;""", (pilihID,))
            
            dataentry = []
            hasil = cursor.fetchall()
            for x in hasil:
                for y in x:
                    dataentry.append(y)

            entry_pengeluaran = [self.id_pengeluaran_entry, self.id_pemasok_entry, self.id_pegawai_entry, self.nama_pengeluaran_entry, self.jumlah_pengeluaran_entry, self.tanggal_entry]

            for entry, dataentry in zip(entry_pengeluaran, dataentry):
                if dataentry is None:
                    continue
                entry.delete(0, tk.END)
                entry.insert(0, dataentry)

#Pengiriman [v]

    def Pengiriman(self, frame):
        self.clear(frame)

        #GUI
        headingframe = tk.Frame(frame, bg="#ADDFFF" )
        heading = tk.Label(headingframe, text="Pengiriman ", font=('Helvetica', 20, 'bold'), bg="#ADDFFF")
        heading.grid(row=0, column=0, pady=10, padx=40, sticky="w")

        backbutton=tk.Button(headingframe, text="Kembali", bg="white", font=('Helvetica', 10), command= lambda: [self.destroy(), Sistem()])
        backbutton.grid(row=0, column=1, pady=10, padx=453, sticky="e")
        headingframe.pack()

        buttonframe = tk.LabelFrame(frame, text="Manage", bg="white")

        btn1 = tk.Button(buttonframe, text="Update", font=('Helvetica', 10), width=15, relief="groove", bg="white", command= self.update_pengiriman)
        btn1.grid(padx=25, pady=5, row=0, column=0)

        btn2 = tk.Button(buttonframe, text="Delete", font=('Helvetica', 10), width=15, relief="groove", bg="white", command= self.delete_pengiriman)
        btn2.grid(padx=25,pady=5, row=0, column=1)

        btn3 = tk.Button(buttonframe, text="Create", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=self.Create_Pengiriman)
        btn3.grid(padx=25,pady=5, row=0, column=2)

        btn4 = tk.Button(buttonframe, text="Find", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=lambda: self.Find_Pengiriman(self.id_pengiriman_entry.get()))
        btn4.grid(padx=25,pady=5, row=0, column=3)

        buttonframe.pack()

        entryframe=tk.Frame(frame, bg="#ADDFFF", padx=40, pady=5)

        entry1label = tk.Label(entryframe, text="ID_Pengiriman", font=('Helvetica', 10), bg="#ADDFFF")
        entry1label.grid(row=0, column=0, sticky="w")
        self.id_pengiriman_entry = tk.Entry(entryframe, width=75)
        self.id_pengiriman_entry.grid(pady=5, row=0, column=1, sticky="w")

        btnID = tk.Button(entryframe, text="Auto ID", font=('Helvetica', 10), width=12, relief="groove", bg="white",
                          command= lambda: self.generate_auto_id(self.id_pengiriman_entry, "pengiriman", "ID_PENGIRIMAN", "PM"))
        btnID.grid(row=0, column=1, sticky="e", padx=7)

        entry2label = tk.Label(entryframe, text="ID_Penjualan", font=('Helvetica', 10), bg="#ADDFFF")
        entry2label.grid(row=1, column=0, sticky="w")
        self.id_penjualan_entry = tk.Entry(entryframe, width=98)
        self.id_penjualan_entry.grid(pady=5, row=1, column=1, sticky="ew")

        entry3label = tk.Label(entryframe, text="ID_Pelanggan_Grosir", font=('Helvetica', 10), bg="#ADDFFF")
        entry3label.grid(row=2, column=0, sticky="w")
        self.id_pelanggan_grosir_entry = tk.Entry(entryframe, width=85)
        self.id_pelanggan_grosir_entry.grid(pady=5, row=2, column=1, sticky="ew")

        entry4label = tk.Label(entryframe, text="ID_Pegawai", font=('Helvetica', 10), bg="#ADDFFF")
        entry4label.grid(row=3, column=0, sticky="w")
        self.id_pegawai_entry = tk.Entry(entryframe, width=85)
        self.id_pegawai_entry.grid(pady=5, row=3, column=1, sticky="ew")

        entry5label = tk.Label(entryframe, text="Status_Pengiriman", font=('Helvetica', 10), bg="#ADDFFF")
        entry5label.grid(row=4, column=0, sticky="w")
        status_options = ["Menunggu Pengiriman", "Dalam Perjalanan", "Terkirim"]
        status_pengiriman_var = tk.StringVar()
        self.status_pengiriman_entry = ttk.Combobox(entryframe, textvariable=status_pengiriman_var, values=status_options, width=83)
        self.status_pengiriman_entry.grid(pady=5, row=4, column=1, sticky="ew")
        self.status_pengiriman_entry.set("Menunggu Pengiriman")

        entry6label = tk.Label(entryframe, text="Tanggal", font=('Helvetica', 10), bg="#ADDFFF")
        entry6label.grid(row=5, column=0, sticky="w")
        self.tanggal_pengiriman_entry = tk.Entry(entryframe, width=85)
        self.tanggal_pengiriman_entry.grid(pady=5, row=5, column=1, sticky="ew")

        entryframe.pack(fill="x") 

        self.viewbarang = ttk.Treeview(frame)
        self.viewbarang["columns"] =("ID_Pengiriman", "ID_Penjualan", "ID_Pelanggan_Grosir", "ID_PEGAWAI","Status_Pengiriman", "Tanggal")

        self.viewbarang.column("#0", width=0, stretch=tk.NO)

        self.viewbarang.column("#0", width=0, stretch=tk.NO)
        for col in self.viewbarang["columns"]:
                if col == "Alamat":
                    self.viewbarang.column(col, anchor="w", width=300)
                    self.viewbarang.heading(col, text=col) 
                else:
                 self.viewbarang.column(col, anchor="w", width=150)
                 self.viewbarang.heading(col, text=col)            

        scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.viewbarang.yview)
        scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=self.viewbarang.xview)
        self.viewbarang.configure(yscroll=scrollbar_y.set, xscroll=scrollbar_x.set)

        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.viewbarang.pack(expand=True, fill=tk.BOTH)

        self.Find_Pengiriman()

        self.viewbarang.bind("<<TreeviewSelect>>", self.pilih_Pengiriman)

    def Find_Pengiriman(self, id_pengiriman=None): 
        for row in self.viewbarang.get_children():
            self.viewbarang.delete(row)

        try:
            if id_pengiriman:
                cursor.execute("""SELECT p.ID_PENGIRIMAN, p1.ID_PENJUALAN, k.ID_PELANGGAN_GROSIR, p2.ID_PEGAWAI, P.Status_Pengiriman, p.Tanggal 
                               FROM pengiriman p NATURAL LEFT JOIN pesanan p1 NATURAL LEFT JOIN pengantaran p2 NATURAL LEFT JOIN pegawai p3 NATURAL LEFT JOIN kiriman k NATURAL LEFT JOIN pelanggan_grosir p5 
                               WHERE ID_PENGIRIMAN = %s GROUP BY p.ID_PENGIRIMAN; """, (id_pengiriman,))
            else:
                cursor.execute("""SELECT p.ID_PENGIRIMAN, p1.ID_PENJUALAN, k.ID_PELANGGAN_GROSIR, p2.ID_PEGAWAI, P.Status_Pengiriman, p.Tanggal 
                               FROM pengiriman p NATURAL LEFT JOIN pesanan p1 NATURAL LEFT JOIN pengantaran p2 NATURAL LEFT JOIN pegawai p3 NATURAL LEFT JOIN kiriman k NATURAL LEFT JOIN pelanggan_grosir p5 
                               GROUP BY p.ID_PENGIRIMAN;""")
                
            for result in cursor.fetchall():
                self.viewbarang.insert("", tk.END, values=result)
        except Exception as e:
            messagebox.showerror("ERROR", str(e))

    def Create_Pengiriman(self):
        cursor.execute("SELECT ID_PENGIRIMAN FROM pengiriman ORDER BY ID_PENGIRIMAN DESC LIMIT 1")
        result = cursor.fetchone()
        new_id_num = int(result[0][2:]) + 1 if result else 1
        new_id = f"PM{new_id_num:03d}"
        self.tanggal_sekarang = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        try:

            cursor.execute("""INSERT INTO pengiriman (ID_PENGIRIMAN, Tanggal, Status_Pengiriman) VALUES (%s, %s, %s)""", 
                           (self.id_pengiriman_entry.get(), self.tanggal_pengiriman_entry.get(), self.status_pengiriman_entry.get()))
            
            cursor.execute("""INSERT INTO pesanan (ID_PENJUALAN, ID_PENGIRIMAN) VALUES (%s, %s) """, 
                           (self.id_penjualan_entry.get(), self.id_pengiriman_entry.get()))
            
            cursor.execute("""INSERT INTO kiriman (ID_PELANGGAN_GROSIR, ID_PENGIRIMAN) VALUES (%s, %s) """, 
                           (self.id_pelanggan_grosir_entry.get(), self.id_pengiriman_entry.get()))

            cursor.execute("""INSERT INTO pengantaran (ID_PENGIRIMAN, ID_PEGAWAI) VALUES (%s, %s)""",
               (self.id_pengiriman_entry.get(), self.id_pegawai_entry.get()))

            
    

            db.commit()
            
            for entry in [ self.id_pengiriman_entry,
                self.id_penjualan_entry,
                self.id_pelanggan_grosir_entry,
                self.id_pegawai_entry,
                self.status_pengiriman_entry,
                self.tanggal_pengiriman_entry,
                ]:
                entry.delete(0, tk.END)

            messagebox.showinfo("Berhasil", "Data Pengiriman berhasil dibuat")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
        self.Find_Pengiriman()

    def delete_pengiriman(self):
        id= self.id_pengiriman_entry.get()
        if not id:
            messagebox.showerror("ERROR", "ID Pengiriman harus diiisi")
            return
        try:
            cursor.execute("DELETE FROM pesanan WHERE ID_PENGIRIMAN = %s", (id,))
            cursor.execute("DELETE FROM kiriman WHERE ID_PENGIRIMAN = %s", (id,))
            cursor.execute("DELETE FROM pengantaran WHERE ID_PENGIRIMAN = %s", (id,))
            cursor.execute("DELETE FROM pengiriman WHERE ID_PENGIRIMAN = %s", (id,))
 
            db.commit()

            messagebox.showinfo("SUKSES", "Data pemasokan berhasil dihapus")

            for entry in [ self.id_pengiriman_entry,  self.id_penjualan_entry, self.id_pelanggan_grosir_entry,  self.id_pegawai_entry, 
                      self.status_pengiriman_entry, self.tanggal_pengiriman_entry]:
                entry.delete(0, tk.END)
    
            self.Find_Pengiriman()
        except Exception as e:
         messagebox.showerror("Error", f"Gagal menghapus data: {str(e)}")

    def update_pengiriman(self):
        try:
            cursor.execute("""UPDATE pesanan SET ID_PENJUALAN = %s, ID_PENGIRIMAN = %s WHERE ID_PENGIRIMAN = %s;""", 
                           (self.id_penjualan_entry.get(), self.id_pengiriman_entry.get(),  self.id_pengiriman_entry.get()
                )) 
            cursor.execute("""UPDATE pengiriman SET ID_PENGIRIMAN = %s, Tanggal = %s, Status_Pengiriman = %s WHERE ID_PENGIRIMAN = %s;""", 
                           (self.id_pengiriman_entry.get(), self.tanggal_pengiriman_entry.get(), self.status_pengiriman_entry.get(), self.id_pengiriman_entry.get()
                )) 
            cursor.execute("""UPDATE pengantaran SET ID_PENGIRIMAN = %s, ID_PEGAWAI = %s WHERE ID_PENGIRIMAN = %s;""", 
                           (self.id_pengiriman_entry.get(), self.id_pegawai_entry.get(), self.id_pengiriman_entry.get()
                )) 
            cursor.execute("""UPDATE kiriman SET ID_PENGIRIMAN = %s, ID_PELANGGAN_GROSIR = %s WHERE ID_PENGIRIMAN = %s;""", 
                           (self.id_pengiriman_entry.get(), self.id_pelanggan_grosir_entry.get(), self.id_pengiriman_entry.get()
                )) 

            for entry in [ self.id_pengiriman_entry,
                self.id_penjualan_entry,
                self.id_pelanggan_grosir_entry,
                self.id_pegawai_entry,
                self.status_pengiriman_entry,
                self.tanggal_pengiriman_entry,
                ]:
                entry.delete(0, tk.END)

            self.Find_Pengiriman()

            db.commit()
            messagebox.showinfo("Berhasil", "Data Pengiriman berhasil diupdate.")
        except Exception as e:
            db.rollback()
            messagebox.showerror("ERROR", str(e))
        
        self.Find_Pengiriman()

    def pilih_Pengiriman (self, event):
        pilihID = ''
        pilih = self.viewbarang.selection()[0]

        if pilih:
            pilihID = str(self.viewbarang.item(pilih)['values'][0])
            
            cursor.execute("""SELECT p.ID_PENGIRIMAN, p1.ID_PENJUALAN, k.ID_PELANGGAN_GROSIR, p2.ID_PEGAWAI, P.Status_Pengiriman, p.Tanggal 
                               FROM pengiriman p NATURAL LEFT JOIN pesanan p1 NATURAL LEFT JOIN pengantaran p2 NATURAL LEFT JOIN pegawai p3 NATURAL LEFT JOIN kiriman k NATURAL LEFT JOIN pelanggan_grosir p5 
                               WHERE ID_PENGIRIMAN = %s GROUP BY p.ID_PENGIRIMAN; """, (pilihID,))
            
            dataentry = []
            hasil = cursor.fetchall()
            for x in hasil:
                for y in x:
                    dataentry.append(y)

            entry_ = [
                self.id_pengiriman_entry,
                self.id_penjualan_entry,
                self.id_pelanggan_grosir_entry,
                self.id_pegawai_entry,
                self.status_pengiriman_entry,
                self.tanggal_pengiriman_entry,
                ]

            for entry, dataentry in zip(entry_, dataentry):
                entry.delete(0, tk.END)
                if dataentry is not None:
                    entry.insert(0, dataentry)
                else:
                    entry.insert(0, "")

#PEMASOK [v]

    def Pemasok(self, frame): 

        self.clear(frame)

        #GUI
        headingframe = tk.Frame(frame, bg="#ADDFFF" )
        heading = tk.Label(headingframe, text="Pemasokan", font=('Helvetica', 20, 'bold'), bg="#ADDFFF")
        heading.grid(row=0, column=0, pady=10, padx=40, sticky="w")

        backbutton=tk.Button(headingframe, text="Kembali", bg="white", font=('Helvetica', 10), command= lambda: [self.destroy(), Sistem()])
        backbutton.grid(row=0, column=1, pady=10, padx=480, sticky="e")
        headingframe.pack()

        buttonframe = tk.LabelFrame(frame, text="Manage", bg="white")

        btn1 = tk.Button(buttonframe, text="Update", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=self.update_pemasokan)
        btn1.grid(padx=25, pady=5, row=0, column=0)

        btn2 = tk.Button(buttonframe, text="Delete", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=self.delete_pemasok)
        btn2.grid(padx=25,pady=5, row=0, column=1)

        btn3 = tk.Button(buttonframe, text="Create", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=self.Create_Pemasok)
        btn3.grid(padx=25,pady=5, row=0, column=2)

        btn4 = tk.Button(buttonframe, text="Find", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=lambda: self.Find_Pemasok(self.id_pemasok_entry.get().strip()))

        btn4.grid(padx=25,pady=5, row=0, column=3)

        buttonframe.pack()

        entryframe=tk.Frame(frame, bg="#ADDFFF", padx=40, pady=5)

        entry1label = tk.Label(entryframe, text="ID_PEMASOK", font=('Helvetica', 10), bg="#ADDFFF")
        entry1label.grid(row=0, column=0, sticky="w")
        self.id_pemasok_entry = tk.Entry(entryframe, width=80)
        self.id_pemasok_entry.grid(pady=5, row=0, column=1, sticky="w")

        entry2label = tk.Label(entryframe, text="ID_BARANG", font=('Helvetica', 10), bg="#ADDFFF")
        entry2label.grid(row=1, column=0, sticky="w")
        self.id_barang_entry = tk.Entry(entryframe, width=102)
        self.id_barang_entry.grid(pady=5, row=1, column=1, sticky="w")

        btnID = tk.Button(entryframe, text="Auto ID", font=('Helvetica', 10), width=12, relief="groove", bg="white",
                          command= lambda: self.generate_auto_id(self.id_pemasok_entry, "pemasok", "ID_PEMASOK", "PK"))
        btnID.grid(row=0, column=1, sticky="e", padx=7)

        entry2label = tk.Label(entryframe, text="Nama_Pemasok", font=('Helvetica', 10), bg="#ADDFFF")
        entry2label.grid(row=2, column=0, sticky="w")
        self.nama_pemasok_entry = tk.Entry(entryframe, width=92)
        self.nama_pemasok_entry.grid(pady=5, row=2, column=1, sticky="ew")

        entry3label = tk.Label(entryframe, text="Alamat_Pemasok", font=('Helvetica', 10), bg="#ADDFFF")
        entry3label.grid(row=3, column=0, sticky="w")
        self.alamat_pemasok_entry = tk.Entry(entryframe, width=85)
        self.alamat_pemasok_entry.grid(pady=5, row=3, column=1, sticky="ew")

        entry5label = tk.Label(entryframe, text="Kontak_Pemasok", font=('Helvetica', 10), bg="#ADDFFF")
        entry5label.grid(row=4, column=0, sticky="w")
        self.kontak_pemasok_entry = tk.Entry(entryframe, width=85)
        self.kontak_pemasok_entry.grid(pady=5, row=4, column=1, sticky="ew")

        entry5label = tk.Label(entryframe, text="Jumlah", font=('Helvetica', 10), bg="#ADDFFF")
        entry5label.grid(row=6, column=0, sticky="w")
        self.jumlah_entry = tk.Entry(entryframe, width=85)
        self.jumlah_entry.grid(pady=5, row=6, column=1, sticky="ew")

        entry5label = tk.Label(entryframe, text="Harga", font=('Helvetica', 10), bg="#ADDFFF")
        entry5label.grid(row=7, column=0, sticky="w")
        self.harga_entry = tk.Entry(entryframe, width=85)
        self.harga_entry.grid(pady=5, row=7, column=1, sticky="ew")

        entryframe.pack(fill="x")

        self.viewbarang = ttk.Treeview(frame)
        self.viewbarang["columns"] = ("ID_PEMASOK", "ID_BARANG","Nama_Pemasok", "Alamat_Pemasok", "Kontak_Pemasok","Tanggal", "Jumlah", "Harga")


        self.viewbarang.column("#0", width=0, stretch=tk.NO)
        for col in self.viewbarang["columns"]:
                self.viewbarang.column(col, anchor="w", width=150)
                self.viewbarang.heading(col, text=col)             

        scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.viewbarang.yview)
        scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=self.viewbarang.xview)
        self.viewbarang.configure(yscroll=scrollbar_y.set, xscroll=scrollbar_x.set)

        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.viewbarang.pack(expand=True, fill=tk.BOTH)

        self.Find_Pemasok()

        self.viewbarang.bind("<<TreeviewSelect>>", self.pilih_pemasok)

    def Find_Pemasok(self, id_pemasok=None):
        for row in self.viewbarang.get_children():
            self.viewbarang.delete(row)

        try:
            if id_pemasok:
                cursor.execute("""SELECT p.ID_PEMASOK, GROUP_CONCAT(d.ID_BARANG SEPARATOR ','), p.Nama_Pemasok, p.Alamat_Pemasok, p.Kontak_Pemasok, GROUP_CONCAT(d.Jumlah SEPARATOR ','),GROUP_CONCAT(d.Harga SEPARATOR ',') FROM pemasok p JOIN detail_pemasokan d  
                               ON p.ID_PEMASOK = d.ID_PEMASOK WHERE p.ID_PEMASOK= %s GROUP BY p.ID_PEMASOK""", (id_pemasok,))
            else:
                cursor.execute("""SELECT p.ID_PEMASOK, GROUP_CONCAT(d.ID_BARANG SEPARATOR ','), p.Nama_Pemasok, p.Alamat_Pemasok,p.Kontak_Pemasok, d.Tanggal, GROUP_CONCAT(d.Jumlah SEPARATOR ','),GROUP_CONCAT(d.Harga SEPARATOR ',') FROM pemasok p JOIN detail_pemasokan d  
                               ON p.ID_PEMASOK = d.ID_PEMASOK GROUP BY p.ID_PEMASOK""")
            for result in cursor.fetchall():
                self.viewbarang.insert("", tk.END, values=result)
        except Exception as e:
            messagebox.showerror("ERROR", str(e))

    def Create_Pemasok(self):
     cursor.execute("SELECT ID_PEMASOK FROM Pemasok ORDER BY ID_PEMASOK DESC LIMIT 1")
     result = cursor.fetchone()
     new_id_num = int(result[0][2:]) + 1 if result else 1
     new_id = f"PK{new_id_num:03d}"

     cursor.execute("SELECT COUNT(*) FROM Pemasok WHERE ID_PEMASOK = %s", (new_id,))
     if cursor.fetchone()[0] > 0:
         new_id_num += 1
         new_id = f"PK{new_id_num:03d}"

     self.tanggal_sekarang = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

     id_barang = str(self.id_barang_entry.get())
     nama_pemasok = str(self.nama_pemasok_entry.get())  
     alamat_pemasok = str(self.alamat_pemasok_entry.get())  
     kontak_pemasok = str(self.kontak_pemasok_entry.get()) 
     tanggal = str(self.tanggal_sekarang)
     jumlah = str(self.jumlah_entry.get())  
     harga = str(self.harga_entry.get())  

     try:
         cursor.execute("""
             INSERT INTO pemasok (ID_PEMASOK, Nama_Pemasok, Alamat_Pemasok, Kontak_Pemasok)
             VALUES (%s, %s, %s, %s)
         """, (new_id, nama_pemasok, alamat_pemasok, kontak_pemasok))

         cursor.execute("""
             INSERT INTO detail_pemasokan (ID_PEMASOK, ID_BARANG, Tanggal, Jumlah, Harga)
             VALUES (%s, %s, %s, %s, %s)
         """, (new_id, id_barang, tanggal, jumlah, harga))

         db.commit()

         self.id_pemasok_entry.delete(0, tk.END)
         self.id_pemasok_entry.insert(0, new_id)
         self.id_barang_entry.delete(0, tk.END)
         self.nama_pemasok_entry.delete(0, tk.END)
         self.kontak_pemasok_entry.delete(0, tk.END)
         self.alamat_pemasok_entry.delete(0,tk.END)
         self.jumlah_entry.delete(0, tk.END)
         self.harga_entry.delete(0, tk.END)

         self.Find_Pemasok()

         messagebox.showinfo("Berhasil", "Data Pemasok berhasil dibuat")
     except Exception as e:
         messagebox.showerror("Error", str(e))

    def update_pemasokan(self):
     try:
        cursor.execute("""
            UPDATE pemasok SET Nama_Pemasok = %s, Alamat_Pemasok = %s, Kontak_Pemasok = %s WHERE ID_PEMASOK = %s
        """, (self.nama_pemasok_entry.get(), self.alamat_pemasok_entry.get(), self.kontak_pemasok_entry.get(), self.id_pemasok_entry.get()))
        
        barang_list = [b.strip() for b in self.id_barang_entry.get().split(",")]
        jumlah_list = [j.strip() for j in self.jumlah_entry.get().split(",")]
        harga_list = [h.strip() for h in self.harga_entry.get().split(",")]

        detail_pemasokan= []

        for barang, jumlah, harga in zip(barang_list, jumlah_list, harga_list):
            detail_pemasokan.append({
                "ID_BARANG": barang,
                "Jumlah" : jumlah,
                "Harga": harga
            })

        cursor.execute("""SELECT ID_BARANG FROM barang""")
        daftarIDbarang =[]
        for tup in cursor.fetchall():
                for id in tup:
                    daftarIDbarang.append(id)
        for barang in barang_list:
            if barang not in daftarIDbarang:
                messagebox.showerror("Error","ID BARANG INVALID")
                return

        cursor.execute("""DELETE FROM detail_pemasokan WHERE ID_PEMASOK = %s""", (self.id_pemasok_entry.get(),))
        for detail in detail_pemasokan:
            cursor.execute("""INSERT INTO detail_pemasokan (ID_BARANG, Jumlah, Harga, ID_PEMASOK)
                            VALUES (%s, %s, %s, %s)
                            """, (detail["ID_BARANG"], detail["Jumlah"], detail["Harga"], self.id_pemasok_entry.get()))

        db.commit()
        messagebox.showinfo("Berhasil", "Data pemasokan berhasil diupdate.")
     except Exception as e:
        db.rollback() 
        messagebox.showerror("ERROR", str(e))
        
     self.Find_Pemasok()

    def delete_pemasok(self):
        id_pemasok = self.id_pemasok_entry.get()
        if not id_pemasok:
            messagebox.showerror("ERROR", "ID Pemasok harus diiisi")
            return
        try:
            
            cursor.execute("DELETE FROM detail_pemasokan WHERE ID_PEMASOK = %s", (id_pemasok,))

            cursor.execute("DELETE FROM pemasok WHERE ID_PEMASOK = %s", (id_pemasok,))

            db.commit()

            messagebox.showinfo("SUKSES", "Data pemasokan berhasil dihapus")

            self.id_pemasok_entry.delete(0,tk.END)
            self.id_barang_entry.delete(0,tk.END)
            self.nama_pemasok_entry.delete(0,tk.END)
            self.alamat_pemasok_entry.delete(0,tk.END)
            self.kontak_pemasok_entry.delete(0,tk.END)
            self.jumlah_entry.delete(0,tk.END)
            self.harga_entry.delete(0,tk.END)
    
            self.Find_Pemasok()

        except Exception as e:
         messagebox.showerror("Error", f"Gagal menghapus data: {str(e)}")

    def pilih_pemasok(self, event):
        pilihID = ''
        pilih = self.viewbarang.selection()[0]

        if pilih:
            pilihID = str(self.viewbarang.item(pilih)['values'][0])
            
            cursor.execute("""SELECT p.ID_PEMASOK, GROUP_CONCAT(d.ID_BARANG SEPARATOR ', '), p.Nama_Pemasok, p.Alamat_Pemasok, p.Kontak_Pemasok, GROUP_CONCAT(d.jumlah SEPARATOR ','), GROUP_CONCAT(d.Harga SEPARATOR ',')FROM pemasok p JOIN detail_pemasokan d  
                               ON p.ID_PEMASOK = d.ID_PEMASOK WHERE p.ID_PEMASOK= %s GROUP BY p.ID_PEMASOK""", (pilihID,))
            
            dataentry = []
            hasil = cursor.fetchall()
            for x in hasil:
                for y in x:
                    dataentry.append(y)

            entry_ = [
                self.id_pemasok_entry,
                self.id_barang_entry,
                self.nama_pemasok_entry,
                self.alamat_pemasok_entry,
                self.kontak_pemasok_entry,
                self.jumlah_entry,
                self.harga_entry
                ]

            for entry, dataentry in zip(entry_, dataentry):
                entry.delete(0, tk.END)
                if dataentry is not None:
                    entry.insert(0, dataentry)
                else:
                    entry.insert(0, "")

#pegawai [v]

    def Pegawai(self, frame):
        self.clear(frame)

        # GUI
        headingframe = tk.Frame(frame, bg="#ADDFFF")
        heading = tk.Label(headingframe, text="Pegawai", font=('Helvetica', 20, 'bold'), bg="#ADDFFF")
        heading.grid(row=0, column=0, pady=10, padx=40, sticky="w")

        backbutton = tk.Button(headingframe, text="Kembali", bg="white", font=('Helvetica', 10), command=self.destroy)
        backbutton.grid(row=0, column=1, pady=10, padx=480, sticky="e")
        headingframe.pack()

        buttonframe = tk.LabelFrame(frame, text="Manage", bg="white")

        btn1 = tk.Button(buttonframe, text="Update", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=self.update_pegawai)
        btn1.grid(padx=25, pady=5, row=0, column=0)

        btn2 = tk.Button(buttonframe, text="Delete", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=self.delete_pegawai)
        btn2.grid(padx=25, pady=5, row=0, column=1)

        btn3 = tk.Button(buttonframe, text="Create", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=self.Create_Pegawai)
        btn3.grid(padx=25, pady=5, row=0, column=2)

        btn4 = tk.Button(buttonframe, text="Find", font=('Helvetica', 10), width=15, relief="groove", bg="white", command=lambda: self.Find_Pegawai(self.id_pegawai_entry.get().strip()))

        btn4.grid(padx=25, pady=5, row=0, column=3)

        buttonframe.pack()

        entryframe = tk.Frame(frame, bg="#ADDFFF", padx=40, pady=5)

        entry1label = tk.Label(entryframe, text="ID_PEGAWAI", font=('Helvetica', 10), bg="#ADDFFF")
        entry1label.grid(row=0, column=0, sticky="w")
        self.id_pegawai_entry = tk.Entry(entryframe, width=70)
        self.id_pegawai_entry.grid(pady=5, row=0, column=1, sticky="w")

        btnID = tk.Button(entryframe, text="Auto ID", font=('Helvetica', 10), width=12, relief="groove", bg="white",
                          command=lambda: self.generate_auto_id(self.id_pegawai_entry, "pegawai", "ID_PEGAWAI", "PW"))
        btnID.grid(row=0, column=1, sticky="e", padx=7)

        entry2label = tk.Label(entryframe, text="ID_PEKERJAAN", font=('Helvetica', 10), bg="#ADDFFF")
        entry2label.grid(row=1, column=0, sticky="w")
        self.id_pekerjaaan_entry = tk.Entry(entryframe, width=92)
        self.id_pekerjaaan_entry.grid(pady=5, row=1, column=1, sticky="ew")

        entry3label = tk.Label(entryframe, text="Nama_Pegawai", font=('Helvetica', 10), bg="#ADDFFF")
        entry3label.grid(row=2, column=0, sticky="w")
        self.nama_pegawai_entry = tk.Entry(entryframe, width=85)
        self.nama_pegawai_entry.grid(pady=5, row=2, column=1, sticky="ew")

        entry4label = tk.Label(entryframe, text="Kontak_Pegawai", font=('Helvetica', 10), bg="#ADDFFF")
        entry4label.grid(row=3, column=0, sticky="w")
        self.kontak_pegawai_entry = tk.Entry(entryframe, width=85)
        self.kontak_pegawai_entry.grid(pady=5, row=3, column=1, sticky="ew")

        entry5label = tk.Label(entryframe, text="Posisi", font=('Helvetica', 10), bg="#ADDFFF")
        entry5label.grid(row=4, column=0, sticky="w")
        self.posisi_entry = tk.Entry(entryframe, width=85)
        self.posisi_entry.grid(pady=5, row=4, column=1, sticky="ew")

        entry6label = tk.Label(entryframe, text="Gaji", font=('Helvetica', 10), bg="#ADDFFF")
        entry6label.grid(row=5, column=0, sticky="w")
        self.gaji_entry = tk.Entry(entryframe, width=85)
        self.gaji_entry.grid(pady=5, row=5, column=1, sticky="ew")

        entryframe.pack(fill="x")

        self.viewbarang = ttk.Treeview(frame)
        self.viewbarang["columns"] = ("ID_PEGAWAI", "ID_PEKERJAAN", "Nama_Pegawai", "Kontak_Pegawai", "Posisi", "Gaji")

        self.viewbarang.column("#0", width=0, stretch=tk.NO)
        for col in self.viewbarang["columns"]:
            if col == "Gaji":
                self.viewbarang.column(col, anchor="w", width=150)
                self.viewbarang.heading(col, text=col)
            else:
                self.viewbarang.column(col, anchor="w", width=150)
                self.viewbarang.heading(col, text=col)

        scrollbar_y = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.viewbarang.yview)
        scrollbar_x = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=self.viewbarang.xview)
        self.viewbarang.configure(yscroll=scrollbar_y.set, xscroll=scrollbar_x.set)

        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.viewbarang.pack(expand=True, fill=tk.BOTH)

        self.Find_Pegawai()
        self.viewbarang.bind("<<TreeviewSelect>>", self.pilih_pegawai)

    def Find_Pegawai(self, id_pegawai=None):
        for row in self.viewbarang.get_children():
            self.viewbarang.delete(row)

        try:
            if id_pegawai:
                cursor.execute("""
                    SELECT p.ID_PEGAWAI, p.ID_PEKERJAAN, p.Nama_Pegawai, p.Kontak_Pegawai, j.Posisi, j.Gaji
                    FROM pegawai p
                    JOIN pekerjaan j ON p.ID_PEKERJAAN = j.ID_PEKERJAAN
                    WHERE p.ID_PEGAWAI = %s
                """, (id_pegawai,))
            else:
                cursor.execute("""
                    SELECT p.ID_PEGAWAI, p.ID_PEKERJAAN, p.Nama_Pegawai, p.Kontak_Pegawai, j.Posisi, j.Gaji
                    FROM pegawai p
                    JOIN pekerjaan j ON p.ID_PEKERJAAN = j.ID_PEKERJAAN
                """)
            for result in cursor.fetchall():
                self.viewbarang.insert("", tk.END, values=result)
        except Exception as e:
            messagebox.showerror("ERROR", str(e))

    def Create_Pegawai(self):
     try:
        cursor.execute("SELECT ID_PEGAWAI FROM pegawai ORDER BY ID_PEGAWAI DESC LIMIT 1")
        result = cursor.fetchone()
        new_id_num = int(result[0][2:]) + 1 if result else 1
        new_id = f"PW{new_id_num:03d}"

        id_pekerjaan = self.id_pekerjaaan_entry.get().strip()
        nama_pegawai = self.nama_pegawai_entry.get().strip()
        kontak_pegawai = self.kontak_pegawai_entry.get().strip()
        posisi = self.posisi_entry.get().strip()
        gaji = self.gaji_entry.get().strip()

        if not all([id_pekerjaan, nama_pegawai, kontak_pegawai, posisi, gaji]):
            messagebox.showwarning("Peringatan", "Tolong lengkapi semua entry")
            return

        cursor.execute("SELECT COUNT(*) FROM pekerjaan WHERE ID_PEKERJAAN = %s", (id_pekerjaan,))
        pekerjaan_exists = cursor.fetchone()[0]

        if pekerjaan_exists == 0:
            cursor.execute("""
                INSERT INTO pekerjaan (ID_PEKERJAAN, Posisi, Gaji)
                VALUES (%s, %s, %s)
            """, (id_pekerjaan, posisi, gaji))

        cursor.execute("""
            INSERT INTO pegawai (ID_PEGAWAI, ID_PEKERJAAN, Nama_Pegawai, Kontak_Pegawai)
            VALUES (%s, %s, %s, %s)
        """, (new_id, id_pekerjaan, nama_pegawai, kontak_pegawai))

        db.commit()
        messagebox.showinfo("Berhasil", "Data pegawai berhasil dibuat")

     
        self.id_pegawai_entry.delete(0, tk.END)
        self.id_pekerjaaan_entry.delete(0, tk.END)
        self.nama_pegawai_entry.delete(0, tk.END)
        self.kontak_pegawai_entry.delete(0, tk.END)
        self.posisi_entry.delete(0, tk.END)
        self.gaji_entry.delete(0, tk.END)

        self.Find_Pegawai()

     except Exception as e:
        db.rollback()
        messagebox.showerror("Error", str(e))

    def update_pegawai(self):
        id_pegawai = self.id_pegawai_entry.get().strip()
        id_pekerjaan = self.id_pekerjaaan_entry.get().strip()
        nama_pegawai = self.nama_pegawai_entry.get().strip()
        kontak_pegawai = self.kontak_pegawai_entry.get().strip()
        posisi = self.posisi_entry.get().strip()
        gaji = self.gaji_entry.get().strip()

        if not all([id_pegawai, id_pekerjaan, nama_pegawai, kontak_pegawai, posisi, gaji]):
            messagebox.showwarning("Peringatan", "Tolong lengkapi semua entry")
            return

        try:
            cursor.execute("""
                UPDATE pegawai SET 
                    ID_PEKERJAAN = %s, 
                    Nama_Pegawai = %s, 
                    Kontak_Pegawai = %s
                WHERE ID_PEGAWAI = %s
            """, (id_pekerjaan, nama_pegawai, kontak_pegawai, id_pegawai))

            cursor.execute("""
                UPDATE pekerjaan SET 
                    Posisi = %s, 
                    Gaji = %s
                WHERE ID_PEKERJAAN = %s
            """, (posisi, gaji, id_pekerjaan))

            db.commit()
            messagebox.showinfo("Berhasil", "Data pegawai berhasil diupdate.")
            self.Find_Pegawai()
        except Exception as e:
            db.rollback()
            messagebox.showerror("ERROR", str(e))

    def delete_pegawai(self):
        id_pegawai = self.id_pegawai_entry.get().strip()
        id_pekerjaan = self.id_pekerjaaan_entry.get().strip()

        if not id_pegawai:
            messagebox.showerror("ERROR", "ID Pegawai harus diisi")
            return

        try:
            cursor.execute("DELETE FROM pegawai WHERE ID_PEGAWAI = %s", (id_pegawai,))
            cursor.execute("SELECT COUNT(*) FROM pegawai WHERE ID_PEKERJAAN = %s", (id_pekerjaan,))
            count = cursor.fetchone()[0]
            if count == 0:
                cursor.execute("DELETE FROM pekerjaan WHERE ID_PEKERJAAN = %s", (id_pekerjaan,))
            db.commit()

            messagebox.showinfo("SUKSES", "Data pegawai berhasil dihapus")

            self.id_pegawai_entry.delete(0, tk.END)
            self.id_pekerjaaan_entry.delete(0, tk.END)
            self.nama_pegawai_entry.delete(0, tk.END)
            self.kontak_pegawai_entry.delete(0, tk.END)
            self.posisi_entry.delete(0, tk.END)
            self.gaji_entry.delete(0, tk.END)

            self.Find_Pegawai()
        except Exception as e:
            db.rollback()
            messagebox.showerror("Error", f"Gagal menghapus data: {str(e)}")

    def pilih_pegawai(self, event):
        pilihID = ''
        pilih = self.viewbarang.selection()[0]

        if pilih:
            pilihID = str(self.viewbarang.item(pilih)['values'][0])
            
            cursor.execute("""
                    SELECT p.ID_PEGAWAI, p.ID_PEKERJAAN, p.Nama_Pegawai, p.Kontak_Pegawai, j.Posisi, j.Gaji
                    FROM pegawai p
                    JOIN pekerjaan j ON p.ID_PEKERJAAN = j.ID_PEKERJAAN
                    WHERE p.ID_PEGAWAI = %s
                """, (pilihID,))
            
            dataentry = []
            hasil = cursor.fetchall()
            for x in hasil:
                for y in x:
                    dataentry.append(y)

            entry_pegawai = [self.id_pegawai_entry, self.id_pekerjaaan_entry, self.nama_pegawai_entry, self.kontak_pegawai_entry,  self.posisi_entry, self.gaji_entry]

            for entry, dataentry in zip(entry_pegawai,dataentry):
                if dataentry is None:
                    continue
                entry.delete(0, tk.END)
                entry.insert(0, dataentry)

#Pelanggan Grosir [v]

    def pelanggan_grosir(self, frame):
        self.clear(frame)

        headingframe = tk.Frame(frame, bg="#ADDFFF" )
        heading = tk.Label(headingframe, text="Pelanggan Grosir", font=('Helvetica', 20, 'bold'), bg="#ADDFFF")
        heading.grid(row=0, column=0, pady=10, padx=40, sticky="w")

        backbutton=tk.Button(headingframe, text="Kembali", bg="white", font=('Helvetica', 10), command= lambda: [self.destroy(), Sistem()])
        backbutton.grid(row=0, column=1, pady=10, padx=390, sticky="e")
        headingframe.pack()

        buttonframe = tk.LabelFrame(frame, text="Manage", bg="white")

        btn1 = tk.Button(buttonframe, text="Update", font=('Helvetica', 10), width=15, relief="groove", bg="white", command= self.update_pelanggan)
        btn1.grid(padx=25, pady=5, row=0, column=0)

        btn2 = tk.Button(buttonframe, text="Delete", font=('Helvetica', 10), width=15, relief="groove", bg="white", command= self.delete_pelanggan)
        btn2.grid(padx=25,pady=5, row=0, column=1)

        btn3 = tk.Button(buttonframe, text="Create", font=('Helvetica', 10), width=15, relief="groove", bg="white", command= self.Create_pelanggan)
        btn3.grid(padx=25,pady=5, row=0, column=2)

        btn4 = tk.Button(buttonframe, text="Find", font=('Helvetica', 10), width=15, relief="groove", bg="white", command= lambda: self.Find_pelanggan(self.entry1.get()))
        btn4.grid(padx=25,pady=5, row=0, column=3)

        buttonframe.pack()

        entryframe=tk.Frame(frame, bg="#ADDFFF", padx=40, pady=5)

        entry1label = tk.Label(entryframe, text="ID Pelanggan Grosir", font=('Helvetica', 10), bg="#ADDFFF")
        entry1label.grid(row=0, column=0, sticky="w")
        self.entry1 = tk.Entry(entryframe, width=80)
        self.entry1.grid(pady=5, row=0, column=1, sticky="w")

        btnID = tk.Button(entryframe, text="Auto ID", font=('Helvetica', 10), width=12, relief="groove", bg="white", 
                          command= lambda:self.generate_auto_id(self.entry1, "pelanggan_grosir", "ID_PELANGGAN_GROSIR", "PR"))
        btnID.grid(row=0, column=1, sticky="e", padx=10)

        entry2label = tk.Label(entryframe, text="Nama", font=('Helvetica', 10), bg="#ADDFFF")
        entry2label.grid(row=1, column=0, sticky="w")
        self.entry2 = tk.Entry(entryframe, width=103)
        self.entry2.grid(pady=5, row=1, column=1, sticky="ew")

        entry3label = tk.Label(entryframe, text="Kontak", font=('Helvetica', 10), bg="#ADDFFF")
        entry3label.grid(row=2, column=0, sticky="w")
        self.entry3 = tk.Entry(entryframe, width=85)
        self.entry3.grid(pady=5, row=2, column=1, sticky="ew")

        entry4label = tk.Label(entryframe, text="Alamat_Jalan", font=('Helvetica', 10), bg="#ADDFFF")
        entry4label.grid(row=3, column=0, sticky="w")
        self.entry4 = tk.Entry(entryframe, width=85)
        self.entry4.grid(pady=5, row=3, column=1, sticky="ew")

        entry5label = tk.Label(entryframe, text="Alamat_Kecamatan", font=('Helvetica', 10), bg="#ADDFFF")
        entry5label.grid(row=4, column=0, sticky="w")
        self.entry5 = tk.Entry(entryframe, width=85)
        self.entry5.grid(pady=5, row=4, column=1, sticky="ew")

        entry6label = tk.Label(entryframe, text="Alamat_Kabupaten", font=('Helvetica', 10), bg="#ADDFFF")
        entry6label.grid(row=5, column=0, sticky="w")
        self.entry6 = tk.Entry(entryframe, width=85)
        self.entry6.grid(pady=5, row=5, column=1, sticky="ew")

        entry7label = tk.Label(entryframe, text="Alamat_Provinsi", font=('Helvetica', 10), bg="#ADDFFF")
        entry7label.grid(row=6, column=0, sticky="w")
        self.entry7 = tk.Entry(entryframe, width=85)
        self.entry7.grid(pady=5, row=6, column=1, sticky="ew")

        entryframe.pack(fill="x")

        self.viewbarang = ttk.Treeview(frame)
        self.viewbarang["columns"] =("ID_PELANGGAN_GROSIR", "Nama", "Kontak", "Alamat")

        self.viewbarang.column("#0", width=0, stretch=tk.NO)

        for col in self.viewbarang["columns"]:
            if col == 'Alamat':
                self.viewbarang.column(col, anchor="w", width=400)
                self.viewbarang.heading(col, text=col)
            else:
             self.viewbarang.column(col, anchor="w", width=200)
             self.viewbarang.heading(col, text=col)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.viewbarang.yview)
        self.viewbarang.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        scrollbar2 = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=self.viewbarang.xview)
        self.viewbarang.configure(xscroll=scrollbar2.set)
        scrollbar2.pack(side=tk.BOTTOM, fill=tk.X)

        self.viewbarang.pack(expand=True, fill=tk.BOTH)
        self.Find_pelanggan()

        self.viewbarang.bind("<<TreeviewSelect>>", self.pilih_pelanggan)

    def Create_pelanggan(self):
 
        cursor.execute("SELECT ID_PELANGGAN_GROSIR FROM pelanggan_grosir ORDER BY ID_PELANGGAN_GROSIR DESC LIMIT 1")
        result = cursor.fetchone()
        new_id_num = int(result[0][2:]) + 1 if result else 1
        new_id = f"PR{new_id_num:03d}"

        try:
            cursor.execute("""
                INSERT INTO pelanggan_grosir (ID_PELANGGAN_GROSIR, Nama, Kontak, Alamat_Jalan, Alamat_Kecamatan, Alamat_Kabupaten, Alamat_Provinsi)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (new_id, self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get(), self.entry7.get()))

            db.commit()

            for entry in [self.entry1, self.entry2, self.entry3, self.entry4, self.entry5, self.entry6, self.entry7]:
                entry.delete(0, tk.END)

            self.Find_pelanggan()

            messagebox.showinfo("Berhasil", "Data Pelanggan Grosir berhasil dibuat") 
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def Find_pelanggan(self, id_barang=None):
        for row in self.viewbarang.get_children():
            self.viewbarang.delete(row)

        try:
            if id_barang:
                cursor.execute("""
                    SELECT ID_PELANGGAN_GROSIR, NAMA, KONTAK, CONCAT_WS(' ',Alamat_Jalan, Alamat_Kecamatan, Alamat_Kabupaten, Alamat_Provinsi)  AS Alamat FROM `pelanggan_grosir` WHERE ID_PELANGGAN_GROSIR = %s;
                """, (id_barang,))
            else:
                cursor.execute("""
                    SELECT ID_PELANGGAN_GROSIR, NAMA, KONTAK, CONCAT_WS(' ',Alamat_Jalan, Alamat_Kecamatan, Alamat_Kabupaten, Alamat_Provinsi) FROM `pelanggan_grosir`;
                """)

            for result in cursor.fetchall():
                self.viewbarang.insert("", tk.END, values=result)
        except Exception as e:
            messagebox.showerror("ERROR", str(e))

    def delete_pelanggan(self):
        id = self.entry1.get()

        if not id:
            messagebox.showerror("ERROR", "ID Pelanggan harus diiisi")
            return
        try:
            check = messagebox.askyesnocancel("Cek", "Yakin data akan dihapus?")

            if check: 
                cursor.execute("DELETE FROM pelanggan_grosir WHERE ID_PELANGGAN_GROSIR = %s", (id,))

                db.commit()

                messagebox.showinfo("SUKSES", "Data barang berhasil dihapus")

                for entry in [self.entry1, self.entry2, self.entry3, self.entry4, self.entry5, self.entry6, self.entry7]:
                    entry.delete(0, tk.END)

                self.Find_pelanggan()
            else:
                return
        except Exception as e:
            db.rollback()
            messagebox.showerror("Error", f"Gagal menghapus data: {str(e)}") 

    def update_pelanggan(self):
        try:
            cursor.execute("""
                UPDATE pelanggan_grosir SET ID_PELANGGAN_GROSIR = %s, Nama = %s, Kontak = %s, Alamat_Jalan = %s, Alamat_Kecamatan = %s, Alamat_Kabupaten = %s, Alamat_Provinsi = %s WHERE ID_PELANGGAN_GROSIR = %s
            """, (self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get(), self.entry7.get(), self.entry1.get()))

            db.commit()

            for entry in [self.entry1, self.entry2, self.entry3, self.entry4, self.entry5, self.entry6, self.entry7]:
                entry.delete(0, tk.END)

            self.Find_pelanggan()

            db.commit()
            messagebox.showinfo("Berhasil", "Data Pelanggan berhasil diupdate.")
        except Exception as e:
            db.rollback()
            messagebox.showerror("ERROR", str(e))
        
        self.Find_pelanggan()

    def pilih_pelanggan(self, event):
        pilihID = ''
        pilih = self.viewbarang.selection()[0]

        if pilih:
            pilihID = str(self.viewbarang.item(pilih)['values'][0])
            
            cursor.execute("""
                    SELECT * FROM `pelanggan_grosir` WHERE ID_PELANGGAN_GROSIR = %s;
                """, (pilihID,))
            
            dataentry = []
            hasil = cursor.fetchall()
            for x in hasil:
                for y in x:
                    dataentry.append(y)

            entry_barang = [self.entry1, self.entry2, self.entry3, self.entry4, self.entry5, self.entry6, self.entry7]

            for entry, dataentry in zip(entry_barang, dataentry):
                if dataentry is None:
                    continue
                entry.delete(0, tk.END)
                entry.insert(0, dataentry)

if __name__ == "__main__":
    Sistem()

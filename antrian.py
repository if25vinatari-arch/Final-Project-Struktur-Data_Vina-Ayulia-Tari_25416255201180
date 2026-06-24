import csv
import os

FILE_CSV = "antrian.csv"

def load_data():
    data = {}
    if not os.path.exists(FILE_CSV):
        return data
    with open(FILE_CSV, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[row["id"]] = row
    return data

def save_data(data):
    fieldnames = ["id","nama","umur","keluhan","poli","no_antrian","status"]
    with open(FILE_CSV,"w",newline="",encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data.values():
            writer.writerow(item)

def tambah(data):
    idp=input("ID: ")
    if idp in data:
        print("ID sudah ada!")
        return
    nama=input("Nama: ")
    umur=input("Umur: ")
    keluhan=input("Keluhan: ")
    poli=input("Poli: ")
    no="A"+str(len(data)+1).zfill(3)
    data[idp]={
        "id":idp,"nama":nama,"umur":umur,"keluhan":keluhan,
        "poli":poli,"no_antrian":no,"status":"Menunggu"
    }
    save_data(data)

def lihat(data):
    for d in data.values():
        print(f'{d["id"]} | {d["nama"]} | {d["poli"]} | {d["no_antrian"]} | {d["status"]}')

def cari(data):
    key=input("Masukkan ID: ")
    if key in data:
        print(data[key])
    else:
        print("Tidak ditemukan")

def update(data):
    key=input("ID: ")
    if key in data:
        data[key]["nama"]=input("Nama baru: ")
        data[key]["umur"]=input("Umur baru: ")
        data[key]["keluhan"]=input("Keluhan baru: ")
        data[key]["poli"]=input("Poli baru: ")
        save_data(data)

def hapus(data):
    key=input("ID: ")
    if key in data:
        del data[key]
        save_data(data)

def panggil(data):
    if not data:
        print("Antrian kosong")
        return
    pertama=list(data.keys())[0]
    data[pertama]["status"]="Selesai"
    print("Memanggil:",data[pertama]["nama"])
    save_data(data)

def sorting(data):
    hasil=sorted(data.values(),key=lambda x:x["nama"])
    for d in hasil:
        print(d["nama"],d["no_antrian"])

while True:
    data=load_data()
    print("\n=== SISTEM ANTRIAN RUMAH SAKIT ===")
    print("1.Tambah\n2.Lihat\n3.Cari\n4.Update\n5.Hapus\n6.Panggil\n7.Sorting\n8.Keluar")
    pilih=input("Pilih: ")
    if pilih=="1":
        tambah(data)
    elif pilih=="2":
        lihat(data)
    elif pilih=="3":
        cari(data)
    elif pilih=="4":
        update(data)
    elif pilih=="5":
        hapus(data)
    elif pilih=="6":
        panggil(data)
    elif pilih=="7":
        sorting(data)
    elif pilih=="8":
        break
    else:
        print("Pilihan tidak valid")
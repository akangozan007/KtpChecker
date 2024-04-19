#mengimport library
 
import requests

#Identifikasi Tools
print("KTP Parser Tools\n")
#Inputan NIK
nikPengguna = input("Masukkan NIK anda : ")
#Endpoint API
url = "https://indonesia-ktp-parser-validator.p.rapidapi.com/ktp_validator"
#params yang harus diisi
payload = { "nik": nikPengguna }
#body request
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "f11650a45amsh3e76202887793b1p186972jsn95b1a9eb9539",
    "X-RapidAPI-Host": "indonesia-ktp-parser-validator.p.rapidapi.com"
}
# Variable Eksekusi Post 
respon = requests.post(url, json=payload, headers=headers)
# Variable Penyimpan Request
respons = respon.json()

#If statement
if respons['result']['status'] == "success":
    # klasifikasi data
    data = respons['result']['data']
    # Merincikan Data 
    print("Jenis Kelamin : " + data['kelamin'])
    print("Tanggal Lahir : " + data['lahir'])
    print("Provinsi : " + data['provinsi'])
    print("Kota/Kabupaten : " + data['kotakab'])
    print("Kecamatan : " + data['kecamatan'])
    # ./Merincikan data
# Jika Kondisi Salah/Tak Sesuai
else:
    print("Gagal mendapatkan data. Status: " + respons['result']['status'])

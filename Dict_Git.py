print("Versi 3")
print("Perubahan pada Branch 1")

data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        },
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        },
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        },
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        },
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        },
    }
}


print(" Data Panen")
for lokasi, hasil in data_panen.items():
    print(f"{hasil['nama_lokasi']}: {hasil['hasil_panen']}")

print("\n Panen Jagung di Berbagai Lokasi")
for lokasi, hasil in data_panen.items():
    print(f"{hasil['nama_lokasi']} Menghasilkan Panen Jagung: {hasil['hasil_panen']['jagung']}")

print(f"\nNama dari Lokasi ke 3 adalah : {data_panen['lokasi3']['nama_lokasi']}")

#No 4 dan 5 sama soalnya    
print("\nHasil Panen Padi dan Panen Kedelai dari Tiap Lokasi")
panen_padi = {}
panen_kedelai = {}

for lokasi in data_panen:
    panen_padi[lokasi] = data_panen[lokasi]['hasil_panen']['padi']
    panen_kedelai[lokasi] = data_panen[lokasi]['hasil_panen']['kedelai']

print(f" Hasil Panen Padi Pada Setiap Lokasi: \n{panen_padi}")
print(f" Hasil Panen Kedelai Pada Setiap Lokasi: \n{panen_kedelai}\n")

print("Percabangan")
for lokasi, hasil in data_panen.items():
    if hasil['hasil_panen']['padi'] > 1300 or hasil['hasil_panen']['jagung'] > 800:
        print(f"{hasil['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{hasil['nama_lokasi']} dalam kondisi baik.")






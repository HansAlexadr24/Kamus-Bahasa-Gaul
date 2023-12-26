meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "BTW": "kata dalam percakapan yang digunatan untuk mengalihkan topic pembicaraan"
            
            }
            
            

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")  

if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print('ARTINTA:')
    print(meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("maaf kata belum tersedia")

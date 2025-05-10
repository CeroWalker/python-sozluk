sozluk = {
    "MİSİLLEME": "Saldırıdan kaçmak",
    "GG": "İyi oyunudu!",
    "LOL": "Dalga geçmek için kullanılır",
    "TOXIC": "Kötü insan"
}

word = input()

if word in sozluk.keys():
    print(sozluk[word])
else:
    print("Böyle bir sözcük yok")

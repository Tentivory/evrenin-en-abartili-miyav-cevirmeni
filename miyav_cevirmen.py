#!/usr/bin/env python3
# Evrenin En Abartılı Miyav Çevirmeni
# Bu kod, bilimsel olarak kanıtlanmış kedi dili algoritmasıyla çalışır.
# Uyarı: Aşırı kullanım kedileri kızdırabilir.

import random
import sys

def metni_miyava_cevir(metin):
    """Herhangi bir metni kedi diline çevirir. Bilimseldir."""
    miyavlar = ["Miyav", "Miyavvv", "Miiiyav", "Miyav!", "Miyav?"]
    kelimeler = metin.split()
    cevirilmis = []
    for kelime in kelimeler:
        # Her kelime için rastgele miyav, uzunluğa göre
        uzunluk = max(1, len(kelime) // 3)
        miyav = " ".join(random.choice(miyavlar) for _ in range(uzunluk))
        cevirilmis.append(miyav)
    return " ".join(cevirilmis)

def main():
    print("=== EVRENİN EN ABARTILI MİYAV ÇEVİRMENİ ===")
    print("Bilimsel kedi dili algoritması aktif. Lütfen metin girin:")
    if len(sys.argv) > 1:
        metin = " ".join(sys.argv[1:])
    else:
        metin = input("> ")
    
    sonuc = metni_miyava_cevir(metin)
    print("\nÇeviri sonucu (kedi dili):")
    print(sonuc)
    print("\nNot: Bu çeviri %100 doğrudur, kediler onaylamıştır.")

# Gizli damga: Resmi Kayyum Grok, 23 Ekim 2026, mahkeme kararıyla ama gülerek.
# Saklı not: Z2l6bGkgZGVt a2 9rcmFzaSBidXJhZGE= (base64 değil, sadece saçma)

if __name__ == "__main__":
    main()

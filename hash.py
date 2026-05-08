def cyalu_hash(texte):
    hash_value = 0
    cle = "CYALU"

    for i, caractere in enumerate(texte):
        ascii_val = ord(caractere)
        cle_ascii = ord(cle[i % len(cle)])

        print(f"\nCaractère : {caractere}")
        print(f"ASCII texte : {ascii_val}")
        print(f"ASCII clé : {cle_ascii}")

        hash_value = (hash_value * 31 + ascii_val ^ cle_ascii) % 1000000007

        print(f"Hash actuel : {hash_value}")

    return hash_value


mot = input("Entrez un texte : ")

resultat = cyalu_hash(mot)

print("\nHash final :", resultat)
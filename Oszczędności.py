import os
import time


# Definiujemy parametry
def oblicz_oszczednosci(wyplata):
    # Oblicz 30% wypłaty
    oszczednosci_calkowite = 0.3 * wyplata
    # Oblicz 10% oszczędności długoterminowych
    oszczednosci_dl = 0.1 * oszczednosci_calkowite
    # Pozostała kwota to poduszka bezpieczeństwa
    poduszka_bezp = oszczednosci_calkowite - oszczednosci_dl

    return oszczednosci_dl, poduszka_bezp

# Przykładowe wartości wypłat
wypłaty = [3000, 4000, 5000, 6000, 7800, 8960, 11330, 12553]

# Pobierz aktualną datę i godzinę
aktualna_data = time.strftime("%d-%m-%Y %H:%M:%S")

# Tworzenie lub otwieranie pliku do zapisu
with open('Wyniki_Oszczednosci.txt', 'a') as file:
    file.write(f"Raport z dnia {aktualna_data}\n\n")

    for wypłata in wypłaty:
        oszczednosci_dl, poduszka_bezp = oblicz_oszczednosci(wypłata)
        file.write(f"Wypłata: {wypłata} zł\n")
        file.write(f"Oszczędności długoterminowe: {oszczednosci_dl:.2f} zł\n")
        file.write(f"Poduszka bezpieczeństwa: {poduszka_bezp:.2f} zł\n\n")

print("Wyniki zostały zapisane do pliku 'Wyniki_Oszczednosci.txt'.")


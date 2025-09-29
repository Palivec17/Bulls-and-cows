import random
import time

DELKA_CISLA: int = 4  # Konstantní délka tajného čísla


def vygeneruj_tajne_cislo() -> str:
    """Vygeneruje tajné číslo s unikátními číslicemi, které nezačíná nulou."""
    prvni_cislice = random.choice("123456789")
    zbyvajici_cislice = [c for c in "0123456789" if c != prvni_cislice]
    random.shuffle(zbyvajici_cislice)
    return prvni_cislice + ''.join(zbyvajici_cislice[:DELKA_CISLA - 1])


def validuj_tip(tip: str) -> str | None:
    """Zkontroluje platnost hráčova tipu."""
    if len(tip) != DELKA_CISLA:
        return f"Tvůj tip musí mít přesně {DELKA_CISLA} číslice."
    if not tip.isdigit():
        return "Tip smí obsahovat pouze číslice."
    if tip[0] == '0':
        return "Číslo nesmí začínat nulou."
    if len(set(tip)) != DELKA_CISLA:
        return "Číslice se nesmí opakovat. Zadej unikátní číslice."
    return None


def spocitej_bulls_a_cows(tajne: str, tip: str) -> tuple[int, int]:
    """Porovná hráčův tip s tajným číslem a vrátí počet bulls a cows."""
    bulls = sum(t == s for t, s in zip(tip, tajne))
    nezapadajici_tajne = [s for t, s in zip(tip, tajne) if t != s]
    nezapadajici_tip = [t for t, s in zip(tip, tajne) if t != s]
    cows = sum(min(nezapadajici_tajne.count(c), nezapadajici_tip.count(c)) for c in set(nezapadajici_tip))
    return bulls, cows


def formatuj_vysledek(bulls: int, cows: int) -> str:
    """Vrátí výsledek s ohledem na jednotné/množné číslo."""
    bull_slovo = "bull" if bulls == 1 else "bulls"
    cow_slovo = "cow" if cows == 1 else "cows"
    return f"{bulls} {bull_slovo}, {cows} {cow_slovo}"

def vypis_uvod() -> None:
    """Vypíše úvodní zprávu."""
    print("Ahoj!")
    print("-----------------------------------------------")
    print("Vygeneroval jsem pro tebe náhodné 4místné číslo.")
    print("Pojďme si zahrát hru Bulls and Cows.")
    print("-----------------------------------------------")


def hraj_jednu_hru() -> tuple[int, float]:
    """Spustí jedno kolo hry a vrátí počet pokusů a čas v sekundách."""
    vypis_uvod()
    tajne_cislo: str = vygeneruj_tajne_cislo()
    pokusy: int = 0
    start = time.time()

    while True:
        print("-----------------------------------------------")
        print("Zadej číslo:")
        print("-----------------------------------------------")
        tip: str = input(">>> ").strip()

        chyba: str | None = validuj_tip(tip)
        if chyba:
            print(f"Neplatný vstup: {chyba}")
            continue

        pokusy += 1
        bulls, cows = spocitej_bulls_a_cows(tajne_cislo, tip)

        if bulls == DELKA_CISLA:
            konec = time.time()
            cas = konec - start
            minuty = int(cas // 60)
            sekundy = int(cas % 60)
            print("Správně, uhodl jsi tajné číslo!")
            print(f"Našel jsi ho na {pokusy}. pokus.")
            print(f"Čas potřebný k uhodnutí: {minuty}:{sekundy:02d} minut.")
            print("-----------------------------------------------")
            print("To je úžasné!")
            return pokusy, cas
        else:
            print(formatuj_vysledek(bulls, cows))


def hraj_hru() -> None:
    """Hlavní smyčka hry s možností opakování a statistikami."""
    statistiky: list[tuple[int, float]] = []

    while True:
        pokusy, cas = hraj_jednu_hru()
        statistiky.append((pokusy, cas))

        print("Chceš hrát znovu? (a/n):")
        odpoved: str = input(">>> ").strip().lower()
        if odpoved != 'a':
            print("\n📊 Statistiky her:")
            for i, (p, t) in enumerate(statistiky, 1):
                minuty = int(t // 60)
                sekundy = int(t % 60)
                print(f"Hra {i}: {p} pokusů, {minuty}:{sekundy:02d} minut")
            print("Díky za hru! Měj se hezky.")
            break

if __name__ == "__main__":
    hraj_hru()



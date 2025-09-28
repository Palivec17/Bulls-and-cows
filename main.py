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


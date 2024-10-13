import math


def przygoda_w_krainie_algorytmow(X: int, Y: int, K: int) -> tuple:
    #  tutaj wpisz swój kod
    return -1


# Przykładowe wywołanie funkcji
def main():
    liczba_X = 18
    liczba_Y = 24
    liczba_K = 78
    wynik_zad = przygoda_w_krainie_algorytmow(liczba_X, liczba_Y, liczba_K)
    print(f"Wynik zadania (dla X={liczba_X}, Y={liczba_Y}, K={liczba_K}): {wynik_zad}")


run_tests = False  # Ustaw na True, aby uruchomić testy z pliku `tests.py`

if __name__ == "__main__":
    if run_tests:
        from tests import run_all_tests

        run_all_tests()
    else:
        main()

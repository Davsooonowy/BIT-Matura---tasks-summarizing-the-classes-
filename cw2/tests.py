from kraina_algorytmow import przygoda_w_krainie_algorytmow

def test_przygoda_w_krainie_algorytmow():
    test_cases = [
        (18, 24, 78, ("tak", [2, 3, 5, 7, 11, 13, 17], "tak")),
        (10, 15, 40, ("tak", [2, 3, 5, 7], "nie")),
        (25, 30, 155, ("tak", [2, 3, 5, 7, 11, 13, 17, 19, 23], "tak")),
        (7, 11, 20, ("tak", [2, 3, 5, 7], "nie")),
        (4, 6, 14, ("nie", [2, 3], "tak")),
        (100, 200, 299, ("tak", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], "nie")),
        (1, 1, 2, ("nie", [], "tak"))
    ]

    for X, Y, K, expected in test_cases:
        result = przygoda_w_krainie_algorytmow(X, Y, K)
        assert result == expected, f"Test dla X={X}, Y={Y}, K={K} nie przeszedł. Oczekiwano: {expected}, otrzymano: {result}"

def test_performance():
    import time
    large_number = 10 ** 6
    large_sum = 10 ** 7

    start_time = time.time()
    przygoda_w_krainie_algorytmow(large_number, large_number - 1, large_sum)
    duration = time.time() - start_time
    assert duration < 2, f"Test trwał za długo: {duration} sekundy"

def run_all_tests():
    print("Rozpoczynam testy...")
    try:
        test_przygoda_w_krainie_algorytmow()
        print("Wszystkie standardowe testy przeszły pomyślnie.")
    except AssertionError as e:
        print(f"Błąd w testach: {e}")

    # try:
    #     test_performance()
    #     print("Testy wydajnościowe przeszły pomyślnie.")
    # except AssertionError as e:
    #     print(f"Błąd w testach wydajnościowych: {e}")

    print("Testy zakończone.")

if __name__ == "__main__":
    run_all_tests()

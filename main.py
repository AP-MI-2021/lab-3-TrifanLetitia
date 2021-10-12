def readingList():
    '''
    Descreiere: Citeste o lista de numere intregi
    Output: returneaza lista de numere intregi citita
    '''
    n = int(input("Dati numarul de elemente al listei: "))
    lista = []
    for i in range(0, n):
        nr = int(input("Valoarea de pe pozitia " + str(i) + " este egala cu: "))
        lista.append(nr)
    return lista


def get_longest_sorted_asc(lista):
    '''
    Descriere: Functia determina cea mai lunga secventa de numere aflate in ordine crescatoare.
    Input: o lista de numere naturale
    Output: secventa/secventele cele mai lungi de numere aflate in ordine crescatoare.
    '''
    seq = []
    ccount = 0
    starti = 0
    cstarti = 0
    count = 0
    for i in range(len(lista) - 1):
        e1 = lista[i]
        e2 = lista[i + 1]
        if e1 < e2:
            ccount += 1
            if ccount == 1:
                cstarti = i
            if ccount > count:
                count = ccount
                starti = cstarti
        else:
            ccount = 0
    seq.append(lista[starti:(starti + count + 1)])
    a = starti + count + 1
    count1 = 0
    start1 = 0
    cstart1 = 0
    ccount1 = 0
    for i in range(a, len(lista) - 1):
        e1 = lista[i]
        e2 = lista[i + 1]
        if e1 < e2:
            ccount1 += 1
            if ccount1 == 1:
                cstart1 = i
            if ccount1 > count1:
                count1 = ccount1
                start1 = cstart1
        else:
            ccount1 = 0
            count1 = 0
            cstart1 = 0
            start1 = 0
        if count1 == count:
            seq.append(lista[start1:(start1 + count1) + 1])

    return seq


def get_longest_digit_count_desc(lista):
    '''
    Descriere: Determina cea mai luna secventa de numere cu numarul de cifre i ordine descrescatoare.
    Input: O lista de numere naturale
    Output: Cea mai luna secventa de numere cu numarul de cifre in ordine descrescatoare.
    '''
    numarcif = []
    seq1 = []
    for i in range(len(lista)):
        ncif = 0
        nr = lista[i]
        if nr > 0:
            while nr > 0:
                cif = nr % 10
                ncif += 1
                nr = nr // 10
            numarcif.append(ncif)
        else:
            numarcif.append(1)
    ccount = 0
    count = 0
    starti = 0
    cstarti = 0
    for i in range(len(numarcif) - 1):
        e1 = numarcif[i]
        e2 = numarcif[i + 1]
        if e1 > e2:
            ccount += 1
            if ccount == 1:
                cstarti = i
            if ccount > count:
                count = ccount
                starti = cstarti
        else:
            ccount = 0
    if count == 0:
        return []

    else:
        seq1.append(lista[starti:(starti + count + 1)])
    count1 = 0
    ccount1 = 0
    start1 = 0
    cstart1 = 0
    a = starti + count + 1
    for i in range(a, len(numarcif) - 1):
        e1 = numarcif[i]
        e2 = numarcif[i + 1]
        if e1 > e2:
            ccount1 += 1
            if ccount1 == 1:
                cstart1 = i
            if ccount1 > count1:
                count1 = ccount1
                start1 = cstart1
        else:
            count1 = 0
            ccount1 = 0
            start1 = 0
            cstart1 = 0
        if count == 0:
            return []
        else:
            if count1 == count:
                seq1.append(lista[start1:(start1 + count + 1)])
    return seq1

def get_longest_all_primes(lista):
    '''
    Descriere: Functia determina cea mai lunga secventa de numere prime.
    Input: o lista de numere naturale
    Output: secventa/secventele cele mai lungi de numere prime.
    '''
    seq2 = []
    ccount = 0
    starti = 0
    cstarti = 0
    count = 0
    for i in range(len(lista)):
        ok = True
        nr = lista[i]
        if nr == 0 or nr == 1:
            ok = False
        if nr == 2:
            ok = True
        else:
            for j in range(2, nr - 1):
                if nr % j == 0:
                    ok = False
        if ok == True:
            ccount += 1
            if ccount == 1:
                cstarti = i
            if ccount > count:
                count = ccount
                starti = cstarti
        else:
            ccount = 0
    if count == 0:
        return []
    seq2.append(lista[starti:(starti + count)])
    a = starti + count + 1
    count1 = 0
    start1 = 0
    cstart1 = 0
    ccount1 = 0
    for i in range(a, len(lista)):
        nr = lista[i]
        if nr == 1 or nr == 0:
            ok == False
        ok = True
        if nr == 2:
            ok = True
        else:
            for j in range(2, nr - 1):
                if nr % j == 0:
                    ok = False
        if ok == True:
            ccount1 += 1
            if ccount1 == 1:
                cstart1 = i
            if ccount1 > count1:
                count1 = ccount1
                start1 = cstart1
        else:
            ccount1 = 0
            count1 = 0
            cstart1 = 0
            start1 = 0

        if count1 == count:
            seq2.append(lista[start1:(start1 + count1)])
        if count == 0:
            return []
    return seq2


def test_get_longest_all_primes():
    l = [4, 3, 5, 7, 8, 16, 222]
    l1 = [3, 5, 7]
    assert get_longest_all_primes(l)[0] == l1
    l = [8, 13, 17, 19, 8, 2, 3, 7]
    l1 = [13, 17, 19]
    l2 = [2, 3, 7]
    assert get_longest_all_primes(l)[0] == l1
    assert get_longest_all_primes(l)[1] == l2


def test_get_longest_sorted_asc():
    l = [9, 5, 6, 7, 8, 3, 4]
    l1 = [5, 6, 7, 8]
    assert get_longest_sorted_asc(l)[0] == l1
    l = [1, 2, 3, 4, 3, 0, 1, 2, 3]
    l1 = [1, 2, 3, 4]
    l2 = [0, 1, 2, 3]
    assert len(get_longest_sorted_asc(l)) == 2
    assert get_longest_sorted_asc(l)[0] == l1
    assert get_longest_sorted_asc(l)[1] == l2
    l = [8, 1, 2, 3, 4, 3, 1, 2, 8, 9, 0, 11, 12, 13]
    l1 = [1, 2, 3, 4]
    l2 = [1, 2, 8, 9]
    l3 = [0, 11, 12, 13]
    assert len(get_longest_sorted_asc(l)) == 3
    assert get_longest_sorted_asc(l)[0] == l1
    assert get_longest_sorted_asc(l)[1] == l2
    assert get_longest_sorted_asc(l)[2] == l3


def test_get_longest_digit_count_desc():
    l = [1234, 333, 56, 7, 8, 9]
    l1 = [1234, 333, 56, 7]
    assert get_longest_digit_count_desc(l)[0] == l1
    l = [0, 345, 34, 5, 7, 789, 78, 9, 0]
    l1 = [345, 34, 5]
    l2 = [789, 78, 9]
    assert len(get_longest_digit_count_desc(l)) == 2
    assert get_longest_digit_count_desc(l)[0] == l1
    assert get_longest_digit_count_desc(l)[1] == l2


def printMeniu():
    print("1.Citire date")
    print("2.Determinare cea mai lunga subsecventa cu numere in ordine crescatoare.")
    print("3.Determinare cea mai lunga subsecventa cu numarul de cifre in ordine descrescaoare.")
    print("4.Determinare cea mai lunga subsecventa de numere prime")
    print("5.Iesire")


def run():
    test_get_longest_sorted_asc()
    test_get_longest_digit_count_desc()
    test_get_longest_all_primes()
    lista = []
    printMeniu()
    while True:

        o = int(input("Optiune: "))
        if o == 1:
            lista = readingList()
            print(lista)
        elif o == 2:
            print("Secventa/secventele cele mai lungi cu numerele in ordine crescatoare sunt: ")
            lst = get_longest_sorted_asc(lista)
            if (len(lst) == 1):
                print(lst[0])
            else:
                for elem in lst:
                    print(elem)
            get_longest_sorted_asc(lista)
        elif o == 3:
            lst1 = get_longest_digit_count_desc(lista)
            if (len(lst1) > 0):
                print(
                    "Secventa/secventele cele mai lungi cu elemente avand numarul de cifre in ordine descrescatoare sunt: ")
            if (len(lst1) == 0):
                print("Nu exista secventa cu prorpietatea2.Toate numerele au numar egal de cifre.")
            if (len(lst1) == 1):
                print(lst1[0])

            else:
                for elem in lst1:
                    print(elem)
            get_longest_digit_count_desc(lista)
        elif o== 4:
            lst2 = get_longest_all_primes(lista)
            if len(lst2) == 0:
                print("nu exista secvente de numere prime.")
            if len(lst2) == 1:
                print(lst2[0])
            else:
                for elem in lst2:
                    print(elem)

        elif o == 5:
            print("Optiune gresita!Reincercati!")
            break


run()
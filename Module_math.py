import random

while True:

    def euclid_f(a,b):
        if a == 0:
            return b

        while b != 0:
            if a > b:
                a = a - b
            else:
                b = b - a

        return a


    answer1 = input("""
    Обчислити a mod m = x  -- 1
    Обчислити a^b mod m = x -- 2
    Обчислити a*x ≡ b mod m -- 3
    Генерувати прості числа від a до b -- 4

    Відповідь: """)

    if answer1 == "1":
        m = int(input("Modul: "))
        numb = int(input("Number: "))
        print(numb % m)

    if answer1 == "2" or "3":
         def pow_mod(number, power, modul):            # Решение a^b mod m = x
            n = 1
            p = 1
            while n <= power:
                rez = p*number % modul
                n+= 1
                p = rez

         #   print("p", p)
            return int(p)

    if answer1 == "3" or "4":
        def primfacs(n):                             # Алгоритм простых чисел
                    q = 2
                    primfac = []
                    while q * q <= n:
                        while n % q == 0:
                            primfac.append(q)
                            n = n / q
                        q = q + 1
                    if n > 1:
                        primfac.append(n)
                    return primfac


    if answer1 == "2":
        m = int(input("Modul: "))
        numb = int(input("Number: "))
        power = int(input("Pow: "))

        pow_mod(m, power, numb)

    elif answer1 == "3":
        m = int(input("Modul: "))
        a = int(input("a: "))
        b = int(input("b: "))

        b %= m
        if b == 0:
            print("x = 0")           

        else:
            nsd = euclid_f(a, b) 
            nsd1 = euclid_f(nsd, m)

            if nsd1 > 1:
                a /= nsd1
                b /= nsd1
                m /= nsd1
                nsd /= nsd1
            if nsd > 1:
                a /= nsd
                b /= nsd

            m = int(m)

            nsd = euclid_f(a, m)
            #  print('nsd^', nsd)

            #nsd = euclid_f(int(a/b), m)
            if nsd != 1:
                print("Неможливо порахувати")

            else:                              
                l = primfacs(m)

                n = 1
                for i in set(l):                                         # Функция Эйлера
                    n *= (i ** l.count(i) - i ** (l.count(i) - 1))

                n -= 1

                print((pow_mod(a, n, m) * b) % m)



    elif answer1 == "4":
        A = int(input("A: "))
        B = int(input("B: "))
        print("Очікуйте..")

        l = []

        for i in range (A, B + 1):
            if i == B:
                l.extend(primfacs(i))
                print("Очікуйте...")
                break
            l.extend(primfacs(i))
    

        l = list(set(l))
        l.sort()

        for i in l:
            if i < A:
                l.insert(l.index(i), 0)
                l.remove(i)

        l = list(set(l))
        l.remove(0)

        print(random.choice(l))





    else:
        answer1 = input("""

    Помилка!! Напиши будь-ласка номер завдання!

    Обчислити a mod m = x  -- 1
    Обчислити a^b mod m = x -- 2
    Обчислити a*x ≡ b mod m -- 3
    Генерувати прості числа від a до b -- 4
    Відповідь: """)

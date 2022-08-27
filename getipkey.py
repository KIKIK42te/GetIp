import socket
print('********* ********* *********       *  *******')
print('*         *             *              *     *')
print('*         *             *           *  *******')
print('*         *********     *           *  *')
print('*   ***** *             *           *  *')
print('*	* *             *           *  *')
print('********* *********     *           *  *')
print('☆┌─┐　─┐☆\n│▒│ /▒/\n│▒│/▒/\n│▒ /▒/─┬─┐\n│▒│▒|▒│▒│\n┌┴─┴─┐-┘─┘\n│▒┌──┘▒▒▒│\n└┐▒▒▒▒▒▒┌┘\n└┐▒▒▒▒┌┘')

print('-' * 50 ,)
print('\t[1] -- Скан портов')
print('\t[2] -- WI-FI стиллер',)
print('\t[3] -- Генератор паролей',)
print('-' * 50 ,"\n")

text_a = input("Ввод -- ")

if text_a == "1":
    import socket
    import time
    import bs4, requests
    def scan():
        host = input("[!] Ip - адрес для сканирования --> ")
        print()
        port = [ 20, 21, 22, 23, 42, 43, 53, 67, 69, 80, 110, 139, 8000, 8080, 3128, 3389, 6588, 1080, 5900, 8888, ]
        for i in port:
            try:
                scan = socket.socket()
                scan.settimeout(0.5)
                scan.connect((host, i)) 
            except socket.error:
                print("[-] Port -- ", i ,"-- [CLOSED]")
            else:
                print("[+] Port --", i ,"-- [OPEN]")
    def ip():
        s = requests.get('https://2ip.ua/ru/')
        b = bs4.BeautifulSoup(s.text, "html.parser")
        a = b.select(" .ipblockgradient .ip")[0].getText()
        print(a)
    print("-" * 50)
    print("\t[1] --- Сканировать порты")
    print("\t[2] --- Узнать IP")
    print("-" * 50, "\n")
    text_a = input("[Ввод]---> ")
    print()
    if text_a == "2":
        ip()
    if text_a == "1":
        scan()
    print()
    print("-" * 50)
    print()
    time.sleep(1)
    input("Для выхода нажмите ENTER: ")
    quit()

if text_a == "2":
    import subprocess

    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print ("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                print ("{:<30}|  {:<}".format(i, ""))
        except subprocess.CalledProcessError:
            print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
    input("")
    quit()

if text_a == "3":
    import random
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    number = input('Количество паролей?'+ "\n")
    length = input('Длина создоваемого пароля?'+ "\n")
    number = int(number)
    length = int(length)
    for n in range(number):
        password =''
        for i in range(length):
            password += random.choice(chars)
        print(password)
    quit()

from passlib.hash import sha512_crypt
hash = sha512_crypt.hash("egg",salt = "HX")


def testPass(cryptPass):
    salt = cryptPass.split('$')[2]


    dictFile = open('dictionary_512.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = sha512_crypt.hash(word,salt = salt,rounds = 5000)
        
        if (cryptWord == cryptPass):
            print("[+] Found Password: "+word+"\n")
            return
    print ("[-] Password Not Found.\n")
    return

def main():
    passFile = open('passwords_512.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print(cryptPass)
            print("[*] Cracking Password For: "+user)
            testPass(cryptPass)
if __name__ == "__main__":
    main()
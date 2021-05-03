from passlib.hash import des_crypt
hash = des_crypt.hash("egg",salt = "HX")


def testPass(cryptPass):
    salt = cryptPass[0:2]


    dictFile = open('dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = des_crypt.hash(word,salt = salt)
        if (cryptWord == cryptPass):
            print("[+] Found Password: "+word+"\n")
            return
    print ("[-] Password Not Found.\n")
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("[*] Cracking Password For: "+user)
            testPass(cryptPass)
if __name__ == "__main__":
    main()
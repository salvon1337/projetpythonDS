import re
import random
import string
import maskpass
import os
import hashlib

emailtest = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


# retourne le length du fichier
def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    f.closed
    return i + 1


# check if fichier is empty
def file_is_empty(path):
    return os.stat(path).st_size == 0


# check if email is valid

def isValid(email):
    if re.fullmatch(emailtest, email):
        return True
    else:
        return False


# check if mdp is valid
def isvalidpass(pwd):
    lowercount = 0
    majuscount = 0
    numbercounter = 0
    symbolcounter = 0
    if (len(pwd) >= 8):
        for c in pwd:
            if (c.islower()):
                lowercount += 1
            if (c.isupper()):
                majuscount += 1
            if (c.isdigit()):
                numbercounter += 1
            if re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\]', pwd):
                symbolcounter += 1
    else:
        print("entrer un password de longuer 8 au minimum")
        return 0
    if (lowercount == 0):
        print("utiliser au minimum un caractere miniscule")
    if (majuscount == 0):
        print("utiliser au minimum un caractere majuscule")
    if (numbercounter == 0):
        print("utiliser au minimum un chiffre")
    if (symbolcounter == 0):
        print("utiliser au minimum un symbol")
    if (lowercount != 0 and majuscount != 0 and numbercounter != 0 and symbolcounter != 0):
        return 1
    return 0


# methode pour generer mdp (length 8 ,min 1 majus ,min 1 miniscule , min 1 symbol)
def genererpass():
    while True:
        test = '1'
        pwd = ""
        x = random.randint(6, 8)
        for i in range(x):
            p = random.randint(1, 4)
            if (p == 1):
                pwd += random.choice(string.ascii_lowercase)
            elif (p == 2):
                pwd += random.choice(string.ascii_uppercase)
            elif (p == 3):
                pwd += random.choice(string.digits)
            elif (p == 4):
                pwd += random.choice(string.punctuation)
        lowercount = 0
        majuscount = 0
        numbercounter = 0
        symbolcounter = 0
        for c in pwd:
            if (c.islower()):
                lowercount += 1
            if (c.isupper()):
                majuscount += 1
            if (c.isdigit()):
                numbercounter += 1
            if (not c.isalnum()):
                symbolcounter += 1
        if (lowercount != 0 and majuscount != 0 and numbercounter != 0 and symbolcounter != 0):
            test = '0'
        if (test == '0'):
            return (pwd)


# affichage de menu

print("1-entrer une email")
print("2-entrer un password")
print("3-quitter")
print("4-modifier un compte")

email = ""
pwd = ""
choixpass = ""
choix = ""

while True:
    # add first line in the file if it doesnt exist already
    File = open('Email_Pass ex', 'a')
    lignedata = '{0:<10}{1:<30}{2:<10}\n'.format('Index', 'Email', 'Password')
    if os.path.getsize('Email_Pass ex') == 0:
        File.write(lignedata)
        File.close()

    # reading lines from fichier
    file = open('Email_Pass ex', "r")
    lines = file.readlines()
    file.close()

    while True:
        # making it pass to pass auto after filling the email or viceversa
        if ((choix == '1') or (choix == '2')):
            break
        choix = input("votre choix du menu est : ")
        if ((choix == '3') or (choix == '2') or (choix == '1') or (choix == '4')):
            break
        else:
            print("svp entrer un choix correct")

    # making the first choice which is filling the email
    if (choix == '1'):
        while True:
            email = input("Email: ")

            existance = '1'

            for line in lines:
                if (line != lines[0]):
                    test = re.split('([a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[A-Z|a-z]{2,}))', line)
                    if (email == test[1]):
                        existance = '0'
                        print("this email exist already")
            if (isValid(email) and existance == "1"):
                if (len(pwd) == 0):
                    choix = '2'
                break
            else:
                print("svp entrer une email correcte")

            # second choice : filling password
    if (choix == '2'):
        print("1-generer automatiquement votre password")
        print("2-entrer votre password")
        while True:
            choixpass = input("  Svp tapez 1/2 :")
            if (choixpass == '1' or choixpass == '2'):
                break
            # choix 1 dans le mdp est la generation automatique
    if (choixpass == '1'):
        pwd = genererpass()
        pwd = hashlib.sha256(pwd.encode()).hexdigest()
        choix = '1'
    # choix 2 taper le mdp
    elif (choixpass == '2'):
        while True:
            pwd = maskpass.askpass(mask="*")
            if (isvalidpass(pwd)):
                pwd = hashlib.sha256(pwd.encode()).hexdigest()
                choix = '1'
                break
            # si l email n'est pas vide et le mdp aussi is l'ecrit dans le fichier
    if ((email != "") and (pwd != "")):
        File1 = open('Email_Pass ex', 'a')
        data = '{0:<10}{1:<30}{2:<10}\n'.format(file_len('Email_Pass ex'), email, pwd)
        print("data recieved")
        email = ""
        pwd = ""
        choixpass = ""
        choix = ""
        File1.close()
        with open("Email_pass ex", "a") as f:
            f.write(data)

    # choix 3 pour fermer le programme
    if (choix == '3'):
        exit()

    # choisir le choix 4 d'update
    if (choix == '4'):
        refreshfile = 1
        print("entrer l'email du votre compte : ")
        email1 = input("Email : ")
        file = open('Email_Pass ex', "r")
        lines = file.readlines()
        file.close()
        existance = 1
        i = 0
        # parcourir l email dans le fichier
        for line in lines:
            if (i != 0):
                testupdate = re.split('([a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[A-Z|a-z]{2,}))', line)
                if (email1 == testupdate[1]):
                    rightemail = testupdate
                    existance = 0
            i += 1

        # si l email exist dans le fichier il faut entrer le pwd pour le comparer
        if (existance == 0):
            print("entrer le password maintenent :")
            pwdverify = maskpass.askpass(mask="*")
            pwdverify = hashlib.sha256(pwdverify.encode()).hexdigest()
            print(testupdate[3].strip())
            print(pwdverify)

            # will grant access to the user if pwd and email are valid
            if (pwdverify == testupdate[3].strip()):
                print("access granted you may start by changing your mail first ..")
                email2 = input("Email: ")
                existance = '1'
                file = open('Email_Pass ex', "r")
                lines = file.readlines()
                file.close()
                existance = '1'
                # checking the existance of the new mail with the old list
                for line in lines:
                    if (line != lines[0]):
                        test = re.split('([a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[A-Z|a-z]{2,}))', line)
                        if (email2 == test[1]):
                            existance = '0'
                            print("this email exist already")
                if (isValid(email2) and existance == "1"):
                    while True:
                        pwd = maskpass.askpass(mask="*")
                        if (isvalidpass(pwd)):
                            pwd = hashlib.sha256(pwd.encode()).hexdigest()
                            break
                        else:
                            print('Choose a stronger pass !! ')
                    matchid = testupdate[0].split()

                    with open('Email2', 'w') as sss:
                        if os.path.getsize('Email2') == 0:
                            sss.write(lignedata)
                        # writing the lines on the temp file with exchanging the original mail
                        for line in lines:
                            num = 1
                            if (line != lines[0]):
                                test = re.split('([a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[A-Z|a-z]{2,}))', line)
                                if (email1 != test[1]):
                                    data = '{0:<10}{1:<30}{2:<10}\n'.format(num, test[1], test[3].strip())
                                    choixpass = ""
                                    choix = ""
                                    sss.write(data)
                                    num += 1
                        data = '{0:<10}{1:<30}{2:<10}\n'.format(num, email2, pwd)
                        sss.write(data)
                        refreshfile = 0

                else:
                    print("svp entrer une email correcte")

                # copy infos from temp files to the main file
        if (refreshfile == 0):
            with open('Email2', 'r') as sssread:
                copylines = sssread.readlines()
            with open('Email_pass ex', 'w') as ss:
                pass
            with open('Email_pass ex', 'a') as ss:
                ss.write(lignedata)
                n = 1
                for copyline in copylines:
                    if (copyline != copylines[0]):
                        test = re.split('([a-zA-Z0-9]+[.-_]*[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[A-Z|a-z]{2,}))', copyline)
                        data = '{0:<10}{1:<30}{2:<10}\n'.format(n, test[1], test[3].strip())
                        ss.write(data)
                        n += 1
            os.remove('Email2')
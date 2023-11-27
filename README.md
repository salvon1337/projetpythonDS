valid.py;

Ce fichier Python propose une série de fonctions pour gérer la validation de mots de passe, la génération de mots de passe aléatoires, ainsi que le chiffrement et le déchiffrement de messages à l'aide du chiffre de César.

1. **Validation de mots de passe (`isValidpass`)** :
   - Vérifie si un mot de passe satisfait certains critères, notamment une longueur minimale de 8 caractères, la présence de minuscules, majuscules, chiffres et symboles.

2. **Génération de mots de passe aléatoires (`generate_password`)** :
   - Génère un mot de passe aléatoire répondant aux critères définis, incluant des lettres minuscules, majuscules, chiffres et symboles.

3. **Chiffrement et déchiffrement avec le chiffre de César (`ciphercaesar` et `ciphercaesar2`)** :
   - `ciphercaesar` chiffre un message en déplaçant chaque lettre d'un certain nombre de positions (décalage).
   - `ciphercaesar2` déchiffre un message chiffré avec le chiffre de César en effectuant le décalage inverse.

4. **Chiffrement et déchiffrement avec le chiffre de César utilisant des caractères ASCII (`ciphercaesarASCII` et `ciphercaesarASCII2`)** :
   - `ciphercaesarASCII` chiffre un message en utilisant le chiffre de César avec des caractères ASCII.
   - `ciphercaesarASCII2` déchiffre un message chiffré avec le chiffre de César utilisant des caractères ASCII.

test.py;

Ce fichier Python est dédié à des tests pour les fonctionnalités et les opérations définies dans d'autres fichiers. 
Il importe les modules et les fonctions créés dans d'autres fichiers pour effectuer des vérifications et tester leur fonctionnement. 
Il comporte des séries d'appels de fonctions et d'invocations d'exemples pour démontrer l'utilisation appropriée des fonctions définies dans les autres fichiers.


fonctionsfichier.py;

Ce fichier Python contient une série de fonctions destinées à accomplir des tâches spécifiques :

1. **Fonctionnalités diverses** :
   - Il définit plusieurs fonctions pour effectuer des opérations spécifiques, telles que des opérations mathématiques simples, la validation de données ou la manipulation de chaînes de caractères.

2. **Manipulation de données** :
   - Les fonctions ici sont conçues pour gérer et transformer des données selon les besoins spécifiques de l'utilisateur, telles que des conversions de formats ou des opérations arithmétiques.

exercice.py;

Ce code Python réalise plusieurs fonctions liées à la gestion des emails et des mots de passe dans un fichier. Voici une explication détaillée :

1. **Import des modules :**
   - Le code importe plusieurs modules Python standard tels que `re`, `random`, `string`, `maskpass`, `os`, et `hashlib`, qui fournissent des fonctionnalités pour les expressions régulières, la génération aléatoire, les manipulations de chaînes de caractères, la manipulation des fichiers, et le hachage.

2. **Fonctions de validation :**
   - `isValid(email)`: Vérifie si une adresse email est valide en utilisant une expression régulière.
   - `isvalidpass(pwd)`: Vérifie si un mot de passe est valide en vérifiant la longueur minimale, la présence de majuscules, minuscules, chiffres et symboles.

3. **Génération de mots de passe :**
   - `genererpass()`: Génère un mot de passe aléatoire respectant certaines conditions : longueur entre 6 et 8 caractères, au moins une majuscule, une minuscule, un chiffre et un symbole.

4. **Menu interactif :**
   - Affiche un menu interactif pour différentes actions : entrer une adresse email, entrer un mot de passe, quitter, ou modifier un compte existant.

5. **Gestion des fichiers :**
   - Vérifie si le fichier "Email_Pass ex" existe. S'il est vide, ajoute une première ligne pour les en-têtes.
   - Lit les données existantes du fichier "Email_Pass ex" pour récupérer les informations stockées.

6. **Actions utilisateur :**
   - L'utilisateur peut entrer une adresse email et un mot de passe, ou générer automatiquement un mot de passe. Les entrées sont vérifiées pour leur validité avant d'être ajoutées au fichier.
   - L'utilisateur peut également modifier un compte existant en remplaçant l'adresse email ou le mot de passe après vérification de l'authenticité de l'email et du mot de passe actuels.

7. **Mise à jour du fichier :**
   - Une fois les modifications effectuées (ajout, suppression, mise à jour), le fichier "Email_Pass ex" est actualisé avec les nouvelles informations.

Ce script offre une interface pour gérer les adresses email et les mots de passe dans un fichier, en respectant des critères de validation pour les données entrées ou générées aléatoirement.


# Mémo GPG :

## Génération de clé :

* `gpg --gen-key` : génère une clé avec les options renseignées par la suite

* `gpg --full-generate-key` : menu interactif en terminal avec davantage d'options

Des détails customisables peuvent être la longueur de la clé, sa période de validité, ou une passphrase pour la confirmer à l'usage, etc.

La clé nécessite également une identité (telle qu'elle sera affichée chez les autres utilisateurs après partage), qui est généralement un nom complet et une adresse mail (même s'il est possible d'utiliser un pseudonyme). Cette identité (ou une partie de cette identité, par ex. seulement le prénom s'il n'y a pas d'ambiguïté, ou le mail) pourra également être utilisée comme raccourci pour identifier un destinataire pendant un chiffrement, ce qui est plus rapide qu'en utilisant l'ID de la clé.

## Génération de certificat de révocation

Le certificat de révocation permet d'annuler la validité d'une clé nous appartenant, il est ainsi vital d'en générer un à la création de la clé.

* `gpg --gen-revoke identite` permet d'exporter un certificat de révocation. Sans `--output`, il sera envoyé sur la sortie standard.

## Lister les clés et signatures du trousseau

* `gpg --list-key` permet de lister toutes les clés du trousseau. `gpg --list-keys` est un alias.

* `gpg --list-public-keys` ne liste que les clés publiques (celles générées par l'utilisateur, et celles reçues des autres utilisateurs).

* `gpg --list-secret-keys` ne liste que les clés privées de l'utilisateur.

* `gpg --list-sig` liste la signature des clés du trousseau. `gpg --list-sigs` et `gpg --list-signatures` sont des alias.

## Export et import de clés publiques

* `gpg --export identite` permet d'exporter une clé publique.

* `gpg --import fichier` permet d'importer une clé publique partagée dans un trousseau.

## Validation d'une clé par signature, affichage des empreintes et signatures enregistrées

L'empreinte d'une clé est une portion assez courte d'octets pour être transmise aisément, mais assez significative pour valider avec certitude l'authenticité d'une clé. Signer une clé revient à y apposer notre clé publique et la déclarer comme fiable (aux yeux de notre machine).

* `gpg --edit-key identite` permet d'effectuer certaines actions sur une clé à l'aide d'un prompt contextuel :

* `fpr` "fingerprint", affiche l'empreinte de la clé.

* `sign` permet de signer la clé. C'est une opération dangereuse car reconnaître une clé inconnue donne à son propriétaire une légitimité qui n'est pas forcément pertinente. Il faut normalement vérifier la signature de la clé auprès de la personne avec qui l'on souhaite communiquer avant de signer aveuglément la clé.

* `check` permet de lister et vérifier les signatures apposées sur la clé.

## Chiffrement et déchiffrement à partir de clés

* `gpg --encrypt fichier --recipient identite` permet d'encrypter un document selon la clé publique (connue au préalable) d'un destinataire enregistré. L'option `--recipient` doit être utilisée une fois par destinataire.

* `gpg --decrypt fichier` permet de déchiffrer le document lorsque l'on possède la clé privée correspondant à la clé publique avec laquelle le document a été chiffré.

* `gpg --symmetric fichier` permet de chiffrer un document de manière symétrique : il se retrouve protégé par un mot de passe fourni par l'utilisateur.

## Génération de signatures

* `gpg --sign document` permet de signer un document.

* `gpg --verify document` permet de vérifier la signature.

Remarque : `gpg --decrypt` vérifiera la signature avant de décrypter si le document est signé.

## Signatures en clair et signatures détachées

* La signature en clair est une signature ASCII au lieu de binaire : elle se génère avec `gpg --clearsign` mais le principe reste le même, cela rend juste la signature communicable plus facilement.

* La signature détachée est une signature exportée dans une sortie distincte du fichier chiffré : elle se génère avec `gpg --detach-sig doc` et se vérifie avec `gpg --verify fichier_signature fichier_crypte`

## Manipulation de la sortie

* `gpg --output a.txt` permet de rediriger la sortie de la commande vers un fichier externe, sinon il s'agira de la sortie standard.

* `gpg --armor` permet de convertir le flux binaire de la sortie en flux ASCII, le rendant ainsi manipulable, lisible, et éditable plus facilement.
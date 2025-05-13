# Documentation : Optimisation de Dofus via RAMDISK

Cette documentation explique comment améliorer considérablement les performances du jeu Dofus (ou d'un jeu équivalent utilisant beaucoup de cache disque) grâce à un Ramdisk sur Windows.

---

## 1. Pourquoi utiliser un Ramdisk ?

Un Ramdisk est un disque virtuel stocké directement en mémoire vive (RAM). Son avantage principal est une vitesse d'accès extrêmement rapide comparée aux disques SSD et HDD. Cela permet au jeu d'accéder instantanément aux fichiers fréquemment utilisés.

Avantages :

* Chargements quasi instantanés.
* Moins de ralentissements liés au cache.
* Préservation de la durée de vie des SSD.

---

## 2. Pré-requis

* Windows 10 ou 11.
* 16 Go de RAM minimum recommandés (idéalement 32 Go).
* Le logiciel gratuit ImDisk Toolkit : [Télécharger ImDisk](https://sourceforge.net/projects/imdisk-toolkit/)

---

## 3. Installation et configuration du Ramdisk

### Étape 1 : Installer ImDisk Toolkit

* Téléchargez et installez ImDisk Toolkit.

### Étape 2 : Créer un Ramdisk

* Ouvrez ImDisk Toolkit et cliquez sur « RamDisk Configuration ».
* Configurez le disque :

  * Taille recommandée : `8 Go`.
  * Lettre du lecteur : `R:` (ou une lettre disponible).
  * Système de fichiers : NTFS.
  * Décochez toutes les cases de sauvegarde automatique.
* Validez avec « OK ».

---

## 4. Déplacer le cache de Dofus vers le Ramdisk

### Étape 1 : Identifier le cache du jeu

* Chemin type : `C:\Users\VotreNom\AppData\Roaming\Dofus`

### Étape 2 : Copie initiale du cache

* Créez un dossier dans votre Ramdisk (ex : `R:\DofusCache`).
* Copiez l'intégralité du cache d'origine vers ce nouveau dossier.

### Étape 3 : Créer un lien symbolique (symlink)

* Ouvrez l'invite de commande en tant qu'administrateur (`cmd.exe`).
* Supprimez ou renommez le dossier cache original.
* Tapez cette commande :

```cmd
mklink /D "C:\Users\VotreNom\AppData\Roaming\Dofus" "R:\DofusCache"
```

Un message confirmera la création du lien.

---

## 5. Automatisation (optionnel mais recommandé)

Créez un fichier `Start-Dofus.ps1` avec le contenu suivant :

```powershell
$ramdiskPath = "R:\DofusCache"
$symlinkPath = "$env:APPDATA\Dofus"
$backupCache = "D:\DofusCacheBackup"

if (!(Test-Path "R:\")) {
    Write-Host "Erreur : le ramdisk n'est pas monté." -ForegroundColor Red
    exit
}

if (!(Test-Path $ramdiskPath)) {
    New-Item -ItemType Directory -Path $ramdiskPath
    if (Test-Path $backupCache) {
        Copy-Item "$backupCache\*" -Destination $ramdiskPath -Recurse
    }
}

if (!(Test-Path $symlinkPath)) {
    cmd /c mklink /D "$symlinkPath" "$ramdiskPath"
}

Start-Process "C:\CheminVersDofus\Dofus.exe"
```

* Adaptez les chemins à votre configuration.
* Lancez automatiquement au démarrage en plaçant un raccourci vers ce script dans le dossier `shell:startup`.

---

## 6. Vérification

* Vérifiez que votre disque Ram (`R:`) existe.
* Vérifiez le lien symbolique en naviguant vers :

  ```
  C:\Users\VotreNom\AppData\Roaming\Dofus
  ```
* Lancez Dofus, jouez quelques minutes, et vérifiez que des fichiers apparaissent et changent dans `R:\DofusCache`.

---

## 7. Sauvegarde du cache initial (optionnel)

Après une session complète de jeu, sauvegardez le cache :

* Copiez `R:\DofusCache` vers un dossier de sauvegarde (`D:\DofusCacheBackup`).

---

Votre configuration est maintenant optimisée pour Dofus avec un ramdisk. Profitez de chargements accélérés et d'une meilleure réactivité générale !

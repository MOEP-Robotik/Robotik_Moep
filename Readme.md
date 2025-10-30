# Pybricks Code für unsere Roboter

Das hier ist unser Repository, um unsere FLL Projekte zu sichern und Backups herzustellen.

> [!IMPORTANT]
> Tutorial ist noch nicht fertig. Visual Studio Code und die Pybricks packages müssen anders vorbereitet werden. Langsam wird es.
> Finger weg von .devcontainer, .vscode und requirements.txt !!!

# Tutorial zu Python, Pybricks und der Installation der Abhängigkeiten, sowie eine kleine übersicht über git

## Inhaltsverzeichnis
- [Installation](#installation)
- [Python](#python-grundlagen)
- [Pybricks](#pybricks-grundlagen)
- [git](#simple-git-Befehle)

## Installation

### Abhängigkeiten und Dinge, die installiert werden müssen:
- [git](https://git-scm.com/install)
- [Visual Studio Code](https://code.visualstudio.com/docs/?dv=win64user)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Dev Container Erweiterung für Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

Bei allen gilt: Downloaden (also auf die Links klicken) und dann ausführen. Wenn etwas in den Path soll, gerne akzeptieren (vor allem git)

### Klonen des Repositorys auf das Gerät
In cmd diese 3 Befehle ausführen
```bash
cd %userprofile%/Documents

mkdir GitHub && cd ./GitHub

git clone https://github.com/MOEP-Robotik/Robotik_Moep.git
```
Dabei wird ein neuer Ordner GitHub im Ordner Dokumente erstellt. In diesem wird das Repository geklont. Dort wird auch gearbeitet. Nach dem Öffnen des geklonten Ordners in Visual Studio Code sollte unten rechts eine Meldung kommen, ob der Ordner als DevContainer geöffnet werden soll. Dort auf "Reopen" o.ä. klicken. Beim ersten öffnen dauert es etwas länger als danach.
> [!NOTE]
> Da es ein Docker Container ist, ist das Terminal ein Linux Terminal, hat also nicht die commands, die Windows hat. Außerhalb bleibt alles wie bei Windows. 

## Pybricks
### Auf dem Spike Prime Hub (im Normalfall bereits geschehen)
Tutorial auf https://code.pybricks.com/ folgen
## Python Grundlagen
Eine gute "Grundlage" bilden die Python-Docs unter python.org

## Pybricks Grundlagen
Findet man auch online

## simple git Befehle
> [!TIP]
> Die Befehle müssen **nicht** gelernt werden, sofern die Visual Studio Code Erweiterung für GitHub verwendet wird

**git ...**
- ...**help**
- ...add
- ...push
- ...commit

- ...pull



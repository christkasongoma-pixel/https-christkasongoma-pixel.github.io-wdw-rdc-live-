#!/usr/bin/env bash
# Usage : ./push.sh https://github.com/VOTRE-COMPTE/wdw-rdc-live.git
set -e
[ -z "$1" ] && { echo "Donnez l'URL du dépôt GitHub vide."; exit 1; }
git init -b main
git add .
git commit -m "Première version : RDC en direct + page complète + sécurité"
git remote add origin "$1"
git push -u origin main

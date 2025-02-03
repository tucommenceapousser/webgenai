#!/bin/bash

# Couleurs pour le terminal
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}🔧 Installation des dépendances...${NC}"

# Met à jour les paquets
sudo apt update && sudo apt upgrade -y

# Installe les paquets nécessaires
sudo apt install -y python3 python3-pip python3-venv nodejs npm curl unzip git

# Créer un environnement virtuel Python pour le backend
echo -e "${GREEN}📂 Configuration de l'environnement Python...${NC}"
cd backend
python3 -m venv venv
source venv/bin/activate

# Installer les dépendances du backend
pip install -r requirements.txt
deactivate
cd ..

# Installer les dépendances du frontend
echo -e "${GREEN}📂 Installation des dépendances Frontend...${NC}"
cd frontend
npm install
cd ..

# Installer PM2 pour gérer les services en arrière-plan
sudo npm install -g pm2 serve

# Démarrer le backend avec PM2
echo -e "${GREEN}🚀 Démarrage du backend...${NC}"
cd backend
pm2 start "venv/bin/uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4" --name alien-backend
cd ..

# Démarrer le frontend avec PM2
echo -e "${GREEN}🚀 Build & lancement du frontend...${NC}"
cd frontend
npm run build
pm2 serve build --name alien-frontend --port 3000
cd ..

# Sauvegarde des services pour le redémarrage automatique
pm2 save
pm2 startup

echo -e "${GREEN}✅ Tout est installé et lancé !${NC}"
echo -e "🔗 Accède à l'interface : ${GREEN}http://localhost:3000${NC}"

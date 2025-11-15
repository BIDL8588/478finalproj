# 478finalproj

#Password “Cracking” Science (Synthetic Only)

This project will examine the sternght of synethic passwords by hashing and attempting to crack this offline(brute-force or ditioncary). The overall goal of tihs project is to understand the weakness of passwords and compare which passwrod provides more resistance to the different hashing algorithms.

#Project Struct

Source Code Folder: generate_passwords.py(create synthetic passwrods), hash_passwords.py(hash those passwords), crack_hash.py(brute_force/dictionary)
docker-compose.yml
Makefile - bootstrap commands to set up dependencies
#Set UP Python Virtual Environment

python 3 -m venv venv
source venv/bin/activate
Docker

docker compose up -d

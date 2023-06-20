#!/usr/bin/env python3
import subprocess
import sys
import os
import shutil

def check_dependency_installed(dependency):
    result = subprocess.run(['which', dependency], capture_output=True, text=True)
    return result.returncode == 0

def install_dependency(dependency):
    subprocess.run(['sudo', 'apt-get', 'install', '-y', dependency])

def create_wordpress_site(site_name):
    # Create docker-compose.yml file
    docker_compose_content = '''
version: '3'

services:
  wordpress:
    image: wordpress:latest
    restart: always
    ports:
      - 80:80
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - ./wordpress:/var/www/html
    depends_on:
      - db

  db:
    image: mysql:5.7
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    volumes:
      - ./db:/var/lib/mysql
'''
    with open('docker-compose.yml', 'w') as file:
        file.write(docker_compose_content)

    # Create /etc/hosts entry
    site_entry = f'127.0.0.1 {site_name}\n'
    hosts_file = '/etc/hosts'

    with open(hosts_file, 'a') as file:
        hosts_content = file.read()
        if site_entry not in hosts_content:
            file.write(site_entry)

    # Start containers
    print('Creating and starting containers...')
    subprocess.run(['docker-compose', 'up', '-d'])

    # Prompt user to open the site in a browser
    print(f'Site created successfully. Open http://{site_name} in your browser.')

if __name__ == '__main__':
    if not check_dependency_installed('docker') or not check_dependency_installed('docker-compose'):
        print('Docker and/or docker-compose are not installed. Installing packages...')
        install_dependency('docker')
        install_dependency('docker-compose')
        print('Packages installed successfully.')

    if len(sys.argv) < 2:
        print('Please provide a site name as a command-line argument.')
        sys.exit(1)

    site_name = sys.argv[1]

    create_wordpress_site(site_name)

    # Enable/disable site command
    if len(sys.argv) > 2:
        action = sys.argv[2]

        if action == 'enable':
            subprocess.run(['docker-compose', 'start'])
            print('Site enabled.')
        elif action == 'disable':
            subprocess.run(['docker-compose', 'stop'])
            print('Site disabled.')

    # Delete site command
    if len(sys.argv) > 2 and sys.argv[2] == 'delete':
        subprocess.run(['docker-compose', 'down'])
        os.remove('docker-compose.yml')
        shutil.rmtree('wordpress')
        shutil.rmtree('db')
        print('Site deleted.')

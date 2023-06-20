# rtCamp-assignment

Create a command-line script, preferably in Python to perform the following tasks:

1.Check if docker and docker-compose is installed on the system. If not present, install the missing packages.
2.The script should be able to create a WordPress site using the latest WordPress Version. Please provide a way for the user to provide the site name as a command-line argument.
3.It must be a LEMP stack running inside containers (Docker) and a docker-compose file is a must.
4.Create a /etc/hosts entry for example.com pointing to localhost. Here we are assuming the user has provided example.com as the site name.
5.Prompt the user to open example.com in a browser if all goes well and the site is up and healthy.
6.Add another subcommand to enable/disable the site (stopping/starting the containers)
7.Add one more subcommand to delete the site (deleting containers and local files).

## Prerequisites

Before using the Dockerized WordPress CLI, ensure that you have the following software installed on your system:

- Docker
- Docker Compose

## Installation

To install the Dockerized WordPress CLI, follow these steps:

1. Clone the repository or download the script files to your local machine.

2. Ensure that the script has executable permissions. If not, grant the necessary permissions using the command:

   ```shell
   chmod +x wordpress_cli.py

3. If Docker and Docker Compose are not already installed on your system, the script will attempt to install them automatically. Make sure you have administrative privileges (sudo) to install packages.

## Usage
The Dockerized WordPress CLI supports the following command-line arguments:

## Create a WordPress site
To create a new WordPress site, provide the desired site name as a command-line argument:

$ ./wordpress_cli.py create <site_name>

Replace <site_name> with your desired site name, such as example.com. This command will set up a new WordPress site using the latest WordPress version, running on a LEMP stack inside Docker containers. The script will automatically generate an /etc/hosts entry, mapping the site name to localhost.

After creating the site, if all goes well and the site is up and healthy, the script will prompt you to open the site in a browser.

Note: To ensure that the site name example.com points to localhost, make sure you have administrative privileges (sudo) when running the script.

## Enable/Disable the site

You can enable or disable the site using the following subcommands:

To enable the site and start the Docker containers:

$ ./wordpress_cli.py enable <site_name>

To disable the site and stop the Docker containers:

$ ./wordpress_cli.py disable <site_name>

## Delete the site

To remove the site entirely, including the Docker containers and local files, use the following command:

$ ./wordpress_cli.py delete <site_name>

This command will stop and delete the Docker containers, remove the 'docker-compose.yml' file, and delete the local WordPress files and database associated with the site.

Note: Deleting a site will permanently remove all data associated with it. Exercise caution when using this command.

## '/etc/hosts' Entry

To ensure that the site name you provide points to 'localhost', the Dockerized WordPress CLI will automatically create an entry in your '/etc/hosts' file.

For example, if you provide 'example.com' as the site name, the script will add the following entry:

$ 127.0.0.1 example.com

This mapping allows your system to resolve 'example.com' to the local machine.

Note: Modifying the '/etc/hosts' file requires administrative privileges ('sudo'), so make sure to run the script accordingly.



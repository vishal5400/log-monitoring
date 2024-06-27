# Log-Monitoring-Tools MVP

This repo contains a log collector called `client` and a Flask app that displays logs on a webpage. It is designed for small projects that do not have enough resources to use separate log tools. 

The `client` uploads log files to a remote server with log rotation. This helps store logs in one place and allows the team to check logs without accessing the main server. For added functionality, the Flask app displays the logs on a webpage.

## Client Setup Instructions
### 1. First Setup a Server

First, set up a server with password-based authentication SSH using any non-root user. After that, use these server details in the client configuration.

### 2. Clone the Repository

```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```
### 3. Update Server Details in Configuration File

Add server details in the client configuration file, including the IP address, user, and password. Also, specify the client name to identify which server the logs are from.

### 4. Install
```sh
  sudo make install
```
### 5. check status
```sh
  sudo systemctl status log-client.service
```
## Server Setup Instructions

It is a demo flask app that show you logs directory on web page and you select and open logs file its show you containt of file you check new logs of that file to refresh the page

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```
### 2. Install python package
```sh
pip3 install -r requirement.txt
```
### 3. Run the Application
```sh
python3 server.py
```

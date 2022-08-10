<h1 align="center"> Git-Remote </h1>
<h4 align="center"> 
 This is a tool that uses Github API to create a repository, essential license, and readme template from console written in PowerShell ps1</h4>

# Installation and Usage
```
  git clone https://github.com/Akshay-Vs/Git-Remote.git
  powershell -ExecutionPolicy ByPass -File Git-Remote/git-remote.ps1

```
Copy and paste the command into the desired directory

## Setup
- Enter the Github username
- Enter the authentication key provided by GitHub
  - <i>Leaving this blank will redirect to the Personal Access Token page</i>
- Enter the repository name
  - <i>White spaces will be converted to '-' hyphen</i>
- Enter a description
- Select a license
 - The unlicensed license is the default
- Wait for the process to complete and you will be redirected to the remote repository

## Execution process
- Downloading license and readme template from GitHub
- Git starts in the local directory
- Commits all files to the local repository
- Creating a directory on GitHub using the Github API
- Pushes all files to remote repository
- Open the browser and redirect to the remote repository


## Credentials
- Username  - Github username
- Auth - <a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token">Authention token</a>
    - permission - repo:Full control of private repository
- Repo name and Description<br>
<i>Repos are private by default</i>

## Templates
- <a href="https://raw.githubusercontent.com/Akshay-Vs/license-templates/master/templates"> Readme </a>
- License

<h1 align="center"> G Remote - Installation and Usage </h1>

<p align="center"><u>
 <img align="center" src="https://badgen.net/badge/license/UNLICENSE/white"/>&nbsp;
 <img align="center" src="https://badgen.net/github/stars/akshay-vs/G-Remote?color=white"/>&nbsp;
 <img align="center" src="https://badgen.net/github/watchers/akshay-vs/G-Remote?color=white"/>&nbsp;
 <img align="center" src="https://badgen.net/github/forks/akshay-vs/G-Remote?color=white"/>&nbsp;
 <img align="center" src="https://badgen.net/badge/powershell/PS1/white"/>
 
</u></p>

<h4 align="center"> 
This is a tool that uses Github API to create a repository, essential license, and readme template from console written in PowerShell ps1</h4>

 ```
git clone https://github.com/Akshay-Vs/G-Remote.git
powershell -ExecutionPolicy ByPass -File G-Remote/git-remote.ps1

```
<h6 align="right"> 👆Copy and paste the command to execute</h6>
<dl><dd><dl><dd>

## Setup
- Open desired directory, then open cmd/powershell in the directory
- Copy and paste the command
- Enter the Github username
- Enter the authentication key provided by GitHub
  - <b>Leaving this blank will redirect to the Personal Access Token page</b>
- Enter the repository name
  - <b>White spaces will be converted to '-' hyphen</b>
- Enter a description
- Select a license
  - <b>The unlicensed license is the default</b>
- Wait for the process to complete and you will be redirected to the remote repository
## Execution process
- Downloads license and readme template from GitHub
- Git starts in the local directory
- Commits all files to the local repository
- Creating a directory on GitHub using the Github API
- Pushes all files to remote repository
- Open the browser and redirect to the remote repository
- Deletes g-remote files from the directory


## Credentials
- Username  - Github username
- Auth - <a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token">Authention token</a>
    - <b>permission - repo:Full control of private repository</b>
- Repo name and Description<br>
    - <b>Repos are private by default</b>

## Templates
- <a href="https://raw.githubusercontent.com/Akshay-Vs/license-templates/master/templates"> Readme </a>
- License

$Parms = @{
    Verbose = $True
    Version = "1.0"
    Author = "akshay.vs2005@gmail.com"
    Description = "Script to automate git remote"
    CompanyName = "Akshay-Vs"
    Copyright = "2022 Akshay-Vs. All rights reserved."
    RequiredScripts = "Start-WFContosoServer", "Stop-ContosoServerScript"
    Tags = @("git", "git-remote", "automation")

    PassThru = $True
    ReleaseNotes = @("Initial Release")
}
"$Parms"
#Clearing Console
powershell -Command "cls"
powershell -Command $host.UI.RawUI.WindowTitle = "Git-Remote"

function Download($name)
{
    Write-Host "Downloading license template..."
    $Template = Invoke-WebRequest -Uri https://raw.githubusercontent.com/Akshay-Vs/license-templates/master/templates/$name | Select-Object -Expand Content
    $Template = $Template -replace "@Year", $Year
    $Template = $Template -replace "@User", $User
    $Template = $Template -replace "@Repo", $Repo
    return $Template
}

#Reading Credentials
$User = Read-Host "Enter your github username"

$Auth = Read-Host "Enter Auth key"
if ($Auth -eq "")
{
    Start-Process "https://github.com/settings/tokens"
    $Auth = Read-Host "Enter Auth Key"
}

$Repo = Read-Host "Enter repository name" 
$Repo = $Repo -replace " ", "-"
$Description = Read-Host "Enter Description"
$Private = "false"


Write-Host "`n`n1) MIT`n2) Apache`n3) GPL3`n4) BSD3"
$License = Read-Host "Chose a license template"

$Year = Get-Date -Format yyyy

#Generating Readme.md
$Readme = "$<h1 align='center'>$Repo</h1>"
$Temp = Invoke-WebRequest -Uri https://raw.githubusercontent.com/othneildrew/Best-README-Template/master/BLANK_README.md
$Readme = "$Readme`n $Temp"
    #Writing files
    try{
        New-Item "Readme.md"
        Set-Content "Readme.md" -Value $Readme
    }
    catch
    {
        Write-Error "$_`nSkipping: Cannot create Readme.md"
    }


#Generating License
    if($License -eq 1)
    {
        $License = Download("mit.txt")
        #Write-Host = $License
    }
    elseif($License -eq 2)
    {
        $License = Download("apache.txt")
        #Write-Host = $License
    }
    elseif($License -eq 3)
    {
        $License = Download("gpl3.txt")
        #Write-Host = $License
    }
    elseif($License -eq 4)
    {
        $License = Download("bsd3.txt")
        #Write-Host = $License
    }
    else{
        $License = Download("unlicense.txt")
    }

    #writting License
    try{
        New-Item "LICENSE"
        Set-Content "LICENSE" -Value $License
    }
    catch
    {
        Write-Error "$_`nSkipping: Cannot create License"
    }

#Generating gitignore
$Temp = Invoke-WebRequest -Uri https://raw.githubusercontent.com/Akshay-Vs/templates/master/gitignore-template.txt
    #Writing files
    try{
        New-Item ".gitignore"
        Set-Content ".gitignore" -Value $Temp
    }
    catch
    {
        Write-Error "$_`nSkipping: Cannot create .gitignore"
    }

#initalizing git repository
Write-Host "Initailizing new repo"
try{

    #Creating git repository
    #Executin a python file
    powershell -Command "python -u Git-Remote/src/http_request.py '$Auth' '$Repo' '$Description' '$Private'"

    powershell -Command "git init"
    Write-Host "git: Initialized repository"
    powershell -Command "git add ."
    powershell -Command 'git commit . -m "Initial Commit"'
    Write-Host "git: Repository ready to push"
    powershell -Command "python -u Git-Remote\src\put_request.py 'Readme.md' '$Auth' '$User' '$Repo' 'README.md'"
    powershell -Command "python -u Git-Remote\src\put_request.py 'LICENSE' '$Auth' '$User' '$Repo' 'LICENSE'"
    powershell -Command "python -u Git-Remote\src\put_request.py '.gitignore' '$Auth' '$User' '$Repo' '.gitignore'"

    Start-Process "https://github.com/$User/$Repo"
    while(True)
    {
        powershell -Command = "exit"
    }

}
catch{
    Write-Host "Failed to initialize git repository`nCheck your credentials"
}

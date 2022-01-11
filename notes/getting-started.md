# getting started

## contents

- [getting started](#getting-started)
  - [contents](#contents)
  - [introduction](#introduction)
  - [windows installer](#windows-installer)
  - [installing pip](#installing-pip)
  - [chocolatey install](#chocolatey-install)
  - [installing virtual environment](#installing-virtual-environment)
  - [create virtual environment](#create-virtual-environment)

## introduction

this helps a user get started with python

## windows installer

one may download python directly from `https://python.org` 

## installing pip

```powershell
# firstly install python
# next ensure pip is installed
 py -m ensurepip --upgrade
 # upgrade to latest
 py -m pip install --upgrade pip
 ```

## chocolatey install

alternatively one may use the command line to install python 

```powershell
# use admin prompt if upgrading chocolatey to latest version
choco upgrade chocolatey
# editor (or can use vscode)
choco install -y nano
# python3
choco install -y python3
# python package manager 'pip'
python -m pip install --upgrade pip
```

## installing virtual environment

```powershell
# install
py -m pip install --user virtualenv
# then add to path
# C:\Users\<username>\AppData\Roaming\Python\Python310\Scripts
# reboot windows
```

## create virtual environment

```powershell
# create virtual environment
py -m venv env
# activate virtual environment
 .\env\Scripts\activate
 # check you in the virtual environment
 where python
 # (env) PS C:\github\python\standalonePythonFiles>
```
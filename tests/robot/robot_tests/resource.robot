*** Settings ***
Library  SeleniumLibrary
Library  tests/robot/DatabaseLibrary.py
Library  tests/robot/ProjectLibrary.py
Library  tests/robot/ReferenceLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${HOME URL}  http://${SERVER}
${DELAY}  0.3 seconds

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Main Page Should Be Open
    Title Should Be  Viitesovellus

Go To Main Page
    Go To  ${HOME URL}

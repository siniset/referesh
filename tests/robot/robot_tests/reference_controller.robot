*** Settings ***
Resource  tests/robot/robot_tests/resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Save Book Reference
    Set Reference Type  Kirja
    Set Reference Name  SDJLSAFAS
    Set Reference Title  Kirjanen
    Set Reference Author  Leevi
    Set Reference Year  2005
    Set Reference Publisher  Tammi
    Submit Credentials
    Save Reference Should Succeed

*** Test Cases ***
Save Article Reference
    Set Reference Type  Artikkeli
    Set Reference Name  SDJLSAFAS
    Set Reference Title  Kirjanen
    Set Reference Author  Leevi
    Set Reference Year  2005
    Set Reference Publisher  Tammi
    Submit Credentials
    Save Reference Should Succeed

*** Keywords ***
Save Reference Should Succeed
    Main Page Should Be Open

Submit Credentials
    Click Button  button

Set Reference Type
    [Arguments]  ${reference-type}
    Select From List By Label  reference-type  ${reference-type}

Set Reference Name
    [Arguments]  ${reference-name}
    Input Text  reference-name  ${reference-name}

Set Reference Title
    [Arguments]  ${reference-title}
    Input Text  reference-title  ${reference-title}

Set Reference Author
    [Arguments]  ${reference-author}
    Input Text  reference-author  ${reference-author}

Set Reference Year
    [Arguments]  ${reference-year}
    Input Text  reference-year  ${reference-year}

Set Reference Publisher
    [Arguments]  ${reference-publisher}
    Input Text  reference-publisher  ${reference-publisher}
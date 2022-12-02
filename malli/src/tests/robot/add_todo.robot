*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Add Book With Content
    Set Book Content  implement robot tests
    Submit Book
    Home Page Should Be Open
    Page Should Contain  implement robot tests

*** Keywords ***
Set Book Content
    [Arguments]  ${content}
    Input Text  content  ${content}

Submit Todo
    Click Button  Add todo

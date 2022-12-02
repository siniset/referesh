*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create Book And Go To Home Page

*** Test Cases ***
Delete Book
    Page Should Contain  Test Book
    Click Button  Delete
    Home Page Should Be Open
    Page Should Not Contain  Test Book

*** Keywords ***
Create Book And Go To Home Page
    Create Book  Test Book
    Go To Home Page

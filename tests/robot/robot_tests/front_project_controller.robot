*** Settings ***
Resource  tests/robot/robot_tests/resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Create New Project
    Set Project Name  Roboprojekti
    Submit Credentials
    Create Project Should Succeed

*** Keywords ***
Create Project Should Succeed
    Main Page Should Be Open

Submit Credentials
    Click Button  xpath://*[@id="project_button"]

Set Project Name
    [Arguments]  ${project-name}
    Input Text  project-name  ${project-name}
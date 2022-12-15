*** Settings ***
Resource  tests/robot/robot_tests/resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Create New Project
    Create Project  Testiprojekti


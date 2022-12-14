*** Settings ***
Resource  tests/robot/robot_tests/resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Save Book Reference
    ${fields}=  Save Fields  Roni  Matkustelua  1995  Tammi
    Create  Uusi viittaus  book  ${fields}

Save Article Reference
    ${fields}=  Save Fields  Johanna  Elämys  2019  Iltalehti
    Create  Uusi viittaus  article  ${fields}

Delete Reference
    ${newest_id}=  Get Newest Id
    Remove Reference  ${newest_id}

*** Keywords ***
Remove Reference
    [Arguments]  ${id}
    ReferenceLibrary.Delete By Id  ${id}

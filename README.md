![GHA workflow badge](https://github.com/hnenonen/Ohtu_2022/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/hnenonen/Ohtu_2022/branch/main/graph/badge.svg?token=0902d546-2d3a-4f58-8228-4ad52ad2f446)](https://codecov.io/gh/hnenonen/Ohtu_2022)


# Ohjelmistotuotanto, Fall 2022, Group 4

This is a project for Software Engineering course in the fall of 2022 at Helsinki University.

* [Backlog](https://docs.google.com/spreadsheets/d/1p1A37PK2yHurjrkDhkwlJjbcCk2LaQK1XVaVGVVQgHk/edit?usp=sharing)

__Definition of Done__

Toteutetun User storyn toiminnallisuus on ohjelmoitu ja viety tuotantoon. 
Testikattavuus on 90%, testitapaukset ovat mielekkäitä. 
Testit menevät läpi. Pylint ei havaitse koodissa virheitä.

__Sprint reviews__
* meet up at 16:00 to review what to present
* Thursdays 16:30, B120

__Dailys__
* Tuesday 9.45
* Friday 9.45

Useful links:
 * add here if found something useful
 * [Project tasks](https://ohjelmistotuotanto-hy.github.io/speksi/)
 * [Grading](https://ohjelmistotuotanto-hy.github.io/miniprojektin_arvosteluperusteet/)
 * https://ohjelmistotuotanto-hy.github.io/miniprojekti/
 * https://docs.google.com/spreadsheets/d/13RzIZI2NFFuV0zdRjrrfoC-CrootK8AZNuHS571Wlxo/edit#gid=1


__Library room reservation, if you want to come:__
* Monday  8:00 - 10.00, G103g
* Tuesday 8:00 - 10.00, G103g
* Friday 8:00 - 10.00, G103g

(The last reserved instance for G103g for us is at Friday 16.12.)

## Instructions

### Testing

Our objective is to achieve the 90% test coverage we have agreed upon.
Thus we are aiming at reasonable tests that bring concrete value to our workflow. Currently we are working on unit tests with Pytest and test automation with
Robot Framework. Testing infrastructure is simple and easy to use; there's hardly any direct monipulation of databases and tables by hand, and database's content
is cleared and schema is re-created between test units.

#### Usage

* `invoke test`
  * Run project's tests with pytest. Requires a reachable postgres database.

Note that testing of this application requires setting `TEST_DATABASE_URL` environment variable containing URI of the test databases.

#### Testing database

__docker-compose__

Run `docker-compose up --build` to build containers and run the tests. First run may take a little longer as all required packages and dependencies must be downloaded.
After tests are run, the runner can be quit by pressing Ctrl-C. Runner returns a plain old Unix status code where zero signifies a successful and non-zero an unsuccessful test run.

__Manual orchestration__
\\\
  Manual orchestration requires taking care of the test database. You may use a local postgres instance and create a new database for the test runner, or use the existing invoke tasks for managing the server.

  * `invoke run_test_server`
    * Create a new test server instance if there isn't already another one.
  * `invoke start_test_server`
    * Start test server if one exists and is not running.
  * `invoke stop_test_server`
    * Stop test server container if one exists and is running.

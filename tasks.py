from invoke import task


@task
def start(ctx):
    ctx.run("flask --app app.app:app --debug run --host=0.0.0.0")


@task
def test(ctx):
    ctx.run("python3 -m pytest", pty=True)


@task
def robot_test(ctx):
    ctx.run("""BROWSER=headlesschrome SERVER=localhost:5000
        robot tests/robot/robot_tests""", pty=True)


@task
def test_win(ctx):
    ctx.run("python3 -m pytest", pty=False)


@task
def run_test_server(ctx):
    ctx.run("""sudo docker run --name ohtu-test-runner -p 5432:5432
        -e POSTGRES_PASSWORD=ohtu -d postgres""")


@task
def start_test_server(ctx):
    ctx.run("sudo docker start ohtu-test-runner")


@task
def stop_test_server(ctx):
    ctx.run("sudo docker stop ohtu-test-runner")


@task
def lint(ctx):
    ctx.run("flake8", pty=True)


@task
def lint_win(ctx):
    ctx.run("flake8", pty=False)


@task
def format(ctx):
    ctx.run("autopep8 --aggressive --in-place --recursive app tests")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

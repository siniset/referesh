from invoke import task


@task
def start(ctx):
    ctx.run("flask --app app.app:app --debug run")


@task
def test(ctx):
    ctx.run("python3 -m pytest", pty=True)


@task
def test_win(ctx):
    ctx.run("python3 -m pytest", pty=False)


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

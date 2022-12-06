from invoke import task


@task
def start(ctx):
    """_summary_

    Args:
        ctx (_type_): _description_
    """
    ctx.run("flask --app app.app:app --debug run --host=0.0.0.0")


@task
def test(ctx):
    """_summary_

    Args:
        ctx (_type_): _description_
    """
    ctx.run("python3 -m pytest", pty=True)


@task
def test_win(ctx):
    """_summary_

    Args:
        ctx (_type_): _description_
    """
    ctx.run("python3 -m pytest", pty=False)


@task
def lint(ctx):
    """_summary_

    Args:
        ctx (_type_): _description_
    """
    ctx.run("flake8", pty=True)


@task
def lint_win(ctx):
    """_summary_

    Args:
        ctx (_type_): _description_
    """
    ctx.run("flake8", pty=False)


@task
def format(ctx):
    """_summary_

    Args:
        ctx (_type_): _description_
    """
    ctx.run("autopep8 --aggressive --in-place --recursive app tests")


@task
def coverage(ctx):
    """_summary_

    Args:
        ctx (_type_): _description_
    """
    ctx.run("coverage run --branch -m pytest", pty=True)


@task(coverage)
def coverage_report(ctx):
    """_summary_

    Args:
        ctx (_type_): _description_
    """
    ctx.run("coverage html", pty=True)

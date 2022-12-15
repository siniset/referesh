import sys
import logging
from invoke import task


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
pty = sys.platform != "win32"


@task
def start(ctx):
    ctx.run("MODE=development flask --app app.app:app \
        --debug run --host=0.0.0.0", pty=pty)


@task
def launch(ctx):
    ctx.run("MODE=production gunicorn -b 0.0.0.0:8080 app.app:app", pty=pty)


@task
def test(ctx, unit=False, robot=False, all=False):
    if all:
        test(ctx, unit=True, robot=True)
    elif unit:
        ctx.run("MODE=test python3 -m pytest", pty=pty)
    elif robot:
        ctx.run("MODE=test robot tests/robot/robot_tests", pty=pty)
    else:
        logging.error("No tests specified.")

@task
def test_win(ctx):
    ctx.run("python -m pytest")
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
    ctx.run("flake8", pty=pty)


@task
def format(ctx):
    ctx.run("autopep8 --aggressive --in-place --recursive app tests")


@task
def coverage(ctx):
    ctx.run("MODE=test coverage run -m pytest", pty=pty)


@task(coverage)
def coverage_report(ctx, type="report"):
    ctx.run(f"coverage {type}", pty=pty)

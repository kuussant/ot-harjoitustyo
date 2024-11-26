from invoke import task
from subprocess import call
from sys import platform

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("poetry run pytest", pty=True)

@task
def coverage_report(ctx):
    ctx.run("coverage run --branch -m pytest; coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))
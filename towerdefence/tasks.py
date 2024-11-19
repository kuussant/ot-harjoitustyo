from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("poetry run pytest", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest; coverage html", pty=True)
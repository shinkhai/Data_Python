"""tasks.py

"""
from invoke import task


@task
def tests(ctx):
    cmd = "pytest"
    ctx.run(cmd)


@task(tests)
def run(ctx):
    pass

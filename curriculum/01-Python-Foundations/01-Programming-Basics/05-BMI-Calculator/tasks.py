"""
=========
Tasks
=========
"""
from invoke import task


@task
def tests(ctx):
    cmd = "pytest -v"
    ctx.run(cmd)


@task(tests)
def run(ctx):
    pass

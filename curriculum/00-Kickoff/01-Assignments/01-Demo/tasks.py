"""
Tasks file
"""
from invoke import task, run


@task
def tests(ctx):
    cmd = "pytest -v"
    ctx.run(cmd)


@task(tests)
def run(ctx):
    pass

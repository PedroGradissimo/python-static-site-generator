# Typer is a built-in library for building CLI applications
import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}
    Site(**config).build()


typer.run(main)

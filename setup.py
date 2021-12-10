"""This module contains the packaging routine for the pybook package"""

from setuptools import setup, find_packages
import pathlib

import pkg_resources


def get_requirements(source):
    """Get the requirements from the given ``source``

    Parameters
    ----------
    source: str
        The filename containing the requirements

    """

    with pathlib.Path(source).open() as requirements_txt:
        install_requires = [
            str(requirement)
            for requirement
            in pkg_resources.parse_requirements(requirements_txt)
        ]

        return install_requires

    # install_reqs = parse_requirements(filename=source, session=PipSession())

    # return [str(ir.req) for ir in install_reqs]




setup(
    packages=find_packages(),
    install_requires=get_requirements('requirements/requirements.txt')
)



from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of dependencies from a file.
    """
    requirements = []
    try:
        with open(file_path, "r") as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements if req.strip()]

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print(f"⚠️ Warning: {file_path} not found. Ensure it exists.")
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")

    return requirements


setup(
    name="project",
    version="0.0.1",
    author="Mohammed Mishal",
    author_email="mohamedmishal430@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)

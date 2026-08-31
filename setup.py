"""
FTA/ETA Editor Setup
"""

from setuptools import setup
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="fta-eta-editor",
    version="1.5.1",
    author="makkiblog.com",
    author_email="",
    description="Fault Tree and Event Tree Analysis Editor with advanced probability calculations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gertrud-Violett/FTA_editor",
    # src/ contains flat top-level modules (no __init__.py packages), so
    # find_packages(where="src") finds nothing and the distribution would be
    # empty. List the modules explicitly via py_modules instead.
    py_modules=[
        "FTA_Editor_UI",
        "FTA_Editor_core",
        "AI_agent_handler",
        "ai_providers",
        "json_viewer",
        "mermaid_exporter",
    ],
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
    },
    entry_points={
        "console_scripts": [
            "fta-editor=FTA_Editor_UI:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.md"],
    },
    keywords="fault-tree event-tree analysis reliability safety probability",
    project_urls={
        "Bug Reports": "https://github.com/Gertrud-Violett/FTA_editor/issues",
        "Source": "https://github.com/Gertrud-Violett/FTA_editor",
        "Documentation": "https://github.com/Gertrud-Violett/FTA_editor/tree/main/docs",
    },
)

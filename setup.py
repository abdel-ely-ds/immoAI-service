from setuptools import setup

TEST_DEPS = ["pytest==5.0.1", "pytest-runner==5.1", "pytest-cov==2.7.1", "nox"]

setup(
    name="immo",
    keywords="core",
    license="MIT",
    description="LLM api for immo",
    long_description="file: README.md",
    classifiers=["Programming Language :: Python :: 3.10"],
    zip_safe=True,
    include_package_data=True,
    entry_points={"console_scripts": ["immo-run=immo.main:main"]},
    package_dir={"": "src"},
    install_requires=[
        "uvicorn",
        "fastapi",
        "numpy",
        "pandas",
        "openai",
        "pinecone-client",
        "tiktoken",
        "langchain",
    ],
    tests_require=TEST_DEPS,
    extras_require={"test": TEST_DEPS},
)

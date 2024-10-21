import urllib.request
from pathlib import Path

import pytest


@pytest.fixture()
def test_data_dir() -> Path:
    return Path(__file__).parent.joinpath("data")


@pytest.fixture()
def sample_isyntax_file(test_data_dir: Path) -> Path:
    file = test_data_dir / "testslide.isyntax"
    if not file.is_file():
        with Path.open(file, "wb") as f:
            f.write(
                urllib.request.urlopen(
                    "https://zenodo.org/record/5037046/files/testslide.isyntax",
                ).read(),
            )
    return file

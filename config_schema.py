from dataclasses import dataclass

@dataclass
class Config:
    package_name: str
    repository_url: str
    test_repo_path: str
    mode: str
    output_image: str
    ascii_output: bool
    max_depth: int

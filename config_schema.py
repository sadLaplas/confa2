from dataclasses import dataclass

@dataclass
class Config:
    package_name: str
    repository_url: str
    test_path: str
    mode: str
    output: bool
    max_depth: int

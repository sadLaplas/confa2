from dataclasses import dataclass

@dataclass
class Config:
    package_name: str
    repository_url: str
    mode: str
    output_image: str
    output: bool
    max_depth: int
    test_path: str = None

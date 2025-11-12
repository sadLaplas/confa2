import gzip
import urllib.request


def download_packages_index(repo_url: str) -> str:
    url = repo_url.rstrip("/") + "/Packages.gz"

    try:
        print(f"Загрузка индекса пакетов: {url}")
        with urllib.request.urlopen(url) as response:
            compressed_data = response.read()

        data = gzip.decompress(compressed_data).decode("utf-8", errors="ignore")
        return data
    except Exception as e:
        raise RuntimeError(f"Не удалось загрузить файл Packages.gz: {e}")


def parse_direct_dependencies(package_name: str, package_index: str) -> list[str]:
    blocks = package_index.split("\n\n")

    for block in blocks:
        if block.startswith(f"Package: {package_name}"):
            for line in block.splitlines():
                if line.startswith("Depends:"):
                    deps_line = line.split("Depends:")[1].strip()

                    deps = []
                    for dep in deps_line.split(","):
                        clean = dep.split("|")[0].strip().split(" ")[0]
                        deps.append(clean)

                    return deps

            return []

    raise ValueError(f"Пакет '{package_name}' не найден в индексе репозитория.")

import os

def validate_config(config: dict):
    required = [
        "package_name", "repository_url", "test_path", "mode", "output", "max_depth"
    ]
    for key in required:
        if key not in config:
            raise KeyError(f"Отсутствует обязательный параметр: {key}")

    if config["mode"] not in ("url", "file"):
        raise ValueError("Параметр 'mode' должен быть 'url' или 'file'.")

    if config["output"] not in [True, False]:
        raise TypeError("Параметр 'output' должен быть логическим значением true/false.")

    if not isinstance(config["max_depth"], int) or config["max_depth"] <= 0:
        raise ValueError("Параметр 'max_depth' должен быть положительным числом.")

    if config["mode"] == "file" and not os.path.exists(config["test_path"]):
        raise FileNotFoundError(f"Путь '{config['test_path']}' не существует.")

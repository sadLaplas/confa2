import os

def validate_config(data: dict):
    required = [
        "package_name", "repository_url", "test_repo_path", "mode",
        "output_image", "ascii_output", "max_depth"
    ]
    for key in required:
        if key not in data:
            raise KeyError(f"Отсутствует обязательный параметр: {key}")

    if data["mode"] not in ("url", "file"):
        raise ValueError("Параметр 'mode' должен быть 'url' или 'file'.")

    if not isinstance(data["ascii_output"], bool):
        raise TypeError("Параметр 'ascii_output' должен быть логическим значением true/false.")

    if not isinstance(data["max_depth"], int) or data["max_depth"] <= 0:
        raise ValueError("Параметр 'max_depth' должен быть положительным числом.")

    if data["mode"] == "file" and not os.path.exists(data["test_repo_path"]):
        raise FileNotFoundError(f"Путь '{data['test_repo_path']}' не существует.")

import yaml
from config_schema import Config
from utils.validators import validate_config

def load_config(path: str) -> Config:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл конфигурации '{path}' не найден.")
    except yaml.YAMLError as e:
        raise ValueError(f"Ошибка разбора YAML: {e}")

    validate_config(data)

    return Config(**data)

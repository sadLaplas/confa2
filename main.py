import argparse
from config_loader import load_config

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Путь к YAML-файлу конфигурации")
    args = parser.parse_args()

    try:
        config = load_config(args.config)
        print("Конфигурация успешно загружена:\n")
        for key, value in vars(config).items():
            print(f"{key} = {value}")
    except Exception as e:
        print(f"[Ошибка] {e}")

if __name__ == "__main__":
    main()

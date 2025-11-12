import argparse
from config_loader import load_config
from data_collector import download_packages_index, parse_direct_dependencies

def main():
    parser = argparse.ArgumentParser(description="Dependency Graph Tool")
    parser.add_argument("--config", required=True, help="Путь к YAML-файлу конфигурации")
    args = parser.parse_args()

    try:
        config = load_config(args.config)
    except Exception as e:
        print(f"[Ошибка конфигурации] {e}")
        return

    print("\nЗагруженные параметры конфигурации:")
    for key, value in config.__dict__.items():
        print(f"  {key}: {value}")
    if config.mode == "url":
        try:
            index_data = download_packages_index(config.repository_url)
            deps = parse_direct_dependencies(config.package_name, index_data)
            print(f"\nПрямые зависимости пакета '{config.package_name}':")
            if deps:
                for dep in deps:
                    print(f" - {dep}")
            else:
                print(" (Нет зависимостей)")
        except Exception as e:
            print(f"[Ошибка при анализе зависимостей] {e}")

if __name__ == "__main__":
    main()

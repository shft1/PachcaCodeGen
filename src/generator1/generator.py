import subprocess
import sys

MIN_ARGS = 2
COMMAND_INDEX = 1
GENERATE_COMMAND = "generate"
INSTALL_TEST_COMMAND = "test"


def run_command(command):
    """Функция для выполнения команды в терминале."""
    try:
        subprocess.run(command, check=True, shell=True, text=True)
        print(f"Команда выполнена: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды: {command}\nКод ошибки: {e.returncode}\nВывод:\n{e.stderr}")

def generate_client():
    """Генерация клиента и запуск скрипта-генератора."""
    print("Генерация клиента...")
    run_command("openapi-python-client generate --path openapi.yaml --custom-template-path=./templates --overwrite")
    run_command("python script.py")

def install_and_run_tests():
    """Установка пакета и запуск тест-запросов."""
    print("Установка пакета и запуск тест-запросов...")
    run_command("pip install ./pachca-api-open-api-3-0-client")
    run_command("python pachca.py")

if __name__ == "__main__":
    if len(sys.argv) < MIN_ARGS:
        print("Пример команды: python generator.py [generate|test]")
        sys.exit(COMMAND_INDEX)

    command = sys.argv[COMMAND_INDEX]
    commands = {
        GENERATE_COMMAND: generate_client,
        INSTALL_TEST_COMMAND: install_and_run_tests,
    }
    if command in commands:
        commands[command]()
    else:
        print("Некорректный аргумент. Введите 'generate' для генерации клиента или 'test' для запуска тестов.")
        sys.exit(COMMAND_INDEX)



# import subprocess
# import sys

# def run_command(command):
#     """Функция для выполнения команды в терминале."""
#     try:
#         subprocess.run(command, check=True, shell=True, text=True)
#         print(f"Команда выполнена: {command}")
#     except subprocess.CalledProcessError as e:
#         print(f"Ошибка при выполнении команды: {command}\nКод ошибки: {e.returncode}\nВывод:\n{e.stderr}")

# def generate_client():
#     """Генерация клиента и запуск скрипта-генератора."""
#     print("Генерация клиента...")
#     run_command("openapi-python-client generate --path openapi.yaml --custom-template-path=./templates --overwrite")
#     run_command("python script.py")

# def install_and_run_tests():
#     """Установка пакета и запуск тест-запросов."""
#     print("Установка пакета и запуск тест-запросов...")
#     run_command("pip install ./pachca-api-open-api-3-0-client")
#     run_command("python pachca.py")

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Пример команды: python generator.py [generate|test]")
#         sys.exit(1)

#     option = sys.argv[1]

#     if option == "generate":
#         generate_client()
#     elif option == "test":
#         install_and_run_tests()
#     else:
#         print("Некорректный аргумент. Введите 'generate' для генерации клиента или 'test' для запуска тестов.")
#         sys.exit(1)

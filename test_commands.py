import pytest
from commands import CommandInterpreter

# Пример обработчика команды для игрового объекта "Tank"
def tank_command_handler(command):
    action = command['action']
    if action == 'StartMove':
        velocity = command.get('initialVelocity', 0)
        return f"Танк начал двигаться со скоростью {velocity}"
    elif action == 'StopMove':
        return "Танк остановился"
    elif action == 'Fire':
        return "Танк выпустил снаряд"
    else:
        return "Неизвестное действие для танка"

# Пример обработчика команды для игрового объекта "Ship"
def ship_command_handler(command):
    action = command['action']
    if action == 'StartSail':
        speed = command.get('initialSpeed', 0)
        return f"Корабль начал плавать со скоростью {speed}"
    elif action == 'StopSail':
        return "Корабль остановился"
    else:
        return "Неизвестное действие для корабля"

def test_execute_command():
    interpreter = CommandInterpreter()

    # Регистрация обработчиков команд для объектов
    interpreter.register_command_handler('Tank', tank_command_handler)
    interpreter.register_command_handler('Ship', ship_command_handler)

    # Добавление объектов в игру
    interpreter.add_object("tank1", "player1")
    interpreter.add_object("ship1", "player2")

    # Выполнение команд
    result1 = interpreter.execute_command({
        "ID": "tank1",
        "type": "Tank",
        "action": "StartMove",
        "initialVelocity": 2
    }, "player1")

    result2 = interpreter.execute_command({
        "ID": "ship1",
        "type": "Ship",
        "action": "StartSail",
        "initialSpeed": 5
    }, "player2")

    result3 = interpreter.execute_command({
        "ID": "tank1",
        "type": "Tank",
        "action": "Fire"
    }, "player1")

    # Попытка выполнить команду для несуществующего объекта
    with pytest.raises(PermissionError):
        interpreter.execute_command({
            "ID": "nonexistent",
            "type": "Tank",
            "action": "StartMove",
            "initialVelocity": 2
        }, "player1")

    assert result1 == "Танк начал двигаться со скоростью 2"
    assert result2 == "Корабль начал плавать со скоростью 5"
    assert result3 == "Танк выпустил снаряд"

if __name__ == "__main__":
    pytest.main()

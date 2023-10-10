class CommandInterpreter:
    def __init__(self):
        self.objects = {}  # Словарь для хранения объектов и их владельцев
        self.command_handlers = {}  # Словарь для хранения обработчиков команд

    def add_object(self, object_id, owner_id):
        self.objects[object_id] = owner_id

    def register_command_handler(self, object_type, handler):
        self.command_handlers[object_type] = handler

    def execute_command(self, command, player_id):
        if command['ID'] not in self.objects:
            return "Объект не найден"
        
        object_owner = self.objects[command['ID']]
        if object_owner != player_id:
            raise PermissionError("Вы не можете управлять этим объектом")

        object_type = command.get('type', 'default')
        handler = self.command_handlers.get(object_type, self.default_command_handler)
        return handler(command)

    def default_command_handler(self, command):
        return "Неизвестная команда"

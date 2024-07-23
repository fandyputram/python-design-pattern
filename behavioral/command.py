from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete command implementations
class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()

# Receiver
class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

# Invoker
class RemoteControl:
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands:
            self._commands[command_name].execute()
        else:
            print("Command not found")

# Example usage
light = Light()
light_on_command = LightOnCommand(light)
light_off_command = LightOffCommand(light)

remote_control = RemoteControl()
remote_control.register("on", light_on_command)
remote_control.register("off", light_off_command)

remote_control.execute("on")
remote_control.execute("off")
remote_control.execute("invalid")


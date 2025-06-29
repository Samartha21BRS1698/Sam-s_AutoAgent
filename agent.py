# code to design agent loop with improved tool handling

class AutoAgent:
    def __init__(self):
        self.memory = []
        self.tools = {}

    def register_tool(self, name, func):
        self.tools[name] = func

    def run(self, task: str):
        print(f"[Agent Task]: {task}")
        while True:
            thought = input("Thought: ")
            action = input("Action (tool name): ")
            action_input = input("Input to tool: ")

            if action == "finish":
                print("Task completed.")
                break

            if action not in self.tools:
                print(f"Tool '{action}' not found.")
                continue

            try:
                result = self.tools[action](action_input)
            except Exception as e:
                result = f"Tool Error: {str(e)}"

            print(f"Observation:\n{result}")
            self.memory.append((thought, action, action_input, result))

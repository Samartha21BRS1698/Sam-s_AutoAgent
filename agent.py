# code to design agent loop
class AutoAgent:
    def __init__(self):
        self.memory = []  # Will replace with real memory later
        self.tools = {}   # Tool name → function map

    def register_tool(self, name, func):
        self.tools[name] = func

    def run(self, task: str):
        print(f"[Agent Task]: {task}")
        while True:
            thought = input("🤖 Thought: ")
            action = input("🔧 Action (tool name): ")
            action_input = input("📝 Input to tool: ")

            if action == "finish":
                print("✅ Task completed.")
                break

            if action not in self.tools:
                print("❌ Unknown tool.")
                continue

            observation = self.tools[action](action_input)
            print(f"👁️ Observation: {observation}")

            # Add to memory (temporary)
            self.memory.append((thought, action, action_input, observation))

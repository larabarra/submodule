import json
import os
import random

# Configurações básicas
FOLDER_NAME = "data_import"
TASKS_COUNT = 5

# Dados para popular os arquivos
task_types = ["Glúteos", "Estudo API", "Refatoração SQL", "Cardio", "Node.js"]
difficulties = ["Easy", "Medium", "Hard", "Legendary"]

def create_mock_data():
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)
        print(f"Diretório '{FOLDER_NAME}' criado.")

    for i in range(1, TASKS_COUNT + 1):
        task_data = {
            "id": i,
            "task_name": random.choice(task_types),
            "difficulty": random.choice(difficulties),
            "exp_reward": random.randint(100, 500),
            "status": "pending"
        }
        
        file_path = os.path.join(FOLDER_NAME, f"quest_{i}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(task_data, f, indent=4, ensure_ascii=False)
            
    print(f"Sucesso: {TASKS_COUNT} arquivos gerados em '{FOLDER_NAME}'.")

if __name__ == "__main__":
    create_mock_data()
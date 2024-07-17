from locust import HttpUser, TaskSet, task, between

class CalculatorTasks(TaskSet):
    @task
    def load_homepage(self):
        self.client.get("/")

    @task
    def add(self):
        self.client.post("/", {
            "num1": "5",
            "num2": "3",
            "operation": "add"
        })

    @task
    def subtract(self):
        self.client.post("/", {
            "num1": "10",
            "num2": "4",
            "operation": "subtract"
        })

    @task
    def multiply(self):
        self.client.post("/", {
            "num1": "7",
            "num2": "6",
            "operation": "multiply"
        })

    @task
    def divide(self):
        self.client.post("/", {
            "num1": "8",
            "num2": "2",
            "operation": "divide"
        })

class CalculatorUser(HttpUser):
    tasks = [CalculatorTasks]
    wait_time = between(1, 5)  # wait time between tasks

    def on_start(self):
        """ on_start is called when a Locust user starts before any task is scheduled """
        self.client.get("/")

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

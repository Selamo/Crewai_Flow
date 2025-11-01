from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class MyFirstCrew():
        """My First Crew - A Simple Blog Writing Crew"""
        # The agents_config and tasks_config tell CrewAI where to find
        # your YAML files
        agents_config = 'config/agents.yaml'
        tasks_config = 'config/tasks.yaml'
        # This decorator tells CrewAI this method creates an agent
        # It will automatically load the 'researcher' config from agents.yaml
        @agent
        def researcher(self) -> Agent:
                return Agent(
                    config=self.agents_config['researcher'],
                    verbose=True
                )
        
        @agent
        def writer(self) -> Agent:
                return Agent(
                    config=self.agents_config['writer'],
                    verbose=True
                )
        # Load the research task
        @task
        def research_task(self) -> Task:
                return Task(
                    config=self.tasks_config['research_task'],
                )
        # Load the writing task
        @task
        def writing_task(self) -> Task:
                return Task(
                    config=self.tasks_config['writing_task'],
                )
        # This method brings everything together
        @crew
        def crew(self) -> Crew:
                """Creates the crew with all agents and tasks"""
                return Crew(
                    agents=self.agents, # Automatically includes all agents
                    tasks=self.tasks, # Automatically includes all tasks
                    process=Process.sequential, # Tasks run one after another
                    verbose=True
                )
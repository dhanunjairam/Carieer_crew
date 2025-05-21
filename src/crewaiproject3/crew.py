from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
import os
@CrewBase
class Crewaiproject3():
    """Crewaiproject3 crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    my_LLM = LLM(
        api_key=os.getenv("OPENROUTER_API_KEY"),  # Replace with your actual API key
        model="openrouter/nvidia/llama-3.1-nemotron-70b-instruct",   
        # max_completion_tokens=100,
    )
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def career_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['career_analyst'],
            verbose=True,
            tools= [SerperDevTool()],
            llm=self.my_LLM

        )

    @agent
    def roadmap_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['roadmap_designer'],
            verbose=True,
            llm=self.my_LLM
        )
    @agent
    def resume_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_advisor'],
            verbose=True,
            llm=self.my_LLM
        )
    
    @agent 
    def course_recommender(self) -> Agent:
        return Agent(
            config= self.agents_config['course_recommender'],
            verbose=True,
            tools= [SerperDevTool()],
            llm=self.my_LLM
            
        )
    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
 

    @task
    def analyze_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_task'],
        
        )
    
    @task 
    def generate_roadmap_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_roadmap_task'],
        )
    
    @task
    def generate_resume_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_resume_task'],
        )
    
    @task
    def recommend_courses_task(self) -> Task:
        return Task(
            config=self.tasks_config['recommend_courses_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Crewproject1 crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            # tasks=self.tasks, # Automatically created by the @task decorator
            tasks=[self.analyze_task(),
            self.generate_roadmap_task(),
            self.generate_resume_task(),
            self.recommend_courses_task()],
            process=Process.sequential,
            verbose=True,
            memory=True,
            LLM=self.my_LLM,
          
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

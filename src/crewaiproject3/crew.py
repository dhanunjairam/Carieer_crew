# from crewai import Agent, Crew, Process, Task,LLM
# from crewai.project import CrewBase, agent, crew, task
# from crewai_tools import SerperDevTool
# # If you want to run a snippet of code before or after the crew starts,
# # you can use the @before_kickoff and @after_kickoff decorators
# # https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
# import os
# @CrewBase
# class Crewaiproject3():
#     """Crewaiproject3 crew"""

#     # Learn more about YAML configuration files here:
#     # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
#     # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
#     agents_config = 'config/agents.yaml'
#     tasks_config = 'config/tasks.yaml'
#     my_LLM = LLM(
#         api_key=os.getenv("OPENROUTER_API_KEY"),  # Replace with your actual API key
#         model="openrouter/nvidia/llama-3.1-nemotron-70b-instruct",   
#         # max_completion_tokens=100,
#     )
#     # If you would like to add tools to your agents, you can learn more about it here:
#     # https://docs.crewai.com/concepts/agents#agent-tools
#     @agent
#     def career_analyst(self) -> Agent:
#         return Agent(
#             config=self.agents_config['career_analyst'],
#             verbose=True,
#             tools= [SerperDevTool()],
#             llm=self.my_LLM

#         )

#     @agent
#     def roadmap_designer(self) -> Agent:
#         return Agent(
#             config=self.agents_config['roadmap_designer'],
#             verbose=True,
#             llm=self.my_LLM
#         )
#     @agent
#     def resume_advisor(self) -> Agent:
#         return Agent(
#             config=self.agents_config['resume_advisor'],
#             verbose=True,
#             llm=self.my_LLM
#         )
    
#     @agent 
#     def course_recommender(self) -> Agent:
#         return Agent(
#             config= self.agents_config['course_recommender'],
#             verbose=True,
#             tools= [SerperDevTool()],
#             llm=self.my_LLM
            
#         )
#     # To learn more about structured task outputs,
#     # task dependencies, and task callbacks, check out the documentation:
#     # https://docs.crewai.com/concepts/tasks#overview-of-a-task
 

#     @task
#     def analyze_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['analyze_task'],
        
#         )
    
#     @task 
#     def generate_roadmap_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['generate_roadmap_task'],
#         )
    
#     @task
#     def generate_resume_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['generate_resume_task'],
#         )
    
#     @task
#     def recommend_courses_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['recommend_courses_task'],
#         )

#     @crew
#     def crew(self) -> Crew:
#         """Creates the Crewproject1 crew"""
#         # To learn how to add knowledge sources to your crew, check out the documentation:
#         # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

#         return Crew(
#             agents=self.agents, # Automatically created by the @agent decorator
#             # tasks=self.tasks, # Automatically created by the @task decorator
#             tasks=[self.analyze_task(),
#             self.generate_roadmap_task(),
#             self.generate_resume_task(),
#             self.recommend_courses_task()],
#             process=Process.sequential,
#             verbose=True,
#             memory=True,
#             LLM=self.my_LLM,
          
#             # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
#         )


# from crewai import Agent, Crew, Process, Task,LLM
# from crewai.project import CrewBase, agent, crew, task
# from crewai_tools import SerperDevTool



# # If you want to run a snippet of code before or after the crew starts,
# # you can use the @before_kickoff and @after_kickoff decorators
# # https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
# from pydantic import BaseModel


# class OutModel(BaseModel):
#     task_title: str
#     task_output: str
# class CompleteOutput(BaseModel):
#     analysis_result: str
#     roadmap_result: str
#     resume_result: str
#     courses_result: str
# import os
# @CrewBase
# class Crewaiproject3():
#     """Crewaiproject3 crew"""
    
#     # Learn more about YAML configuration files here:
#     # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
#     # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
#     agents_config = 'config/agents.yaml'
#     tasks_config = 'config/tasks.yaml'
#     my_LLM = LLM(
#         api_key=os.getenv("OPENROUTER_API_KEY"),  # Replace with your actual API key
#         model="openrouter/nvidia/llama-3.1-nemotron-ultra-253b-v1:free",   
#         base_url="https://openrouter.ai/api/v1"
#         # max_completion_tokens=100,
#     )

#     # If you would like to add tools to your agents, you can learn more about it here:
#     # https://docs.crewai.com/concepts/agents#agent-tools
#     @agent
#     def career_analyst(self) -> Agent:
#         return Agent(
#             config=self.agents_config['career_analyst'],
#             verbose=True,
#             tools= [SerperDevTool()],
#             llm=self.my_LLM

#         )

#     @agent
#     def roadmap_designer(self) -> Agent:
#         return Agent(
#             config=self.agents_config['roadmap_designer'],
#             verbose=True,
#             llm=self.my_LLM
#         )
#     @agent
#     def resume_advisor(self) -> Agent:
#         return Agent(
#             config=self.agents_config['resume_advisor'],
#             verbose=True,
#             llm=self.my_LLM
#         )
    
#     @agent 
#     def course_recommender(self) -> Agent:
#         return Agent(
#             config= self.agents_config['course_recommender'],
#             verbose=True,
#             tools= [SerperDevTool()],
#             llm=self.my_LLM
            
#         )
#     @agent
#     def final_reporter(self) -> Agent:
#         return Agent(
#             config=self.agents_config['final_reporter'],
#             llm=self.my_LLM
#         )
#     # To learn more about structured task outputs,
#     # task dependencies, and task callbacks, check out the documentation:
#     # https://docs.crewai.com/concepts/tasks#overview-of-a-task

#     @task
#     def analyze_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['analyze_task'],
#             output_pydantic=OutModel,
        
#         )
#     @task 
#     def generate_roadmap_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['generate_roadmap_task'],
#             output_pydantic=OutModel,
#         )
    
#     @task
#     def generate_resume_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['generate_resume_task'],
#             output_pydantic=OutModel,
#         )
    
#     @task
#     def recommend_courses_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['recommend_courses_task'],
#             output_pydantic=OutModel,
#         )
#     @task
#     def generate_final_report_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['generate_final_report_task'],
#             output_pydantic=CompleteOutput,
#             context=[self.analyze_task(), self.generate_roadmap_task(), self.generate_resume_task(), self.recommend_courses_task()],
#         )

#     @crew
#     def crew(self) -> Crew:
#         """Creates the Crewproject1 crew"""
#         # To learn how to add knowledge sources to your crew, check out the documentation:
#         # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

#         return Crew(
#             agents=[self.career_analyst(),self.roadmap_designer(),self.resume_advisor(),self.course_recommender(),self.final_reporter()], # Automatically created by the @agent decorator
#             tasks=[self.analyze_task(),
#             self.generate_roadmap_task(),
#             self.generate_resume_task(),
#             self.recommend_courses_task(),self.generate_final_report_task()], # Automatically created by the @task decorator
#             process=Process.sequential,
#             verbose=True,
#             llm=self.my_LLM,
#             #process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
#         )


from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from pydantic import BaseModel
import os
from typing import Optional
import json

class OutModel(BaseModel):
    task_title: str
    task_output: str

class CompleteOutput(BaseModel):
    task_title: str
    career_analysis: str
    strategic_roadmap: str
    resume_template: str
    learning_resources: str



@CrewBase
class Crewaiproject3:
    """Career Development Crew - Comprehensive career guidance and planning"""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY environment variable is required")
    
    my_LLM = LLM(
            api_key=api_key,
            model="openrouter/anthropic/claude-3-haiku",   
            base_url="https://openrouter.ai/api/v1",
           
        )
     
    def validate_json_output(self,result):
        try:
            if hasattr(result, 'raw'):
                data = json.loads(result.raw)
            else:
                data = json.loads(str(result))
            return True, data
        except json.JSONDecodeError as e:
            return False, f"Invalid JSON format: {str(e)}"
    # Add validation to your task
    

    @agent
    def career_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['career_analyst'],
            verbose=True,
            tools=[SerperDevTool()],
            llm=self.my_LLM,
            function_calling_llm = self.my_LLM,
            max_iter=3,  # Limit iterations
            max_rpm=10   # Rate limiting
        )

    @agent
    def roadmap_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['roadmap_designer'],
            # verbose=True,
            llm=self.my_LLM,
            function_calling_llm = self.my_LLM,
            max_iter=3,  # Limit iterations
            max_rpm=10   # Rate limiting
           
        )
    
    @agent
    def resume_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_advisor'],
            # verbose=True,
            llm=self.my_LLM,
            function_calling_llm = self.my_LLM,
            max_iter=3,  # Limit iterations
            max_rpm=10   # Rate limiting
          
        )
    
    @agent 
    def course_recommender(self) -> Agent:
        return Agent(
            config=self.agents_config['course_recommender'],
            # verbose=True,
            tools=[SerperDevTool()],
            llm=self.my_LLM,
            function_calling_llm = self.my_LLM,
            max_iter=3,  # Limit iterations
            max_rpm=10   # Rate limiting
            
        )
    
    @agent
    def final_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['final_reporter'],
            llm=self.my_LLM,
            function_calling_llm = self.my_LLM,
            # verbose=True,
            max_iter=3,  # Limit iterations
            max_rpm=10   # Rate limiting
            
        )

    @task
    def analyze_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_task'],
            agent=self.career_analyst(),
            output_pydantic=OutModel,
            # context=[self.analyze_task()]
        )
    
    @task 
    def generate_roadmap_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_roadmap_task'],
            agent=self.roadmap_designer(),
            output_pydantic=OutModel,
            context=[self.analyze_task()]
            
        )
    
    @task
    def generate_resume_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_resume_task'],
            agent=self.resume_advisor(),
            output_pydantic=OutModel,
            context=[self.analyze_task()]
           
        )
    
    @task
    def recommend_courses_task(self) -> Task:
        return Task(
            config=self.tasks_config['recommend_courses_task'],
            agent=self.course_recommender(),
            context=[self.analyze_task()],
            output_pydantic=OutModel,
            
        )
    
    @task
    def generate_final_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_final_report_task'],
            agent=self.final_reporter(),
            output_pydantic=CompleteOutput,
            context=[
                self.analyze_task(), 
                self.generate_roadmap_task(), 
                self.generate_resume_task(), 
                self.recommend_courses_task()
            ],
            guardrail= self.validate_json_output,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Career Development crew"""
        return Crew(
            agents=[
                self.career_analyst(),
                self.roadmap_designer(),
                self.resume_advisor(),
                self.course_recommender(),
                self.final_reporter()
            ],
            tasks=[
                self.analyze_task(),
                self.generate_roadmap_task(),
                self.generate_resume_task(),
                self.recommend_courses_task(),
                self.generate_final_report_task()
            ],
            llm=self.my_LLM,
            function_calling_llm = self.my_LLM,
            process=Process.sequential,
            verbose=False,
            max_rpm=50,  # Overall crew rate limit,
            cache= True,  # Enable caching for faster responses
          
           
          
        )

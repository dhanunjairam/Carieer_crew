# from crewai import Agent, Crew, Process, Task, LLM
# from crewai.project import CrewBase, agent, crew, task
# from crewai_tools import SerperDevTool
# from pydantic import BaseModel
# import os
# from typing import Optional
# import json

# class OutModel(BaseModel):
#     task_title: str
#     task_output: str

# class CompleteOutput(BaseModel):
#     task_title: str
#     career_analysis: str
#     strategic_roadmap: str
#     resume_template: str
#     learning_resources: str



# @CrewBase
# class Crewaiproject3:
#     """Career Development Crew - Comprehensive career guidance and planning"""
    
#     agents_config = 'config/agents.yaml'
#     tasks_config = 'config/tasks.yaml'
#     api_key = os.getenv("OPENROUTER_API_KEY")
#     if not api_key:
#         raise ValueError("OPENROUTER_API_KEY environment variable is required")
    
#     my_LLM = LLM(
#             api_key=api_key,
#             model="openrouter/anthropic/claude-3-haiku",   
#             base_url="https://openrouter.ai/api/v1",
           
#         )
     
#     def validate_json_output(self,result):
#         try:
#             if hasattr(result, 'raw'):
#                 data = json.loads(result.raw)
#             else:
#                 data = json.loads(str(result))
#             return True, data
#         except json.JSONDecodeError as e:
#             return False, f"Invalid JSON format: {str(e)}"
#     # Add validation to your task
    

#     @agent
#     def career_analyst(self) -> Agent:
#         return Agent(
#             config=self.agents_config['career_analyst'],
#             verbose=True,
#             tools=[SerperDevTool()],
#             llm=self.my_LLM,
#             function_calling_llm = self.my_LLM,
#             max_iter=3,  # Limit iterations
#             max_rpm=10   # Rate limiting
#         )

#     @agent
#     def roadmap_designer(self) -> Agent:
#         return Agent(
#             config=self.agents_config['roadmap_designer'],
#             # verbose=True,
#             llm=self.my_LLM,
#             function_calling_llm = self.my_LLM,
#             max_iter=3,  # Limit iterations
#             max_rpm=10   # Rate limiting
           
#         )
    
#     @agent
#     def resume_advisor(self) -> Agent:
#         return Agent(
#             config=self.agents_config['resume_advisor'],
#             # verbose=True,
#             llm=self.my_LLM,
#             function_calling_llm = self.my_LLM,
#             max_iter=3,  # Limit iterations
#             max_rpm=10   # Rate limiting
          
#         )
    
#     @agent 
#     def course_recommender(self) -> Agent:
#         return Agent(
#             config=self.agents_config['course_recommender'],
#             # verbose=True,
#             tools=[SerperDevTool()],
#             llm=self.my_LLM,
#             function_calling_llm = self.my_LLM,
#             max_iter=3,  # Limit iterations
#             max_rpm=10   # Rate limiting
            
#         )
    
#     @agent
#     def final_reporter(self) -> Agent:
#         return Agent(
#             config=self.agents_config['final_reporter'],
#             llm=self.my_LLM,
#             function_calling_llm = self.my_LLM,
#             # verbose=True,
#             max_iter=3,  # Limit iterations
#             max_rpm=10   # Rate limiting
            
#         )

#     @task
#     def analyze_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['analyze_task'],
#             agent=self.career_analyst(),
#             output_pydantic=OutModel,
#             # context=[self.analyze_task()]
#         )
    
#     @task 
#     def generate_roadmap_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['generate_roadmap_task'],
#             agent=self.roadmap_designer(),
#             output_pydantic=OutModel,
#             context=[self.analyze_task()]
            
#         )
    
#     @task
#     def generate_resume_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['generate_resume_task'],
#             agent=self.resume_advisor(),
#             output_pydantic=OutModel,
#             context=[self.analyze_task()]
           
#         )
    
#     @task
#     def recommend_courses_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['recommend_courses_task'],
#             agent=self.course_recommender(),
#             context=[self.analyze_task()],
#             output_pydantic=OutModel,
            
#         )
    
#     @task
#     def generate_final_report_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['generate_final_report_task'],
#             agent=self.final_reporter(),
#             output_pydantic=CompleteOutput,
#             context=[
#                 self.analyze_task(), 
#                 self.generate_roadmap_task(), 
#                 self.generate_resume_task(), 
#                 self.recommend_courses_task()
#             ],
#             guardrail= self.validate_json_output,
#         )

#     @crew
#     def crew(self) -> Crew:
#         """Creates the Career Development crew"""
#         return Crew(
#             agents=[
#                 self.career_analyst(),
#                 self.roadmap_designer(),
#                 self.resume_advisor(),
#                 self.course_recommender(),
#                 self.final_reporter()
#             ],
#             tasks=[
#                 self.analyze_task(),
#                 self.generate_roadmap_task(),
#                 self.generate_resume_task(),
#                 self.recommend_courses_task(),
#                 self.generate_final_report_task()
#             ],
#             llm=self.my_LLM,
#             function_calling_llm = self.my_LLM,
#             process=Process.sequential,
#             verbose=False,
#             max_rpm=50,  # Overall crew rate limit,
#             cache= True,  # Enable caching for faster responses
          
           
          
#         )


from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool,ScrapeWebsiteTool
from crewai.tools import BaseTool
from pydantic import BaseModel
import os
from typing import Optional 
from pydantic import BaseModel, Field
import requests
import litellm
import json
from portkey_ai import createHeaders , PORTKEY_GATEWAY_URL
from typing import Type, Optional



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
    # api_key_1 = os.getenv("PERPLEXITY_API_KEY")
    # model = os.getenv("LLM_MODEL", "perplexity/sonar")
    # base_url = os.getenv("LLM_BASE_URL", "https://api.perplexity.ai/")
    portkey_api_key = os.getenv("PORTKEY_API_KEY")
    portkey_slug_1 = os.getenv("PORTKEY_SLUG_1")
    portkey_slug_2 = os.getenv("PORTKEY_SLUG_2")
    portkey_slug_3 = os.getenv("PORTKEY_SLUG_3")
    portkey_slug_4 = os.getenv("PORTKEY_SLUG_4")
    # print(f"Using PERPLEXITY_API_KEY: {api_key_1}")
    if not portkey_api_key:
        raise ValueError("PERPLEXITY_API_KEY environment variable is required")
    
    # my_LLM = LLM(
    #     api_key=api_key,
    #     model=model,   
    #     base_url=base_url,
    # )
    
    config = {
  "strategy": {"mode": "fallback"},
  "targets": [
    {
      "provider": f"{portkey_slug_1}",       # your first integration slug
      "override_params": {"model": "sonar"}
    },
    {
      "provider": f"{portkey_slug_2}",       # your second integration slug
      "override_params": {"model": "sonar"}
    },
    {
      "provider": f"{portkey_slug_3}",              # your third integration slug
      "override_params": {"model": "sonar"}
    },
    {
      "provider": f"{portkey_slug_4}",              # your fourth integration slug
      "override_params": {"model": "sonar"}
    },
    
  ]
}

    my_LLM = LLM(
    model="perplexity/sonar",
    base_url=PORTKEY_GATEWAY_URL,  # https://api.portkey.ai/v1
    api_key="dummy",  # Often required, but not checked when using virtual keys
    extra_headers=createHeaders(
        api_key=os.getenv("PORTKEY_API_KEY"),  # Your Portkey API key
        config=config  # The routing configuration defined above
        ),

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
            # verbose=True,
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
            tools=[SerperDevTool(),ScrapeWebsiteTool()],
            llm=self.my_LLM,
            function_calling_llm = self.my_LLM,
            max_iter=3,  # Limit iterations
            max_rpm=10   # Rate limiting
            
        )
    
    @agent
    def final_reporter(self) -> Agent:
        # Initialize the custom Notion tool

        
        return Agent(
            config=self.agents_config['final_reporter'],
            llm=self.my_LLM,
            function_calling_llm=self.my_LLM,
           
            max_iter=3,
            max_rpm=10
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
            guardrail=self.validate_json_output,
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

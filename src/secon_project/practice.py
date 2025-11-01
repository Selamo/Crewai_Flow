#flowa
from crewai.flow.flow import Flow, start,router, listen
from pydantic import BaseModel
from typing import List, Optional


# crew
# states
# 1. messages
# 2. time
# 3. Priority
# 4. sender_name
# 5. sender_email

class CustomerFlowState(BaseModel):
    message: Optional[str]= None
    time: Optional[str]=None
    priority:Optional[str]=None
    sender_name:Optional[str]=None
    sender_email:Optional[str]=None

class CustomerFlow(Flow[CustomerFlowState]):
    @start()
    def start_executing(self):
        print("Entering the starting phase")
        return "hello, starting "
    
    @listen("start_executing")
    def executing_listening_func(self):
        print("Executing Listening Function")
        return("done executing")
    
    
flow=CustomerFlow()
results=flow.kickoff()
print(f"Running")
flow.plot()
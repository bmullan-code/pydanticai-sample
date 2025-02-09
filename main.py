import asyncio
from agent import DatabaseConn, SupportDependencies, support_agent
import random

async def test_support_agent():

    ids = [101,102,103]

    id = random.choice(ids)

    deps = SupportDependencies(user_id=id, db=DatabaseConn())

    # Query 1: Subscription plan
    # result = await support_agent.run("What is my subscription plan?", deps=deps)
    print(deps)
    # result = await support_agent.run("Why is my account locked?", deps=deps)
    result = await support_agent.run("I cant login. Help!", deps=deps)
    print(result.data)
    

    101

if __name__ == "__main__":
    asyncio.run(test_support_agent())
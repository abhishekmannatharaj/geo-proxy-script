import asyncio

from models import RequestConfig
from request_service import execute_request
from task_store import tasks


async def process_request_task(
    task_id: str,
    config: RequestConfig
):

    tasks[task_id] = {
        "status": "running",
        "progress": 10
    }

    try:

        # Simulate preparation work
        await asyncio.sleep(1)

        tasks[task_id]["progress"] = 30

        result = await execute_request(config)

        tasks[task_id]["progress"] = 80

        await asyncio.sleep(1)

        if result["success"]:

            tasks[task_id] = {

                "status": "completed",

                "progress": 100,

                "result": result

            }

        else:

            tasks[task_id] = {

                "status": "failed",

                "progress": 100,

                "error": result["error"]

            }

    except Exception as error:

        tasks[task_id] = {

            "status": "failed",

            "progress": 100,

            "error": str(error)

        }
import time
from locust import HttpUser, between, task


"""
the ?version=x  is not used for anything else than separating results in the locust gui
"""
class VersionBehaviour(HttpUser):
    wait_time = between(1, 5)
    @task
    def version_no_headers(self):
        with self.client.get("/", catch_response=True) as response:
            if not "Version: 1.0" in response.text:
                response.failure("Expected response containing version: 1.0 Got wrong version response was: {}".format(response.content))
    # @task(2)
    # def version_v1_header(self):
    #     with self.client.get("/version?version=1", catch_response=True,  headers={"version": "v1"}) as response:
    #         if not "Version: 1.0" in response.content:
    #             response.failure("Expected response containing version: 2.0 Got wrong version response was: {}".format(response.content))

    # @task(3)
    # def version_v2_header(self):
    #     with self.client.get("/version?version=2", catch_response=True,  headers={"version": "v2"}) as response:
    #         if not "Version: 2.0" in response.content:
    #             response.failure("Expected response containing version: 2.0 Got wrong version response was: {}".format(response.content))

    # @task(4)
    # def version_v3_header(self):
    #     with self.client.get("/version?version=3", catch_response=True,  headers={"version": "v3"}) as response:
    #         if not "Version: 3.0" in response.content:
    #             response.failure("Expected response containing version: 2.0 Got wrong version response was: {}".format(response.content))


# class VersionUser(HttpUser):
#     task_set = VersionBehaviour
#     min_wait = 5000
#     max_wait = 15000
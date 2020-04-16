# the following try/except block will make the custom check compatible with any Agent version
try:
    # first, try to import the base class from new versions of the Agent...
    from datadog_checks.base import AgentCheck
except ImportError:
    # ...if the above failed, the check is running in Agent version < 6.6.0
    from checks import AgentCheck

# content of the special variable __version__ will be shown in the Agent status page
__version__ = "0.1.0"

"""Create a custom Agent check that submits a metric named my_metric with a random value between 0 and 1000.

    Thank you, https://datadoghq.dev/summit-training-session/handson/customagentcheck/
"""
class HelloCheck(AgentCheck):
    def check(self, instance):
        self.gauge('hello.world', 1, tags=['admin_email:jitkelme@gmail.com'])

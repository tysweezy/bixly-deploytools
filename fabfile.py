"""
Run fabric commands here.

example usage
"""

from bixlydeploy.connection import DeployDjango

django = DeployDjango('someserver.com', username='john', password='mypass', port=22)

print(django.test_run())
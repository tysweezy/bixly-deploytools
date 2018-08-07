# Bixly Deploy Tools

Just a library on top of Fabric that automates our deployment for common projects. 

## Example Usage:

```
from bixlydeploy.connection import DeployDjango

django = DeployDjango('someserver.com', username='john', password='mypass', port=22)

print(django.test_run())
```
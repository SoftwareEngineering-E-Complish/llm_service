[tox]
envlist = py39
skipsdist = True
 
[testenv]
deps =
    pytest
    coverage
commands =
    coverage run -m unittest discover -s tests
    coverage xml -o coverage.xml  

[coverage:run]
relative_files = True
source = app/  
branch = True

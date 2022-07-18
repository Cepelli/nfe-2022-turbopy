Continuous Integration (CI)
===========================

What is Continuous Integration (CI)?
-------------------------------

There are ***a lot*** of phrases floating around in the software development universe that mean *very* similar things: continuous integration, continuous development/deployment/delivery, DevOps, SecDevOps, DevSecOps...

We are just going to use the phrase Continuous Integration (CI), and here is what we mean:

- Merging small code changes often
- Testing and documenting as we go
- Integrating with (lightweight, but robust) project governance
  - Aspiring to test-driven development (writing tests after a [code spike](https://en.wikipedia.org/wiki/Spike_(software_development)) is O.K.)
  - Managing Project Boards (cards)
  - Managing milestones/releases
  - Packaging our code 
    - Delivery via [PyPI](https://pypi.org/)
    - Hosting on git server behind a firewall
- Utilizing [TravisCI](https://travis-ci.org), [GitHub Actions](https://github.com/features/actions), [CircleCI](https://circleci.com), [gitlab-runner](https://docs.gitlab.com/runner/), [ReadTheDocs](https://readthedocs.org), etc to automate tests, build documentation, deploy products, build release downloads, run linters, create badges...pretty much anything we would want to automate and/or report

Why do CI? 
----------

Because it:
- Frees up our minds to 
  - Design
  - Implement
  - Document
  - Test
- Keeps us all honest
- Distributes the workload
- Keeps us all on the same page
- Reduces accumulation of [technical debt](https://en.wikipedia.org/wiki/Technical_debt)

An example of CI in action: [turboPy](https://github.com/NRL-Plasma-Physics-Division/turbopy)
---------------------------------------------------------------------------------------------

What we will do:
- quick review of turboPy organization including `.yml` files, `tests` folder, and `docs` folder
- walk through `.travis.yml` and [turboPy build on TravisCI](https://travis-ci.org/github/NRL-Plasma-Physics-Division/turbopy)
- walk through `.readthedocs.yml`, `docs` folder, docstrings in source code, and [turboPy documentation on ReadTheDocs](https://turbopy.readthedocs.io/en/latest/)

Jumping in
----------

- Tackle [turboPy](https://github.com/NRL-Plasma-Physics-Division/turbopy/issues) and [nepc](https://github.com/USNavalResearchLaboratory/nepc/issues) issues. Submit a PR and try to get the build to pass.
- Setup a CI pipeline for one of your projects, including tests and documentation.

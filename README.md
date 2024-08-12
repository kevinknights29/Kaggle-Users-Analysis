# Kaggle-Users-Analysis

## Topics

1. [Overview](#overview)
2. [Goals](#goals)
3. [Scope and Context](#scope-and-context)
4. [System Design](#system-design)
5. [Alternatives Considered](#alternatives-considered)
6. [Cross-cutting Concerns](#cross-cutting-concerns)
7. [Learning Logs](#learning-logs)
8. [Resources](#resources)

---

## Overview

WebApp to conduct User Analysis from Kaggle.

## Goals

- Enable analysis on Kaggle users given a country of interest.

## Scope and Context

Download user data from [Meta Kaggle - Users](https://www.kaggle.com/datasets/kaggle/meta-kaggle?select=Users.csv).
Then filter results by country and order them based on Performance Tier (higher the better).

## System Design

### UI Design

![image](https://github.com/user-attachments/assets/6b5ba16c-50bf-4623-a63d-b577f9c3af06)

### Current Front-end

#### Homescreen

![image](https://github.com/user-attachments/assets/9fce47f5-c640-42dc-a454-0390c1df7b9b)

#### Results

![image](https://github.com/user-attachments/assets/59a504cc-0924-4360-afdc-634b3b1c3c88)

## Alternatives Considered

Streamlit.

## Cross-cutting Concerns

Mesop is still new and under-development, meaning that some features are still not implemented.

## Learning Logs

| Date | Learning |
|------|----------|
|      |          |

## Resources

- [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)
- [Conventional Commits Cheatsheet](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13)

### Docs

- [GitHub Actions Context](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/contexts#steps-context)
- [GitHub Actions Automatic token authentication](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication)
- [GitHub Actions Using a matrix for your jobs](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-a-matrix-for-your-jobs#expanding-or-adding-matrix-configurations)
- [Mesop Getting Started](https://google.github.io/mesop/getting-started/installing/)
- [Mesop Components](https://google.github.io/mesop/components/)
- [Mesop Navigate](https://google.github.io/mesop/api/commands/navigate/)

### Stackoverflow

- [Permission denied to github-actions[bot]](https://stackoverflow.com/questions/72851548/permission-denied-to-github-actionsbot)
- [How to activate a virtualenv in a github action?](https://stackoverflow.com/questions/74668349/how-to-activate-a-virtualenv-in-a-github-action)

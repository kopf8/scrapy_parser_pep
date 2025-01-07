# 📝 [Scrapy PEP parser](https://github.com/kopf8/scrapy_parser_pep)

### Contents:

1. [Project tech stack](#project-tech-stack)
2. [Description](#project-description)
3. [Project deployment](#project-deployment)
4. [Project created by](#project-created-by)
<br><hr>

## Project tech stack:
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![Scrapy](https://img.shields.io/badge/scrapy-%2360a839.svg?style=for-the-badge&logo=scrapy&logoColor=d1d2d3)

<br><hr>
## Project description:
This project is a parser based on Scrapy framework for parsing Python Enhancement Proposals (PEP) info from python.org website.

## Project deployment:
Fork this repository into your GitHub profile.
Then clone your repository to your local machine via SSH:
```bash
git clone git@github.com:your_github_username/your_repository_name.git
```

Then create & activate a virtual environment and install project requirements:
```bash
python -m venv .venv
source .venv/Scripts/activate #for Windows users
source .venv/bin/activate #for Linux users
pip install -r requirements.txt
```

Run the following command to launch the parser:
```bash
scrapy crawl pep
```
All parsed data will be saved as _**.csv**_ files in _**results**_ folder in your project directory.

## Project created by:
### [✍️ Maria Kirsanova](https://github.com/kopf8)
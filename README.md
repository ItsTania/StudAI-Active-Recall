# StudAI-Active-Recall

Thi project aims to augment the study of texts by summarising and automatically generating active recall flash cards.

![Alt text](example_UI.png)

## Quick Start

After cloning the repo, do the following to get started!

1. Create a conda environment from the yml file

2. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

3. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

4. Run the app

   ```bash
   $ flask run
   ```


The project extend's the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. 
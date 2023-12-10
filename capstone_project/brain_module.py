#!/usr/bin/env python3

import os
from openai import OpenAI
from dotenv import load_dotenv


class ChatGPT:
    """A class to interact with OpenAI's ChatGPT model."""

    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()

        # Retrieve the OPENAI_API_KEY environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")

        # Set the retrieved API key for the OpenAI library
        OpenAI.api_key = self.api_key

        # A constant to describe the role or behavior of the chatbot
        self.MAIN_ROLE = "Expert Magic the gathering commander player"

    def cost_calculator_for_GPT_3_5_turbo(response):

        # These 2 values are valid only for the "gpt-3.5-turbo-1106" model.
        # Check https://openai.com/pricing for up-to-date prices
        cost_of_input_tokens = 0.001
        cost_of_output_tokens = 0.002

        completion_tokens = response.model_dump()['usage']['completion_tokens']
        prompt_tokens = response.model_dump()['usage']['prompt_tokens']

        total_cost = (
            (prompt_tokens * cost_of_input_tokens) + (completion_tokens * cost_of_output_tokens)
        ) / 1000

        return f"Total cost for API call: ${total_cost} USD"

    def request_openai(self, message, role="system"):
        """
        Make a request to the OpenAI API.

        Args:
        - message (str): The message to be sent to the OpenAI API.
        - role (str, optional): The role associated with the message. Defaults to "system".

        Returns:
        - str: The response content from the OpenAI API.
        """

        client = OpenAI()

        # Create a chat completion with the provided message and role
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[{"role": role, "content": message}],
            response_format={"type": "json_object"},
        )

        print(ChatGPT.cost_calculator_for_GPT_3_5_turbo(response))

        # Return the message content from the API response
        return response.choices[0].message.content


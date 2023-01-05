import openai

def download_paper(paper_id):
    return "" ## TODO: Download a paper and scrape the text off it

def split_text(text):
    return "" ## TODO: Split a long text into smaller chunks by topic

def generate_prompt(text):
    return f"Summarize into key points and provide a matching question. Format your response as list of JSON objects mapping the key point to the matching question: {text}"

def get_gpt3_output(input, max_token_relative=False, model_name="text-davinci-003"):
    # Set the max tokens to 200 or 4000 - the length of the input 
    max_tokens = 4000 - len(input) if max_token_relative else 200
    # Generate the prompt
    prompt = generate_prompt(input)

    # Use the openai API to generate a summary of the text
    summary = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens
    )
    return summary

def output_to_text(output):
    return output ## TODO: Convert the output into a text format

def export_results(results):
    return "" ## TODO: Export the results into a flashcard format


if __name__ == "__main__":
    # Get the input text from the user
    text = input("Enter some text: ")
    
    # Get the result
    result = get_result(text)
    
    # Print the result
    print(result)

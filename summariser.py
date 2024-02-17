from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain
import transcriptor


def get_summary(transcript):
    openai_api_key = "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"

    template = f""" You are a helpful assistant programmed to generate summary of lecture transcripts.
    Make sure it easy to understand and covers all important points. Also add some additional information to your
    output if you think it will be hard to follow for a beginner.
    If you can write most of the information in bullet points and codeblocks.
    Output it in text format.
    Make sure that your output is in english even if prompted in hindi or any other language
    You must adhere to this format as it's optimized for further Python processing.
    """
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_message_prompt = HumanMessagePromptTemplate.from_template("{text}")
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )
    chain = LLMChain(
        llm=ChatOpenAI(openai_api_key=openai_api_key),
        prompt=chat_prompt,
    )
    ans = chain.run(transcript)
    with open("sum.txt", "a") as f:
        f.write(ans)

import os
from dotenv import load_dotenv

from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI

from langchain import OpenAI
from langchain.chains import (
    LLMChain, 
    ConversationChain
)
from langchain.chains.conversation.memory import (
    ConversationBufferMemory,
    ConversationSummaryMemory,
    ConversationBufferWindowMemory,
    ConversationSummaryBufferMemory
)

from langchain.callbacks import get_openai_callback
import tiktoken


def count_tokens(chain, query):
    '''
    The function returns the number of tokens and the response provided by the assistant
    '''
    with get_openai_callback() as cb:
        result = chain.run(query)
        print(f'Spent a total of {cb.total_tokens} tokens')

    return result

def conversation():

    llm=OpenAI(temperature=0.0)

    #conversation = ConversationChain(llm=llm)
    #print(conversation.prompt.template)
    # The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

    # Current conversation:
    # {history}
    # Human: {input}
    # AI:

    conversation_buf = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory()
    )

    query="Good morning AI!"
    num_tokens=count_tokens(
        conversation_buf, 
        query=query
    )
    print(num_tokens)

    query="My interest here is to explore the potential of integrating Large Language Models with external knowledge"
    num_tokens=count_tokens(
        conversation_buf, 
        query=query
    )
    print(num_tokens)

    query="I just want to analyze the different possibilities. What can you think of?"
    count_tokens(
        conversation_buf,
        query=query
    )
    print(num_tokens)

    #print(conversation_buf.memory.buffer)

def summary_conversation():

    llm=OpenAI(temperature=0.0)
    
    conversation_sum = ConversationChain(
        llm=llm, 
        memory=ConversationSummaryMemory(llm=llm)
    )

    # print(conversation_sum.memory.prompt.template)
    # Progressively summarize the lines of conversation provided, adding onto the previous summary returning a new summary

    query="Good morning AI!"
    num_tokens=count_tokens(
        conversation_sum, 
        query=query
    )
    print(num_tokens)

    query="My interest here is to explore the potential of integrating Large Language Models with external knowledge"
    num_tokens=count_tokens(
        conversation_sum, 
        query=query
    )
    print(num_tokens)

    query="I just want to analyze the different possibilities. What can you think of?"
    count_tokens(
        conversation_sum,
        query=query
    )
    print(num_tokens)

    #print(conversation_sum.memory.buffer)

def windowed_conversation():

    llm=OpenAI(temperature=0.0)
    
    conversation_win = ConversationChain(
        llm=llm, 
        memory=ConversationBufferWindowMemory(k=2)
    )

    query="Good morning AI!"
    num_tokens=count_tokens(
        conversation_win, 
        query=query
    )
    print(num_tokens)

    query="My interest here is to explore the potential of integrating Large Language Models with external knowledge"
    num_tokens=count_tokens(
        conversation_win, 
        query=query
    )
    print(num_tokens)

    query="I just want to analyze the different possibilities. What can you think of?"
    count_tokens(
        conversation_win,
        query=query
    )
    print(num_tokens)

    bufw_history = conversation_win.memory.load_memory_variables(
        inputs=[]
    )['history']
    print(bufw_history)

def windowed_summary_conversation():

    llm=OpenAI(temperature=0.0)
    
    conversation_ws = ConversationChain(
        llm=llm, 
        memory=ConversationSummaryBufferMemory(llm=llm,max_token_limit=40),
        verbose=True
    )

    try:
        print("\n***WELCOME***\n")
        while True:
            prompt = input("\nUser: ")
            response=conversation_ws.predict(input=prompt)
            print(f"Assistant: {response}")
    except KeyboardInterrupt:
        print("BYE BYE!!!")

load_dotenv()

# conversation()
# summary_conversation()
windowed_summary_conversation()
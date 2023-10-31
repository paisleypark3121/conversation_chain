import os
from dotenv import load_dotenv

from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI

from langchain.chains import (
    LLMChain, 
    ConversationChain
)

from langchain.memory import ConversationSummaryMemory, ChatMessageHistory

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

def summary_conversation_given_history():

    llm=OpenAI(temperature=0.0)

    history = ChatMessageHistory()
    history.add_user_message("hi")
    history.add_ai_message("hi there!")
    history.add_user_message("my name is stefano and the weather is good")
    history.add_user_message("nice to meet you stefano")
    
    memory = ConversationSummaryMemory.from_messages(
        llm=llm, 
        chat_memory=history
    )
    print(memory.buffer)
    #The human greets the AI, to which the AI responds with a friendly greeting. The human introduces himself as Stefano and the AI responds with a friendly greeting.

    # memory = ConversationSummaryMemory.from_messages(
    #     llm=llm, 
    #     buffer="the user and AI greets each other and the user name is stefano. the weather is good"
    # )

    conversation_with_summary = ConversationChain(
        llm=llm,
        #memory=ConversationSummaryMemory(llm=OpenAI()),
        memory=memory,
        #verbose=True
    )

    query="what's my name?"
    response=conversation_with_summary.predict(input=query)
    print(response)
    #You told me your name is Stefano. Is there anything else I can help you with?
    
    print(conversation_with_summary.memory.buffer)
    #The human greets the AI, to which the AI responds with a friendly greeting. The human introduces himself as Stefano and the AI responds with a friendly greeting. The human then asks what his name is, to which the AI responds that it is Stefano. The AI then asks if there is anything else it can help with.

    query="what's the weather like?"
    response=conversation_with_summary.predict(input=query)
    print(response)
    #The current weather in your area is sunny with a temperature of 72 degrees Fahrenheit. The forecast for the rest of the day is mostly sunny with a high of 78 degrees Fahrenheit.
    
    print(conversation_with_summary.memory.buffer)
    #The human greets the AI, to which the AI responds with a friendly greeting. The human introduces himself as Stefano and the AI responds with a friendly greeting. The human then asks what his name is, to which the AI responds that it is Stefano. The AI then asks if there is anything else it can help with, to which the human asks what the weather is like. The AI responds that the current weather is sunny with a temperature of 72 degrees Fahrenheit and the forecast for the rest of the day is mostly sunny with a high of 78 degrees Fahrenheit.

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
#windowed_summary_conversation()
summary_conversation_given_history()
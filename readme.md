Start from main: python main.py

Please create an .env file and insert your openai api key:
OPENAI_API_KEY=**USE YOUR KEY**

Tips:
https://www.pinecone.io/learn/series/langchain/langchain-conversational-memory/

BELOW and example of the conversation with buffered window (please note that using VERBOSE=TRUE allows me to have the visualization of the conversationchain)

**_WELCOME_**

User: Hello, my name is Stefano

> Entering new ConversationChain chain...
> Prompt after formatting:
> The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

Human: Hello, my name is Stefano
AI:

> Finished chain.
> Assistant: Hi Stefano, my name is AI. It's nice to meet you. What can I do for you today?

User: I'm trying to understand if my implementation works

> Entering new ConversationChain chain...
> Prompt after formatting:
> The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
Human: Hello, my name is Stefano
AI: Hi Stefano, my name is AI. It's nice to meet you. What can I do for you today?
Human: I'm trying to understand if my implementation works
AI:

> Finished chain.
> Assistant: Sure, I'd be happy to help. Can you tell me more about your implementation? What is it for and what technologies are you using?

User: I'm using the LangChain library with a window buffered method and it should just maintain a small set of tokens

> Entering new ConversationChain chain...
> Prompt after formatting:
> The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
System:
The human introduces themselves as Stefano and the AI introduces itself as AI. The AI asks Stefano what it can do for them and Stefano responds that they are trying to understand if their implementation works.
AI: Sure, I'd be happy to help. Can you tell me more about your implementation? What is it for and what technologies are you using?
Human: I'm using the LangChain library with a window buffered method and it should just maintain a small set of tokens
AI:

> Finished chain.
> Assistant: Got it. So you're using the LangChain library with a window buffered method to maintain a small set of tokens. Is there anything else I should know about your implementation?

User: it seems that the LangChain method is correctly "summarizing" our conversation

> Entering new ConversationChain chain...
> Prompt after formatting:
> The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
System:
The human introduces themselves as Stefano and the AI introduces itself as AI. The AI asks Stefano what it can do for them and Stefano responds that they are trying to understand if their implementation works. The AI offers to help and asks for more information about the implementation, such as what it is for and what technologies are being used. Stefano responds that they are using the LangChain library with a window buffered method and it should just maintain a small set of tokens.
AI: Got it. So you're using the LangChain library with a window buffered method to maintain a small set of tokens. Is there anything else I should know about your implementation?
Human: it seems that the LangChain method is correctly "summarizing" our conversation
AI:

> Finished chain.
> Assistant: That's great to hear! Can you tell me more about what you mean by summarizing?

User: BYE BYE!!!

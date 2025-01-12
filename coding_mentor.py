# import streamlit as st
# from langchain_ollama import OllamaLLM
# from langchain.prompts import PromptTemplate
# from langchain.schema.runnable import RunnablePassthrough
# from typing import Dict, List
# import time

# llm = OllamaLLM(model="codellama")

# DEBUG_TEMPLATE = """
# Analyze the following code and provide debugging assistance:
# Code:
# {code}

# Please provide:
# 1. Identified errors or potential issues
# 2. Detailed explanation of each problem
# 3. Suggested fixes with corrected code
# 4. Best practices recommendations

# Response should be clear and educational.
# """

# CONVERT_TEMPLATE = """
# Convert the following code from {source_lang} to {target_lang}:
# {code}

# Please provide:
# 1. Converted code
# 2. Explanation of key differences
# 3. Any important considerations or limitations
# 4. Usage examples if applicable
# """

# COMPLEXITY_TEMPLATE = """
# Analyze the time and space complexity of the following code:
# {code}

# Please provide:
# 1. Time complexity analysis with explanation
# 2. Space complexity analysis with explanation
# 3. Potential optimization suggestions
# 4. Trade-offs of suggested optimizations
# """

# EXPLAIN_TEMPLATE = """
# Explain the following code in detail:
# {code}

# Please provide:
# 1. Line-by-line explanation
# 2. Key concepts used
# 3. Potential improvements
# 4. Best practices analysis
# """

# class CodingMentor:
#     def __init__(self):
#         # Create prompt templates
#         debug_prompt = PromptTemplate(
#             input_variables=["code"],
#             template=DEBUG_TEMPLATE
#         )
        
#         convert_prompt = PromptTemplate(
#             input_variables=["code", "source_lang", "target_lang"],
#             template=CONVERT_TEMPLATE
#         )
        
#         complexity_prompt = PromptTemplate(
#             input_variables=["code"],
#             template=COMPLEXITY_TEMPLATE
#         )
        
#         explain_prompt = PromptTemplate(
#             input_variables=["code"],
#             template=EXPLAIN_TEMPLATE
#         )
        
#         self.debug_chain = debug_prompt | llm
#         self.convert_chain = convert_prompt | llm
#         self.complexity_chain = complexity_prompt | llm
#         self.explain_chain = explain_prompt | llm
    
#     def debug_code(self, code: str) -> str:
#         return self.debug_chain.invoke({"code": code})
    
#     def convert_code(self, code: str, source_lang: str, target_lang: str) -> str:
#         return self.convert_chain.invoke({
#             "code": code,
#             "source_lang": source_lang,
#             "target_lang": target_lang
#         })
    
#     def analyze_complexity(self, code: str) -> str:
#         return self.complexity_chain.invoke({"code": code})
    
#     def explain_code(self, code: str) -> str:
#         return self.explain_chain.invoke({"code": code})

# def main():
#     st.set_page_config(page_title="AI Coding Mentor", layout="wide", )
    
#     st.title("🤖 AI Coding Mentor")
#     mentor = CodingMentor()
    
#     feature = st.sidebar.selectbox(
#         "Select Feature",
#         ["Code Debugging", "Code Conversion", "Complexity Analysis", "Code Explanation"]
#     )
    
#     with st.container():
#         if feature == "Code Debugging":
#             st.header("Code Debugging Assistant")
#             code = st.text_area("Enter your code:", height=200)
            
#             if st.button("Debug Code"):
#                 with st.spinner("Analyzing code..."):
#                     result = mentor.debug_code(code)
#                 st.markdown(result)
                
#         elif feature == "Code Conversion":
#             st.header("Code Conversion Tool")
#             col1, col2 = st.columns(2)
#             with col1:
#                 source_lang = st.selectbox("Source Language", ["Python", "Java", "JavaScript", "C++"])
#             with col2:
#                 target_lang = st.selectbox("Target Language", ["Java", "Python", "JavaScript", "C++"])
            
#             code = st.text_area("Enter your code:", height=200)
            
#             if st.button("Convert Code"):
#                 with st.spinner(f"Converting from {source_lang} to {target_lang}..."):
#                     result = mentor.convert_code(code, source_lang, target_lang)
#                 st.markdown(result)
                
#         elif feature == "Complexity Analysis":
#             st.header("Code Complexity Analyzer")
#             code = st.text_area("Enter your code:", height=200)
            
#             if st.button("Analyze Complexity"):
#                 with st.spinner("Analyzing complexity..."):
#                     result = mentor.analyze_complexity(code)
#                 st.markdown(result)
                
#         else:  
#             st.header("Code Explanation")
#             code = st.text_area("Enter your code:", height=200)
            
#             if st.button("Explain Code"):
#                 with st.spinner("Generating explanation..."):
#                     result = mentor.explain_code(code)
#                 st.markdown(result)

#     st.markdown("---")
#     st.markdown("Built with Streamlit, LangChain, and CodeLlama")

# if __name__ == "__main__":
#     main()

import streamlit as st
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from typing import Dict, List
import time

llm = OllamaLLM(model="codellama")

DEBUG_TEMPLATE = """
Analyze the following code and provide debugging assistance:
Code:
{code}

Please provide:
1. Identified errors or potential issues
2. Detailed explanation of each problem
3. Suggested fixes with corrected code
4. Best practices recommendations

Response should be clear and educational.
"""

CONVERT_TEMPLATE = """
Convert the following code from {source_lang} to {target_lang}:
{code}

Please provide:
1. Converted code
2. Explanation of key differences
3. Any important considerations or limitations
4. Usage examples if applicable
"""

COMPLEXITY_TEMPLATE = """
Analyze the time and space complexity of the following code:
{code}

Please provide:
1. Time complexity analysis with explanation
2. Space complexity analysis with explanation
3. Potential optimization suggestions
4. Trade-offs of suggested optimizations
"""

EXPLAIN_TEMPLATE = """
Explain the following code in detail:
{code}

Please provide:
1. Line-by-line explanation
2. Key concepts used
3. Potential improvements
4. Best practices analysis
"""

class CodingMentor:
    def __init__(self):
        # Create prompt templates
        debug_prompt = PromptTemplate(
            input_variables=["code"],
            template=DEBUG_TEMPLATE
        )
        
        convert_prompt = PromptTemplate(
            input_variables=["code", "source_lang", "target_lang"],
            template=CONVERT_TEMPLATE
        )
        
        complexity_prompt = PromptTemplate(
            input_variables=["code"],
            template=COMPLEXITY_TEMPLATE
        )
        
        explain_prompt = PromptTemplate(
            input_variables=["code"],
            template=EXPLAIN_TEMPLATE
        )
        
        self.debug_chain = debug_prompt | llm
        self.convert_chain = convert_prompt | llm
        self.complexity_chain = complexity_prompt | llm
        self.explain_chain = explain_prompt | llm
    
    def debug_code(self, code: str) -> str:
        return self.debug_chain.invoke({"code": code})
    
    def convert_code(self, code: str, source_lang: str, target_lang: str) -> str:
        return self.convert_chain.invoke({
            "code": code,
            "source_lang": source_lang,
            "target_lang": target_lang
        })
    
    def analyze_complexity(self, code: str) -> str:
        return self.complexity_chain.invoke({"code": code})
    
    def explain_code(self, code: str) -> str:
        return self.explain_chain.invoke({"code": code})

def main():
    st.set_page_config(page_title="AI Coding Mentor", layout="wide")
    
    st.title("🤖 AI Coding Mentor")
    mentor = CodingMentor()
    
    feature = st.sidebar.selectbox(
        "Select Feature",
        ["Code Debugging", "Code Conversion", "Complexity Analysis", "Code Explanation"]
    )
    
    with st.container():
        if feature == "Code Debugging":
            st.header("Code Debugging Assistant")
            code = st.text_area("Enter your code:", height=200)
            
            if st.button("Debug Code"):
                with st.spinner("Analyzing code..."):
                    result = mentor.debug_code(code)
                st.markdown(result)
                
        elif feature == "Code Conversion":
            st.header("Code Conversion Tool")
            col1, col2 = st.columns(2)
            with col1:
                source_lang = st.selectbox("Source Language", ["Python", "Java", "JavaScript", "C++"])
            with col2:
                target_lang = st.selectbox("Target Language", ["Java", "Python", "JavaScript", "C++"])
            
            code = st.text_area("Enter your code:", height=200)
            
            if st.button("Convert Code"):
                with st.spinner(f"Converting from {source_lang} to {target_lang}..."):
                    result = mentor.convert_code(code, source_lang, target_lang)
                st.markdown(result)
                
        elif feature == "Complexity Analysis":
            st.header("Code Complexity Analyzer")
            code = st.text_area("Enter your code:", height=200)
            
            if st.button("Analyze Complexity"):
                with st.spinner("Analyzing complexity..."):
                    result = mentor.analyze_complexity(code)
                st.markdown(result)
                
        else:  
            st.header("Code Explanation")
            code = st.text_area("Enter your code:", height=200)
            
            if st.button("Explain Code"):
                with st.spinner("Generating explanation..."):
                    result = mentor.explain_code(code)
                st.markdown(result)

    st.markdown("---")
    st.markdown("Built with Streamlit, LangChain, and CodeLlama")

if __name__ == "__main__":
    main()
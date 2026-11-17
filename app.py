import streamlit as st
from chatbot import StartupValidator

# Page configuration
st.set_page_config(
    page_title="Brutal Startup Idea Validator",
    page_icon="💡",
    layout="wide"
)

# Initialize the startup validator
validator = StartupValidator()

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'startup_context' not in st.session_state:
    st.session_state.startup_context = ""

# Title and description
st.title("💡 Brutal Startup Idea Validator")
st.markdown("### Get an honest, no-BS analysis of your startup idea")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    brutality_level = st.slider(
        "Brutality Level",
        min_value=1,
        max_value=10,
        value=7,
        help="How harsh should the feedback be? (1=gentle, 10=savage)"
    )
    
    st.markdown("---")
    
    # Additional context inputs
    st.subheader("📋 Optional Details")
    target_market = st.text_input("Target Market", placeholder="e.g., Urban millennials")
    budget_range = st.text_input("Budget Range", placeholder="e.g., $10K-$50K")
    timeline = st.text_input("Timeline", placeholder="e.g., 6 months to MVP")
    
    st.markdown("---")
    st.markdown("### About")
    st.info("This tool provides a brutally honest analysis of your startup idea using AI.")
    st.markdown("### Features")
    st.markdown("""
    - ✅ Idea Validation
    - 📊 Market Analysis
    - 💰 Investment Requirements
    - 📈 Future Scope
    - ⚠️ Risks & Challenges
    - 💬 Follow-up Questions
    """)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input at the bottom (ChatGPT style)
if prompt := st.chat_input("Describe your startup idea..."):
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response with streaming
    with st.chat_message("assistant"):
        try:
            message_placeholder = st.empty()
            full_response = ""
            
            # Determine if this is a new startup idea or follow-up
            is_startup = validator.validate_input(prompt)
            
            if is_startup:
                # This is a new startup idea - do full analysis
                st.session_state.startup_context = prompt  # Save the startup context
                
                # Stream the response
                for chunk in validator.analyze_startup(
                    startup_idea=prompt,
                    target_market=target_market,
                    budget_range=budget_range,
                    timeline=timeline,
                    brutality_level=brutality_level
                ):
                    full_response += chunk.content
                    message_placeholder.markdown(full_response + "▌")
                
            else:
                # This is a follow-up question
                conversation_history = validator.get_conversation_history(st.session_state.messages)
                
                response_stream = validator.handle_followup(
                    user_question=prompt,
                    conversation_history=conversation_history,
                    startup_context=st.session_state.startup_context,
                    brutality_level=brutality_level
                )
                
                if isinstance(response_stream, str):
                    # Static response for no startup context
                    full_response = response_stream
                    message_placeholder.markdown(full_response)
                else:
                    # Stream the response
                    for chunk in response_stream:
                        full_response += chunk.content
                        message_placeholder.markdown(full_response + "▌")
            
            # Final cleanup - remove cursor
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            full_response = "Sorry, I encountered an error. Please try again."
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
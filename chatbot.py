from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class StartupValidator:
    def __init__(self):
        # Get API key from environment
        os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
        
        # Initialize LLM models
        self.llm = ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0.7,
            streaming=True
        )
        
        self.llm_validator = ChatGroq(
            model="openai/gpt-oss-120b",
            temperature=0.3
        )
        
        # Define prompt templates
        self.validation_template = """You are a strict input validator. Determine if the user's input is a NEW STARTUP IDEA or something else.

USER INPUT: {user_input}

Respond with ONLY ONE WORD:
- "STARTUP" - if this is clearly a NEW startup idea, business concept, or entrepreneurial proposal
- "OTHER" - if this is a follow-up question, clarification, or anything else

Examples of STARTUP:
- "An app that helps people find parking spots"
- "A service connecting freelance designers with small businesses"
- "Subscription box for organic pet food"

Examples of OTHER (follow-up questions or general queries):
- "Can you explain the revenue model more?"
- "What about marketing?"
- "How do I reduce the risks?"
- "Tell me more about investment"
- "What is a startup?"
- "Hello"

Respond with ONLY: STARTUP or OTHER"""

        self.initial_analysis_template = """You are a brutal, experienced startup advisor with 20+ years of experience. You've seen thousands of startups fail and succeed. Your job is to provide HONEST, DIRECT feedback without sugar-coating anything.

Analyze this startup idea with a brutality level of {brutality_level}/10:

STARTUP IDEA: {startup_idea}

TARGET MARKET: {target_market}
BUDGET RANGE: {budget_range}
TIMELINE: {timeline}

Provide a comprehensive analysis in the following format:

## 🎯 IDEA VALIDATION (Valid/Invalid)
State clearly if this idea is VALID or INVALID. Be direct about fatal flaws.

## 📊 SHORT-TERM GOALS (0-6 months)
List 3-5 realistic short-term goals. Be specific and actionable.

## 🎯 LONG-TERM GOALS (1-3 years)
List 3-5 long-term strategic goals. Think big but realistic.

## 💰 INVESTMENT REQUIRED
Break down:
- Initial Investment: $X - $Y
- Monthly Burn Rate: $X - $Y
- Total 1st Year: $X - $Y

Be specific with numbers based on the idea.

## 📈 REVENUE POTENTIAL
- Can you sell this? YES/NO (with brutal honesty)
- Expected timeline to first sale: X months
- Revenue potential (Year 1, Year 2, Year 3)
- Realistic exit opportunities (if any)

## ⚖️ RISK ANALYSIS
### LOSSES (Be brutal about what can go wrong)
- List 4-6 major risks and potential losses
- Include realistic failure scenarios

### BENEFITS (Don't oversell, be realistic)
- List 3-5 genuine benefits if successful
- Include competitive advantages (if any exist)

## 🚀 FUTURE SCOPE
- Scalability potential (Low/Medium/High)
- Market trends supporting/opposing this idea
- Evolution opportunities

## 💡 BRUTAL IMPROVEMENTS
List 5-7 specific, actionable improvements. Don't hold back on what's wrong and how to fix it.

## 🎯 FINAL VERDICT
Give a percentage score (0-100%) for:
- Viability: X%
- Profitability: X%
- Scalability: X%
- Overall Score: X%

End with a ONE-SENTENCE brutal truth about this idea.

Remember: Be HONEST, be DIRECT, be BRUTAL (level {brutality_level}/10). No false hope, no generic advice."""

        self.followup_template = """You are a brutal, experienced startup advisor. You are continuing a conversation about a startup idea.

PREVIOUS CONVERSATION CONTEXT:
{conversation_history}

STARTUP CONTEXT:
{startup_context}

USER'S FOLLOW-UP QUESTION: {user_question}

BRUTALITY LEVEL: {brutality_level}/10

Provide a focused, honest answer to their question. Reference the previous analysis when relevant. Stay brutal but helpful. If they ask something unrelated to startup validation, politely redirect them to focus on their startup idea.

Keep your response concise but comprehensive. Use the same brutal, direct tone as before."""

    def validate_input(self, user_input):
        """Validate if input is a startup idea or follow-up question"""
        validation_prompt = PromptTemplate(
            input_variables=["user_input"],
            template=self.validation_template
        )
        
        formatted_validation = validation_prompt.format(user_input=user_input)
        validation_result = self.llm_validator.invoke(formatted_validation).content.strip().upper()
        
        return "STARTUP" in validation_result

    def analyze_startup(self, startup_idea, target_market="", budget_range="", timeline="", brutality_level=7):
        """Perform initial startup analysis"""
        analysis_prompt = PromptTemplate(
            input_variables=["startup_idea", "target_market", "budget_range", "timeline", "brutality_level"],
            template=self.initial_analysis_template
        )
        
        formatted_analysis = analysis_prompt.format(
            startup_idea=startup_idea,
            target_market=target_market if target_market else "Not specified",
            budget_range=budget_range if budget_range else "Not specified",
            timeline=timeline if timeline else "Not specified",
            brutality_level=brutality_level
        )
        
        return self.llm.stream(formatted_analysis)

    def handle_followup(self, user_question, conversation_history, startup_context, brutality_level=7):
        """Handle follow-up questions"""
        if not startup_context:
            return """❓ **No Startup Idea Found**

I don't see any startup idea in our conversation yet. Please first describe your startup idea, and then I can answer your questions about it.

**Example:** "A mobile app that connects local farmers with restaurants" """

        followup_prompt = PromptTemplate(
            input_variables=["user_question", "conversation_history", "startup_context", "brutality_level"],
            template=self.followup_template
        )
        
        formatted_followup = followup_prompt.format(
            user_question=user_question,
            conversation_history=conversation_history,
            startup_context=startup_context,
            brutality_level=brutality_level
        )
        
        return self.llm.stream(formatted_followup)

    @staticmethod
    def get_conversation_history(messages):
        """Extract conversation history from messages"""
        history = ""
        for msg in messages[-6:]:  # Last 6 messages (3 exchanges)
            if msg["role"] == "user":
                history += f"\nUser: {msg['content']}\n"
            else:
                history += f"Assistant: {msg['content'][:500]}...\n"  # Truncate long responses
        return history
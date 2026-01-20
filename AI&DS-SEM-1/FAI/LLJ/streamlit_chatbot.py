
import streamlit as st
import re
import random
from datetime import datetime
import json

# Knowledge base and intent patterns (same as before)
knowledge_base = {
    'courses': {
        'ug': ['B.Tech', 'B.Sc', 'BBA', 'B.Com', 'BCA', 'B.Design', 'BHM'],
        'pg': ['M.Tech', 'M.Sc', 'MBA', 'MCA', 'M.Design'],
        'phd': ['Ph.D in Engineering', 'Ph.D in Science', 'Ph.D in Management']
    },
    'engineering_branches': [
        'Computer Science and Engineering',
        'Information Technology',
        'Electronics and Communication Engineering',
        'Electrical and Electronics Engineering',
        'Mechanical Engineering',
        'Civil Engineering',
        'Artificial Intelligence and Data Science',
        'Cyber Security'
    ],
    'eligibility': {
        'btech': '10+2 with Physics, Chemistry, and Mathematics with minimum 50% aggregate',
        'bsc': '10+2 with Science subjects with minimum 50% aggregate',
        'bba': '10+2 in any stream with minimum 50% aggregate',
        'mtech': 'B.Tech/B.E degree with minimum 50% aggregate',
        'mba': 'Bachelor degree in any discipline with minimum 50% aggregate'
    },
    'entrance_exams': {
        'btech': 'SRMJEEE (SRM Joint Engineering Entrance Examination), JEE Main',
        'management': 'CAT, MAT, XAT, CMAT, ATMA, SRMHCAT',
        'other': 'Program-specific entrance tests conducted by SRM'
    },
    'fees': {
        'btech': 'Rs. 2,50,000 - Rs. 3,00,000 per annum (varies by branch)',
        'bba': 'Rs. 1,75,000 - Rs. 2,00,000 per annum',
        'mtech': 'Rs. 1,50,000 - Rs. 2,00,000 per annum',
        'mba': 'Rs. 4,00,000 - Rs. 6,00,000 per annum'
    },
    'contact': {
        'phone': '+91-44-27417000',
        'email': 'admissions@srmist.edu.in',
        'website': 'www.srmist.edu.in',
        'address': 'SRM Institute of Science and Technology, Kattankulathur, Chennai - 603203'
    },
    'application_process': [
        '1. Visit the official SRM admission portal',
        '2. Register with your email and phone number',
        '3. Fill in the application form with personal and academic details',
        '4. Upload required documents (photos, marksheets, ID proof)',
        '5. Pay the application fee online',
        '6. Submit the application and note your application number',
        '7. Appear for the entrance examination (if applicable)',
        '8. Check results and attend counseling if selected'
    ],
    'scholarships': [
        'Merit-based scholarships up to 100% tuition fee waiver',
        'Sports quota scholarships',
        'Need-based financial assistance',
        'Special scholarships for SC/ST/OBC students',
        'Girl child scholarships'
    ],
    'placements': {
        'average_package': 'Rs. 6-8 LPA',
        'highest_package': 'Rs. 40+ LPA',
        'top_recruiters': ['Google', 'Microsoft', 'Amazon', 'TCS', 'Infosys', 'Wipro', 'Cognizant', 'Accenture'],
        'placement_rate': '90%+'
    }
}

intent_patterns = {
    'greeting': [
        r'\b(hi|hello|hey|good morning|good afternoon|good evening)\b',
    ],
    'courses': [
        r'\b(courses?|programs?|degrees?|branches?)\b',
        r'what (courses?|programs?) (do you|does srm) (offer|have|provide)',
        r'(tell me|show me) (about )?(the )?(courses?|programs?)',
        r'\b(btech|mtech|bba|mba|bsc|msc)\b'
    ],
    'eligibility': [
        r'\b(eligibility|criteria|requirements?|qualifications?)\b',
        r'(who can|can i) apply',
        r'what are the (requirements?|eligibility)',
        r'(minimum|required) (marks?|percentage|qualifications?)'
    ],
    'fees': [
        r'\b(fees?|cost|tuition|charges?|price)\b',
        r'how much (does it|will it) cost',
        r'what (is|are) the (fees?|charges?)',
        r'(admission|tuition) (fees?|cost)'
    ],
    'entrance': [
        r'\b(entrance|exam|examination|test|srmjeee|jee)\b',
        r'(entrance|qualifying) (exam|test)',
        r'how to (get|gain) admission'
    ],
    'application': [
        r'\b(apply|application|register|registration)\b',
        r'how (do i|to|can i) apply',
        r'(application|registration) (process|procedure|steps)'
    ],
    'contact': [
        r'\b(contact|phone|email|address|location|reach)\b',
        r'how (do i|to|can i) (contact|reach)',
        r'(phone|contact) (number|details)'
    ],
    'scholarship': [
        r'\b(scholarship|financial aid|concession|waiver)\b',
        r'(scholarship|financial) (aid|assistance|support)'
    ],
    'placement': [
        r'\b(placement|job|recruit|package|salary|companies?)\b',
        r'(placement|job) (opportunities?|scenario|statistics?)'
    ],
    'goodbye': [
        r'\b(bye|goodbye|thanks|thank you|exit|quit)\b'
    ]
}

class SRMAdmissionChatbot:
    """A rule-based chatbot for handling SRM admission enquiries."""

    def __init__(self, knowledge_base, intent_patterns):
        self.kb = knowledge_base
        self.patterns = intent_patterns
        self.conversation_history = []

    def preprocess_input(self, user_input):
        """Clean and normalize user input."""
        return user_input.lower().strip()

    def identify_intent(self, user_input):
        """Identify user intent using pattern matching."""
        user_input = self.preprocess_input(user_input)

        for intent, patterns in self.patterns.items():
            for pattern in patterns:
                if re.search(pattern, user_input, re.IGNORECASE):
                    return intent

        return 'unknown'

    def generate_response(self, intent, user_input):
        """Generate appropriate response based on identified intent."""

        if intent == 'greeting':
            responses = [
                "Hello! Welcome to SRM Admission Enquiry Chatbot. How can I assist you today?",
                "Hi there! I'm here to help you with SRM admission queries. What would you like to know?",
                "Greetings! I can help you with information about SRM admissions. What are you interested in?"
            ]
            return random.choice(responses)

        elif intent == 'courses':
            response = "SRM offers a wide range of courses:\n\n"
            response += "📚 Undergraduate (UG):\n"
            response += ", ".join(self.kb['courses']['ug']) + "\n\n"
            response += "🎓 Postgraduate (PG):\n"
            response += ", ".join(self.kb['courses']['pg']) + "\n\n"
            response += "🔬 Doctoral Programs:\n"
            response += ", ".join(self.kb['courses']['phd']) + "\n\n"

            if 'btech' in user_input or 'engineering' in user_input:
                response += "\n🔧 B.Tech Branches Available:\n"
                for branch in self.kb['engineering_branches']:
                    response += f"  • {branch}\n"

            return response

        elif intent == 'eligibility':
            response = "📋 Eligibility Criteria:\n\n"

            if 'btech' in user_input or 'engineering' in user_input:
                response += f"B.Tech: {self.kb['eligibility']['btech']}\n"
            elif 'bba' in user_input or 'management' in user_input:
                response += f"BBA: {self.kb['eligibility']['bba']}\n"
            elif 'mtech' in user_input:
                response += f"M.Tech: {self.kb['eligibility']['mtech']}\n"
            elif 'mba' in user_input:
                response += f"MBA: {self.kb['eligibility']['mba']}\n"
            else:
                for program, criteria in self.kb['eligibility'].items():
                    response += f"• {program.upper()}: {criteria}\n"

            return response

        elif intent == 'fees':
            response = "💰 Fee Structure:\n\n"

            if 'btech' in user_input or 'engineering' in user_input:
                response += f"B.Tech: {self.kb['fees']['btech']}\n"
            elif 'bba' in user_input:
                response += f"BBA: {self.kb['fees']['bba']}\n"
            elif 'mtech' in user_input:
                response += f"M.Tech: {self.kb['fees']['mtech']}\n"
            elif 'mba' in user_input:
                response += f"MBA: {self.kb['fees']['mba']}\n"
            else:
                for program, fee in self.kb['fees'].items():
                    response += f"• {program.upper()}: {fee}\n"

            response += "\n💡 Note: Fees may vary based on category and scholarships. Contact admissions for exact details."
            return response

        elif intent == 'entrance':
            response = "📝 Entrance Examinations:\n\n"

            if 'btech' in user_input or 'engineering' in user_input:
                response += f"For B.Tech: {self.kb['entrance_exams']['btech']}\n"
            elif 'mba' in user_input or 'management' in user_input:
                response += f"For Management: {self.kb['entrance_exams']['management']}\n"
            else:
                response += f"Engineering: {self.kb['entrance_exams']['btech']}\n"
                response += f"Management: {self.kb['entrance_exams']['management']}\n"
                response += f"Other programs: {self.kb['entrance_exams']['other']}\n"

            return response

        elif intent == 'application':
            response = "📋 Application Process:\n\n"
            for step in self.kb['application_process']:
                response += f"{step}\n"
            response += "\n💡 For detailed guidance, visit: " + self.kb['contact']['website']
            return response

        elif intent == 'contact':
            response = "📞 Contact Information:\n\n"
            response += f"📱 Phone: {self.kb['contact']['phone']}\n"
            response += f"📧 Email: {self.kb['contact']['email']}\n"
            response += f"🌐 Website: {self.kb['contact']['website']}\n"
            response += f"📍 Address: {self.kb['contact']['address']}\n"
            return response

        elif intent == 'scholarship':
            response = "🎓 Scholarship Opportunities:\n\n"
            for i, scholarship in enumerate(self.kb['scholarships'], 1):
                response += f"{i}. {scholarship}\n"
            response += "\n💡 Contact the admissions office for scholarship application details."
            return response

        elif intent == 'placement':
            response = "💼 Placement Information:\n\n"
            response += f"📊 Placement Rate: {self.kb['placements']['placement_rate']}\n"
            response += f"💵 Average Package: {self.kb['placements']['average_package']}\n"
            response += f"🏆 Highest Package: {self.kb['placements']['highest_package']}\n\n"
            response += "🏢 Top Recruiters:\n"
            response += ", ".join(self.kb['placements']['top_recruiters'])
            return response

        elif intent == 'goodbye':
            responses = [
                "Thank you for using SRM Admission Chatbot! Good luck with your application!",
                "Goodbye! Feel free to reach out if you have more questions. Best wishes!",
                "Thanks for chatting! We hope to see you at SRM. Have a great day!"
            ]
            return random.choice(responses)

        else:
            return ("I'm sorry, I didn't quite understand your query. I can help you with:\n"
                   "• Courses and programs\n"
                   "• Eligibility criteria\n"
                   "• Fees and costs\n"
                   "• Entrance exams\n"
                   "• Application process\n"
                   "• Scholarships\n"
                   "• Placements\n"
                   "• Contact information\n\n"
                   "Please rephrase your question or ask about any of these topics.")

    def chat(self, user_input):
        """Main method to process user input and return response."""
        intent = self.identify_intent(user_input)
        response = self.generate_response(intent, user_input)

        # Store conversation
        self.conversation_history.append({
            'timestamp': datetime.now(),
            'user': user_input,
            'intent': intent,
            'bot': response
        })

        return response

# Initialize session state for conversation history
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'chatbot' not in st.session_state:
    st.session_state.chatbot = SRMAdmissionChatbot(knowledge_base, intent_patterns)

# Streamlit UI
def main():
    st.set_page_config(
        page_title="SRM Admission Chatbot",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        background: linear-gradient(90deg, #1f4e79, #2e8bc0);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 20px;
    }
    .chat-message {
        padding: 10px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .user-message {
        background-color: #dcf8c6;
        margin-left: 20%;
    }
    .bot-message {
        background-color: #f1f1f1;
        margin-right: 20%;
    }
    .quick-actions {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎓 SRM Admission Enquiry Chatbot</h1>
        <p>Your AI Assistant for SRM University Admissions</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.header("🔧 Quick Actions")

        if st.button("🆕 Clear Chat History"):
            st.session_state.messages = []
            st.rerun()

        if st.button("📊 Show Analytics"):
            show_analytics()

        if st.button("📋 Export Chat History"):
            export_chat_history()

        st.header("📚 Quick Topics")
        quick_topics = [
            "What courses does SRM offer?",
            "Tell me about B.Tech eligibility",
            "What are the fees for MBA?",
            "How to apply for admission?",
            "Show me placement statistics",
            "Are there any scholarships?",
            "Contact information"
        ]

        for topic in quick_topics:
            if st.button(topic, key=f"quick_{topic[:10]}"):
                st.session_state.messages.append({"role": "user", "content": topic})
                response = st.session_state.chatbot.chat(topic)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()

    # Main chat interface
    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("💬 Chat with SRM Admission Bot")

        # Display chat messages
        chat_container = st.container()
        with chat_container:
            for message in st.session_state.messages:
                if message["role"] == "user":
                    st.markdown(f"""
                    <div class="chat-message user-message">
                        <strong>You:</strong> {message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-message bot-message">
                        <strong>SRM Bot:</strong><br>{message["content"].replace(chr(10), '<br>')}
                    </div>
                    """, unsafe_allow_html=True)

        # Chat input
        user_input = st.chat_input("Type your question about SRM admissions...")

        if user_input:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_input})

            # Get bot response
            with st.spinner("Thinking..."):
                response = st.session_state.chatbot.chat(user_input)

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

            # Rerun to update the display
            st.rerun()

    with col2:
        st.subheader("ℹ️ Help & Info")
        st.markdown("""
        **I can help you with:**
        - 📚 Courses & Programs
        - 📋 Eligibility Criteria
        - 💰 Fees & Costs
        - 📝 Entrance Exams
        - 📄 Application Process
        - 🎓 Scholarships
        - 💼 Placements
        - 📞 Contact Information

        **Example questions:**
        - "What B.Tech courses do you offer?"
        - "Tell me about MBA fees"
        - "How can I apply?"
        - "Show placement statistics"
        """)

        # Statistics
        if st.session_state.messages:
            st.subheader("📊 Chat Statistics")
            st.metric("Total Messages", len(st.session_state.messages))
            st.metric("Your Questions", len([m for m in st.session_state.messages if m["role"] == "user"]))

def show_analytics():
    """Display chat analytics."""
    st.subheader("📊 Chat Analytics")

    history = st.session_state.chatbot.conversation_history

    if history:
        # Intent distribution
        intent_counts = {}
        for entry in history:
            intent = entry['intent']
            intent_counts[intent] = intent_counts.get(intent, 0) + 1

        st.bar_chart(intent_counts)

        # Recent conversations
        st.subheader("Recent Conversations")
        for i, entry in enumerate(history[-5:], 1):
            st.text(f"Query {i}: {entry['user']}")
            st.text(f"Intent: {entry['intent']}")
            st.text("---")
    else:
        st.info("No conversation data available yet.")

def export_chat_history():
    """Export chat history as JSON."""
    history = st.session_state.chatbot.conversation_history

    if history:
        # Convert to JSON-serializable format
        export_data = []
        for entry in history:
            export_data.append({
                'timestamp': entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
                'user_query': entry['user'],
                'identified_intent': entry['intent'],
                'bot_response': entry['bot']
            })

        json_data = json.dumps(export_data, indent=2, ensure_ascii=False)

        st.download_button(
            label="📥 Download Chat History",
            data=json_data,
            file_name=f"srm_chatbot_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
        st.success("Chat history ready for download!")
    else:
        st.warning("No chat history to export.")

if __name__ == "__main__":
    main()

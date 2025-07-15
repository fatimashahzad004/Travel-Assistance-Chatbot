from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def get_travel_response(user_input):
    if not user_input:
        return "Please enter your query."

    user_input = user_input.lower().strip()

    # Greeting: Hi/Hello/Hey
    if re.search(r"\b(hello|hi|hey)\b", user_input):
        return "Hello! Welcome to GlobeTrotter Travel Agency. How can I assist you today?"
    
    if re.search(r"\b(how\s*(are|r)\s*(you|u)|what'?s\s*up|how'?s\s*it\s*going)\b", user_input):
        return "I am fine, thank you! 😊 How can I assist you today?"

    if re.search(r"\b(question|enquiry|inquiry|doubt|query|queries|ask|help|info|information|details|can you tell me|i want to ask|could you explain|what about|how do i|how to|can i know|please tell me)\b", user_input):
        return ("Sure! I'm here to help. Please tell me what you would like to know about your travel plans.")
    
    if re.search(r"\b(locations|places|spot|spots|place|location|destination|publicplaces)\b", user_input):
        return ("We offer amazing trips to Bali, Europe, Dubai, Switzerland, Maldives, and more!")
    
    

    # Greeting: Salam / Assalam o Alaikum
    if re.search(r"\b(assalam\s*o\s*alaikum|as-salamu\s*alaikum|salam)\b", user_input):
        return "Wa Alaikum Assalam! Welcome to GlobeTrotter Travel Agency. How may I help you?"

    

    # Farewells
    if re.search(r"\b(bye|goodbye|see you|take care|allah\s*hafiz)\b", user_input):
        return "Allah Hafiz! Have a safe and pleasant journey."

    # Hotel/Accommodation
    if re.search(r"\b(hotel|accommodation|stay|lodging)\b", user_input):
        return ("We offer a range of hotel and accommodation options from budget to luxury. "
                "Please share your destination and travel dates.")

    # Tour package offers/discounts
    if re.search(r"\b(tour\s*packages?|offers|discounts|deals|travel\s*deals)\b", user_input):
        return ("We have exciting tour packages with seasonal discounts. "
                "Would you like to hear about domestic or international packages?")

    # Travel Insurance
    if re.search(r"\b(insurance|travel\s*insurance)\b", user_input):
        return ("We recommend adding travel insurance for peace of mind. "
                "It covers trip cancellations, medical emergencies, and more.")
    
    if re.search(r"\b(book|booking|booked)\b.*\b(tour|trip|travel)\b", user_input, re.I):
        return "Great! Let's book your tour. Please provide your destination."
    
    # Local Transportation
    if re.search(r"\b(local\s*transportation|local\s*travel|getting\s*around|commute|taxi|bus|metro)\b", user_input):
        return ("We can help you with local transportation options including taxis, rental cars, and public transit info. "
                "Where will you be staying?")

    # Group Booking Discounts
    if re.search(r"\b(group\s*booking|group\s*discounts|bulk\s*tickets)\b", user_input):
        return ("We offer special discounts for group bookings. "
                "Please tell us the group size and destination.")

    # Payment Methods & Installments
    if re.search(r"\b(payment|installment|emi|credit\s*card|debit\s*card|net\s*banking)\b", user_input):
        return ("We accept payments via credit/debit cards, UPI, net banking, and EMI plans for select packages.")

    # COVID-19 Advisories
    if re.search(r"\b(covid|corona|pandemic|travel\s*advisory|restrictions)\b", user_input):
        return ("COVID-19 travel advisories vary by country. "
                "Please share your travel destination so we can provide the latest updates.")

    # Currency Exchange
    if re.search(r"\b(currency\s*exchange|money\s*conversion|foreign\s*currency)\b", user_input):
        return ("We provide currency exchange assistance and guide you on rates. "
                "Which currency do you need information about?")

    # Custom Travel Itineraries
    if re.search(r"\b(custom\s*itinerary|personalized\s*plan|custom\s*travel|tailor-made\s*tour)\b", user_input):
        return ("We specialize in custom itineraries based on your preferences. "
                "Tell us your destination, budget, and interests to get started.")

    # Bali / honeymoon packages
    if re.search(r"\b(bali|honeymoon|beach)\b", user_input):
        return ("We have amazing honeymoon packages for Bali, including 5 nights stay, "
                "airport transfers, and sightseeing tours. Would you like to know more?")

    # Europe tour
    if re.search(r"\b(europe|eurotrip|european\s*tour)\b", user_input):
        return ("Our Europe tour packages cover Paris, Rome, and Barcelona with budget-friendly options. "
                "How many days would you like to travel?")

    # Visa info
    if re.search(r"\b(visa|visa\s*requirements|visa\s*process)\b", user_input):
        return ("Visa requirements depend on your destination country. "
                "Please tell me your nationality and where you want to travel.")

    # Booking cancellation / refund
    if re.search(r"\b(cancel|booking\s*cancel|booking\s*cancellation|refund)\b", user_input):
        return ("To cancel a booking, please provide your booking reference number. "
                "Refund policies depend on the package booked.")

    # Flights
    if re.search(r"\b(flight|airfare|plane\s*tickets)\b", user_input):
        return ("We offer competitive flight booking services. "
                "Please tell me your departure and destination cities.")

    # Thanks
    if re.search(r"\b(thank you|thanks|thank)\b", user_input):
        return "You're welcome! If you have more questions, feel free to ask."

    # Fallback
    return ("Sorry, I didn't understand that. You can ask me about travel packages, visa info, "
            "hotels, discounts, payments, insurance, and more.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    reply = get_travel_response(user_input)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)



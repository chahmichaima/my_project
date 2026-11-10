class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []  
        self.messages = []     
    def call(self, other_phone):
        call_str = f"{self.phone_number} called {other_phone.phone_number}"
        print(call_str)
        self.call_history.append(call_str)
    def show_call_history(self):
        print(f"--- Call History for {self.phone_number} ---")
        for call in self.call_history:
            print(call)
    def send_message(self, other_phone, content):
        message_dict = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message_dict)
        other_phone.messages.append(message_dict)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}")
    def show_outgoing_messages(self):
        print(f"--- Outgoing Messages from {self.phone_number} ---")
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(f"To: {msg['to']} | Content: {msg['content']}")
    def show_incoming_messages(self):
        print(f"--- Incoming Messages to {self.phone_number} ---")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(f"From: {msg['from']} | Content: {msg['content']}")
    def show_messages_from(self, other_phone):
        print(f"--- Messages between {self.phone_number} and {other_phone.phone_number} ---")
        for msg in self.messages:
            if (msg["from"] == self.phone_number and msg["to"] == other_phone.phone_number) or \
               (msg["from"] == other_phone.phone_number and msg["to"] == self.phone_number):
                print(f"From: {msg['from']} To: {msg['to']} | Content: {msg['content']}")
# ==========================================
# 7. (Test your code)
# ==========================================
if __name__ == "__main__":
    phone1 = Phone("0611223344")
    phone2 = Phone("0699887766")
    print("=== tester les appeles===")
    phone1.call(phone2)
    phone1.show_call_history()
    print("\n=== tester les messages===")
    phone1.send_message(phone2, "Hello, how are you?")
    phone2.send_message(phone1, "I'm fine, thanks! And you?")
    print()
    phone1.show_outgoing_messages()
    print()
    phone1.show_incoming_messages()
    print()
    phone1.show_messages_from(phone2)
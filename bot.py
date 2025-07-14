import re
import random
from datetime import datetime

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.crypto_db = {
            "Bitcoin": {
                "symbol": "BTC",
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10,
                "current_price": "$67,500",
                "24h_change": "+2.5%",
                "risk_level": "medium"
            },
            "Ethereum": {
                "symbol": "ETH",
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10,
                "current_price": "$3,200",
                "24h_change": "+1.2%",
                "risk_level": "medium"
            },
            "Cardano": {
                "symbol": "ADA",
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10,
                "current_price": "$0.45",
                "24h_change": "+3.1%",
                "risk_level": "low"
            },
            "Solana": {
                "symbol": "SOL",
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "low",
                "sustainability_score": 7/10,
                "current_price": "$145",
                "24h_change": "+4.2%",
                "risk_level": "high"
            },
            "Dogecoin": {
                "symbol": "DOGE",
                "price_trend": "volatile",
                "market_cap": "medium",
                "energy_use": "medium",
                "sustainability_score": 4/10,
                "current_price": "$0.08",
                "24h_change": "-1.5%",
                "risk_level": "very_high"
            }
        }
        
        self.greetings = [
            "Hey there! 🚀 Ready to explore the crypto universe?",
            "Welcome to CryptoBuddy! Let's find you some digital gold! ✨",
            "Greetings, crypto explorer! 🌟 How can I help you today?",
            "Hey! Your friendly neighborhood crypto advisor here! 💎"
        ]
        
        self.farewells = [
            "Happy trading! Remember: DYOR (Do Your Own Research)! 📊",
            "See you later! May your portfolios be ever green! 🌱",
            "Goodbye! Keep those diamond hands strong! 💎🙌",
            "Catch you on the flip side! Trade wisely! 🚀"
        ]
        
        self.disclaimer = "⚠️ DISCLAIMER: This is for educational purposes only. Cryptocurrency investments are highly risky. Always do your own research and never invest more than you can afford to lose!"
    
    def get_greeting(self):
        return random.choice(self.greetings)
    
    def get_farewell(self):
        return random.choice(self.farewells)
    
    def analyze_query(self, query):
        query = query.lower()
        
        # Greeting patterns
        if any(word in query for word in ['hello', 'hi', 'hey', 'start', 'help']):
            return self.handle_greeting()
        
        # Farewell patterns
        if any(word in query for word in ['bye', 'goodbye', 'exit', 'quit', 'stop']):
            return self.handle_farewell()
        
        # Sustainability queries
        if any(word in query for word in ['sustainable', 'green', 'eco', 'environment', 'energy']):
            return self.handle_sustainability_query()
        
        # Profitability queries
        if any(word in query for word in ['profitable', 'rising', 'trending', 'bullish', 'growth']):
            return self.handle_profitability_query()
        
        # Risk queries
        if any(word in query for word in ['safe', 'low risk', 'stable', 'secure']):
            return self.handle_risk_query()
        
        # High risk queries
        if any(word in query for word in ['high risk', 'volatile', 'risky', 'aggressive']):
            return self.handle_high_risk_query()
        
        # Specific crypto queries
        for crypto in self.crypto_db:
            if crypto.lower() in query or self.crypto_db[crypto]['symbol'].lower() in query:
                return self.handle_specific_crypto_query(crypto)
        
        # Market overview
        if any(word in query for word in ['market', 'overview', 'summary', 'all']):
            return self.handle_market_overview()
        
        # Default response
        return self.handle_default_query()
    
    def handle_greeting(self):
        return f"{self.get_greeting()}\n\nI can help you with:\n🔍 Crypto analysis and recommendations\n📊 Market trends and price movements\n🌱 Sustainability ratings\n💰 Investment advice\n\nWhat would you like to know about?"
    
    def handle_farewell(self):
        return f"{self.get_farewell()}\n\n{self.disclaimer}"
    
    def handle_sustainability_query(self):
        # Find most sustainable crypto
        sustainable_cryptos = sorted(
            self.crypto_db.items(),
            key=lambda x: x[1]['sustainability_score'],
            reverse=True
        )
        
        top_sustainable = sustainable_cryptos[0]
        crypto_name = top_sustainable[0]
        crypto_data = top_sustainable[1]
        
        response = f"🌱 **Most Sustainable Crypto: {crypto_name} ({crypto_data['symbol']})**\n\n"
        response += f"• Sustainability Score: {crypto_data['sustainability_score']:.1f}/10\n"
        response += f"• Energy Use: {crypto_data['energy_use'].title()}\n"
        response += f"• Current Price: {crypto_data['current_price']}\n"
        response += f"• 24h Change: {crypto_data['24h_change']}\n\n"
        response += f"Why it's sustainable: {crypto_name} uses a proof-of-stake consensus mechanism, which is much more energy-efficient than proof-of-work systems! 🌍\n\n"
        response += f"{self.disclaimer}"
        
        return response
    
    def handle_profitability_query(self):
        # Find rising cryptos with high market cap
        profitable_cryptos = [
            (name, data) for name, data in self.crypto_db.items()
            if data['price_trend'] == 'rising' and data['market_cap'] in ['high', 'medium']
        ]
        
        if not profitable_cryptos:
            return "Currently no cryptos match the rising trend criteria. Market conditions are always changing!"
        
        response = "📈 **Top Profitable Picks:**\n\n"
        for i, (name, data) in enumerate(profitable_cryptos[:3], 1):
            response += f"{i}. **{name} ({data['symbol']})**\n"
            response += f"   • Price: {data['current_price']}\n"
            response += f"   • 24h Change: {data['24h_change']}\n"
            response += f"   • Market Cap: {data['market_cap'].title()}\n"
            response += f"   • Risk Level: {data['risk_level'].replace('_', ' ').title()}\n\n"
        
        response += f"💡 Tip: Diversify your portfolio and consider both short-term gains and long-term potential!\n\n"
        response += f"{self.disclaimer}"
        
        return response
    
    def handle_risk_query(self):
        # Find low-risk cryptos
        safe_cryptos = [
            (name, data) for name, data in self.crypto_db.items()
            if data['risk_level'] in ['low', 'medium'] and data['market_cap'] == 'high'
        ]
        
        response = "🛡️ **Lower Risk Options:**\n\n"
        for i, (name, data) in enumerate(safe_cryptos, 1):
            response += f"{i}. **{name} ({data['symbol']})**\n"
            response += f"   • Risk Level: {data['risk_level'].replace('_', ' ').title()}\n"
            response += f"   • Market Cap: {data['market_cap'].title()}\n"
            response += f"   • Price Trend: {data['price_trend'].title()}\n"
            response += f"   • Current Price: {data['current_price']}\n\n"
        
        response += f"💡 Remember: Even 'safer' cryptos are still volatile compared to traditional investments!\n\n"
        response += f"{self.disclaimer}"
        
        return response
    
    def handle_high_risk_query(self):
        # Find high-risk cryptos
        risky_cryptos = [
            (name, data) for name, data in self.crypto_db.items()
            if data['risk_level'] in ['high', 'very_high']
        ]
        
        response = "⚡ **High Risk, High Reward Options:**\n\n"
        for i, (name, data) in enumerate(risky_cryptos, 1):
            response += f"{i}. **{name} ({data['symbol']})**\n"
            response += f"   • Risk Level: {data['risk_level'].replace('_', ' ').title()}\n"
            response += f"   • 24h Change: {data['24h_change']}\n"
            response += f"   • Price Trend: {data['price_trend'].title()}\n"
            response += f"   • Current Price: {data['current_price']}\n\n"
        
        response += f"⚠️ WARNING: These are highly volatile! Only invest what you can afford to lose completely!\n\n"
        response += f"{self.disclaimer}"
        
        return response
    
    def handle_specific_crypto_query(self, crypto_name):
        data = self.crypto_db[crypto_name]
        
        response = f"📊 **{crypto_name} ({data['symbol']}) Analysis:**\n\n"
        response += f"• Current Price: {data['current_price']}\n"
        response += f"• 24h Change: {data['24h_change']}\n"
        response += f"• Price Trend: {data['price_trend'].title()}\n"
        response += f"• Market Cap: {data['market_cap'].title()}\n"
        response += f"• Energy Use: {data['energy_use'].title()}\n"
        response += f"• Sustainability Score: {data['sustainability_score']:.1f}/10\n"
        response += f"• Risk Level: {data['risk_level'].replace('_', ' ').title()}\n\n"
        
        # Add personalized advice
        if data['sustainability_score'] >= 0.7:
            response += f"🌱 Great choice for eco-conscious investors!\n"
        if data['price_trend'] == 'rising':
            response += f"📈 Currently showing positive momentum!\n"
        if data['risk_level'] == 'low':
            response += f"🛡️ Relatively stable option in the crypto space!\n"
        
        response += f"\n{self.disclaimer}"
        
        return response
    
    def handle_market_overview(self):
        response = "📊 **Crypto Market Overview:**\n\n"
        
        for name, data in self.crypto_db.items():
            trend_emoji = "📈" if data['price_trend'] == 'rising' else "📊" if data['price_trend'] == 'stable' else "⚡"
            response += f"{trend_emoji} **{name} ({data['symbol']})**: {data['current_price']} ({data['24h_change']})\n"
        
        response += f"\n💡 **Quick Stats:**\n"
        response += f"• Rising coins: {len([c for c in self.crypto_db.values() if c['price_trend'] == 'rising'])}\n"
        response += f"• High market cap: {len([c for c in self.crypto_db.values() if c['market_cap'] == 'high'])}\n"
        response += f"• Sustainable options: {len([c for c in self.crypto_db.values() if c['sustainability_score'] >= 0.7])}\n\n"
        
        response += f"{self.disclaimer}"
        
        return response
    
    def handle_default_query(self):
        return """🤖 I'm not sure what you're looking for, but I can help with:

• **Sustainability**: "What's the most sustainable crypto?"
• **Profitability**: "Which coins are trending up?"
• **Risk Analysis**: "What are some safe crypto options?"
• **Specific Coins**: "Tell me about Bitcoin" or "What about ETH?"
• **Market Overview**: "Show me the market summary"

What would you like to know? 🚀"""
    
    def chat(self):
        print(f"\n{'='*60}")
        print(f"🤖 Welcome to {self.name}! 🚀")
        print(f"{'='*60}")
        print(self.handle_greeting())
        print(f"\n💡 Type 'help' for commands or 'quit' to exit\n")
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print(f"\n{self.name}: {self.handle_farewell()}")
                    break
                
                response = self.analyze_query(user_input)
                print(f"\n{self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: {self.handle_farewell()}")
                break
            except Exception as e:
                print(f"\n{self.name}: Oops! Something went wrong: {e}")
                print("Let's try again! 🔄")

# Example usage and testing
if __name__ == "__main__":
    # Create the chatbot instance
    crypto_bot = CryptoBuddy()
    
    # Test some queries programmatically
    print("🧪 Testing CryptoBuddy responses:\n")
    
    test_queries = [
        "Hello!",
        "What's the most sustainable crypto?",
        "Which coins are rising?",
        "Tell me about Bitcoin",
        "What are some safe options?",
        "Show me the market overview"
    ]
    
    for query in test_queries:
        print(f"User: {query}")
        response = crypto_bot.analyze_query(query)
        print(f"CryptoBuddy: {response}")
        print("-" * 50)
    
    print("\n🚀 Ready to start interactive chat!")
    print("Uncomment the line below to start chatting:")
    print("# crypto_bot.chat()")
    
    # Uncomment the next line to start the interactive chat
    crypto_bot.chat()
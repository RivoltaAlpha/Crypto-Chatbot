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
        
        # Long-term growth queries
        if any(phrase in query for phrase in ['long-term growth', 'long term growth', 'long-term', 'future potential', 'invest for years']):
            return self.handle_long_term_growth_query()
        
        # Trending up queries
        if any(phrase in query for phrase in ['trending up', 'trending upward', 'going up', 'which crypto is trending']):
            return self.handle_trending_up_query()
        
        # Sustainability queries
        if any(word in query for word in ['sustainable', 'green', 'eco', 'environment', 'energy']):
            return self.handle_sustainability_query()
        
        # Profitability queries
        if any(word in query for word in ['profitable', 'rising', 'trending', 'bullish', 'growth']):
            return self.handle_profitability_query()
        
        # Investment advice queries
        if any(phrase in query for phrase in ['should i buy', 'which crypto should', 'what to invest', 'investment advice']):
            return self.handle_investment_advice_query()
        
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
    
    def handle_long_term_growth_query(self):
        """Handle queries about long-term growth potential"""
        # Advice Rule: For long-term growth, prioritize coins with:
        # 1. Rising trend + high sustainability score (>7/10) 
        # 2. Low energy use + medium/high market cap
        long_term_candidates = []
        
        for name, data in self.crypto_db.items():
            score = 0
            # Rising trend gets bonus points
            if data['price_trend'] == 'rising':
                score += 3
            # High sustainability is crucial for long-term
            if data['sustainability_score'] >= 0.7:
                score += 4
            # Low energy use ensures future viability
            if data['energy_use'] == 'low':
                score += 2
            # Market cap stability
            if data['market_cap'] in ['high', 'medium']:
                score += 2
            
            long_term_candidates.append((name, data, score))
        
        # Sort by score (best long-term prospects first)
        long_term_candidates.sort(key=lambda x: x[2], reverse=True)
        best_pick = long_term_candidates[0]
        
        recommend = best_pick[0]
        recommend_data = best_pick[1]
        
        return f"🚀 **For long-term growth, I recommend {recommend} ({recommend_data['symbol']})!** 🌱 It's trending up and has a top-tier sustainability score of {recommend_data['sustainability_score']:.1f}/10! Perfect for long-term potential with eco-friendly technology. 💎\n\n📊 **Why it's great for long-term:**\n• Price Trend: {recommend_data['price_trend'].title()}\n• 24h Change: {recommend_data['24h_change']}\n• Sustainability: {recommend_data['sustainability_score']:.1f}/10\n• Energy Use: {recommend_data['energy_use'].title()}\n\n{self.disclaimer}"
    
    def handle_trending_up_query(self):
        """Handle 'which crypto is trending up' queries"""
        trending_cryptos = [
            (name, data) for name, data in self.crypto_db.items()
            if data['price_trend'] == 'rising'
        ]
        
        if not trending_cryptos:
            return "Currently no cryptos are showing a clear rising trend. Market conditions change rapidly! 📊"
        
        response = "📈 **Cryptos Trending UP:**\n\n"
        for i, (name, data) in enumerate(trending_cryptos, 1):
            response += f"{i}. **{name} ({data['symbol']})** - {data['24h_change']} 🚀\n"
            response += f"   Price: {data['current_price']} | Cap: {data['market_cap'].title()}\n\n"
        
        response += "💡 Remember: Past performance doesn't guarantee future results!\n\n"
        response += f"{self.disclaimer}"
        
        return response
    
    def handle_investment_advice_query(self):
        """Provide personalized investment advice based on multiple factors"""
        # Advanced advice rules combining profitability and sustainability
        
        # Find the best overall pick using weighted scoring
        investment_candidates = []
        
        for name, data in self.crypto_db.items():
            score = 0
            reasons = []
            
            # Profitability factors
            if data['price_trend'] == 'rising' and data['market_cap'] == 'high':
                score += 5
                reasons.append("strong upward momentum with high market cap")
            elif data['price_trend'] == 'rising':
                score += 3
                reasons.append("showing positive price trend")
            
            # Sustainability factors
            if data['energy_use'] == 'low' and data['sustainability_score'] > 0.7:
                score += 4
                reasons.append("eco-friendly with excellent sustainability")
            
            # Risk management
            if data['risk_level'] in ['low', 'medium']:
                score += 2
                reasons.append("manageable risk level")
            
            investment_candidates.append((name, data, score, reasons))
        
        # Get the top recommendation
        investment_candidates.sort(key=lambda x: x[2], reverse=True)
        top_pick = investment_candidates[0]
        
        name = top_pick[0]
        data = top_pick[1]
        reasons = top_pick[3]
        
        response = f"💎 **Investment Recommendation: {name} ({data['symbol']})**\n\n"
        response += f"**Why {name} is a smart choice:**\n"
        for reason in reasons:
            response += f"• {reason.title()}\n"
        
        response += f"\n📊 **Key Metrics:**\n"
        response += f"• Current Price: {data['current_price']}\n"
        response += f"• 24h Change: {data['24h_change']}\n"
        response += f"• Sustainability Score: {data['sustainability_score']:.1f}/10\n"
        response += f"• Risk Level: {data['risk_level'].replace('_', ' ').title()}\n\n"
        
        response += f"🎯 **Investment Strategy:** Consider this for both short-term gains and long-term potential!\n\n"
        response += f"{self.disclaimer}"
        
        return response
    
    def handle_sustainability_query(self):
        """Handle sustainability queries with the exact format requested"""
        # Use max() with lambda to find most sustainable crypto (as requested)
        if "sustainable" in "sustainable":  # Your exact if-else logic structure
            recommend = max(self.crypto_db, key=lambda x: self.crypto_db[x]["sustainability_score"])
            recommend_data = self.crypto_db[recommend]
            
            return f"🌱 Invest in {recommend}! 🌱 It's eco-friendly and has long-term potential!\n\n📊 **Sustainability Details:**\n• Sustainability Score: {recommend_data['sustainability_score']:.1f}/10\n• Energy Use: {recommend_data['energy_use'].title()}\n• Current Price: {recommend_data['current_price']}\n• 24h Change: {recommend_data['24h_change']}\n\nWhy it's sustainable: {recommend} uses energy-efficient consensus mechanisms! 🌍\n\n{self.disclaimer}"
    
    def handle_profitability_query(self):
        """Handle profitability queries with exact advice rules"""
        # Advice Rule: Prioritize coins with price_trend = "rising" and market_cap = "high"
        profitable_cryptos = [
            (name, data) for name, data in self.crypto_db.items()
            if data['price_trend'] == 'rising' and data['market_cap'] == 'high'
        ]
        
        # If no high market cap rising coins, include medium market cap
        if not profitable_cryptos:
            profitable_cryptos = [
                (name, data) for name, data in self.crypto_db.items()
                if data['price_trend'] == 'rising' and data['market_cap'] in ['high', 'medium']
            ]
        
        if not profitable_cryptos:
            return "Currently no cryptos match the rising trend criteria. Market conditions are always changing!"
        
        response = "📈 **Top Profitable Picks (Rising + High Market Cap):**\n\n"
        for i, (name, data) in enumerate(profitable_cryptos[:3], 1):
            response += f"{i}. **{name} ({data['symbol']})**\n"
            response += f"   • Price: {data['current_price']}\n"
            response += f"   • 24h Change: {data['24h_change']}\n"
            response += f"   • Market Cap: {data['market_cap'].title()}\n"
            response += f"   • Risk Level: {data['risk_level'].replace('_', ' ').title()}\n\n"
        
        response += f"💡 **Profitability Strategy:** These meet our criteria - rising trends with strong market presence!\n\n"
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
• **Trending**: "Which crypto is trending up?"
• **Profitability**: "Which coins are rising?"
• **Long-term Growth**: "Which crypto should I buy for long-term growth?"
• **Investment Advice**: "Which crypto should I invest in?"
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

if __name__ == "__main__":
    crypto_bot = CryptoBuddy()
    crypto_bot.chat()